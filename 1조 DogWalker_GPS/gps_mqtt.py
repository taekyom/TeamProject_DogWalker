""" 

    전체 코드 흐름 :
    1. main에서 loop함수 호출(gps_data.py 내용)
    2. loop함수에서 send_data 호출(send_data : gps → mqtt 전송하는 데이터 함수)
    3. send_data 실행
    4. MQTT 초기화(오류 방지)
    5. json data 발생
    6. gps → mqtt : 이 과정이 publish, json data로 변환 필요
    7. MQTT topic으로 전송

"""

#python으로 뽑아낸 데이터를 MQTT로 전송하는 작업
from typing import OrderedDict  #데이터 순서대로 받기
import time
import serial
import string 
import pynmea2                  #python으로 raw data를 알아볼 수 있는 숫자로 변환(분석)하는 라이브러리
import paho.mqtt.client as mqtt #python에서 MQTT를 사용하기 위한 라이브러리
import datetime as dt
import uuid                     #GPS 번역과정에서 필요한 Namespace
import json

# MQTT 브로커 설정 
dev_id = 'GPS01'
dev_uid = str(uuid.uuid3(uuid.NAMESPACE_OID, dev_id))
broker_address = '210.119.12.97'    #브로커 주소
pub_topic = 'gps01/machine1/data/'  #MQTT topic : 브로커에게 필요한 주소(전달주소)

#Mosquito : MQTT 브로커 중 대표적인 프로그램 → 클라이언트에서 메시지를 받아서 전달해주는 역할 

#send_data 구성 : Mosquito를 활영하여 MQTT방식으로 json형태의 데이터 전달
def send_data(result, lat, lon):
    if result == 'LON': #result가 raw data일 때
        send_msg = 'OK'
    elif result == 'CONN': #result가 연결됐을 때
        send_msg = 'CONN'
    else:
        send_msg = 'ERROR'

    #원하는 날짜 출력
    currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    #json data generate(발생)
    raw_data = OrderedDict()    #데이터 순서대로 받기
    raw_data['dev_id'] = dev_id
    #raw_data['dev_uid'] = dev_uid
    raw_data['prc_time'] = currtime
    raw_data['prc_msg'] = send_msg
    raw_data['gps_lat'] = lat #위도
    raw_data['gps_lon'] = lon #경도

    #publish위해 json data 변환 
    pub_data = json.dumps(raw_data, ensure_ascii=False, indent='\t')

    #mqtt_publish
    print(pub_data)
    client2.publish(pub_topic, pub_data)

#GPS 데이터 받아오기 
def loop():
    result = ""

    while True:
        port = "/dev/ttyAMA0" #사용하고 있는 시리얼 이름 
        ser = serial.Serial(port, baudrate=9600, timeout=0.5) #(포트, 전송속도, 시간초과)
        dataout = pynmea2.NMEAStreamReader()
        #데이터 출력을 NMEA로 출력하겠음 
        #NMEA(위치전송 규격)문장의 스트림을 데이터 처리 가능 
        #GPGGA - 위도,경도 알려줌 

        newdata = ser.readline()
        newdata_u = '' #newdata_u가 빈값일 때
        try:
            newdata_u = newdata.decode('utf-8') 
        except Exception as e:
            pass

        if newdata_u == '': continue #newdata_u가 빈값일 때 → 빈 값일 때는 decode하지 않도록(오류 방지)
        if newdata_u[0:6] == "$GPRMC": #[시작 : 마지막] → 0번째부터 6-1번째까지 슬라이스
            new_gps = pynmea2.parse(newdata_u)  #newdata_u를 parsing
            result = "LON"
            #if new_gps.latitude :
               #lat = "lat"
            #if new_gps.longitude:
               #lon = "lon"
            lat = new_gps.latitude
            lon = new_gps.longitude
            #gps = "Lat : " + str(lat) + "Lon : " + str(lon)
            send_data(result,lat,lon)
            
        time.sleep(3)
        

#MQTT 초기화
client2 = mqtt.Client(dev_id)
client2.connect(broker_address, 1883)  #브로커가 서버에 접속할 수 있게 해줌
print('MQTT Client connected')         #접속 확인

#main 
if __name__=='__main__':
    send_data('CONN', None, None)
    try:
        loop()
    except KeyboardInterrupt:
        pass