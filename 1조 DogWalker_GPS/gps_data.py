#GPS 데이터 값을 받기 위한 초기 작업
import serial #시리얼 통신 
import time 
import string
import pynmea2 #python으로 raw data를 알아볼 수 있는 숫자로 변환(분석)하는 라이브러리
 
while True: #항상 GPS에서 데이터를 수신하도록 True로 설정
    port = "/dev/ttyAMA0" #ttyAMA0 : 시리얼 통신을 받기 위한 Namespace
    ser = serial.Serial(port, baudrate=9600, timeout=0.5) #serial : GPS 통신
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline() #계속해서 새로운 데이터를 받음
    #print(newdata) 

    newdata_u = newdata.decode('utf-8') #받은 데이터를 utf-8로 변환
    #print(newdata_u)
    
    if newdata_u[0:6] == "$GPRMC":
        new_gps = pynmea2.parse(newdata_u) #초기 raw data → utf-8로 변환 → pynmea2로 번역(= parse, 알아볼 수 있는 데이터)
        lat = new_gps.latitude  
        lon = new_gps.longitude  
        gps = "Latitude = " + str(lat) + " Longitude = " + str(lon)
        print(gps)
        
    time.sleep(3)

"""
- putty에서 실행하는 명령 → sudo cat /dev/ttyAMA0 : GPS 모듈 실행 명령
- 알 수 없는 숫자(raw data)가 출력되는데 이 데이터 중 위도/경도만 Python으로 뽑아내는 작업이 필요
- putty에서 sudo cat /dev/ttyAMA0를 실행했을 때 출력되는 데이터 중 $GPRMC만 필요($GPRMC : 위도, 경도 데이터값)

"""
