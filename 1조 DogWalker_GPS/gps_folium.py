"""
    MQTT에서 받은 데이터 → WPF로 옮기기
    1. MQTT 데이터를 WPF 이용해 mssql에 저장
    2. DB 데이터를 python으로 Flask서버 실행
    Flask서버는 vscode로 오픈
    3. folium으로 출력 
    4. vs로 DogWalker 실행 시, DB 오픈 & DB 연결해야 실행 정상

"""
from flask import Flask
import folium
import pymssql
import time

#DB 서버 주소
server = '127.0.0.1'
#DB 이름
database = 'DogWalker'
#접속 유저명
username = 'sa'
#접속 유저 패스워드
password = 'mssql_p@ssw0rd!'
#mssql 접속
cnxn = pymssql.connect(server, username, password, database)

cursor = cnxn.cursor()

#SQL문 실행
coordinate = []


def new_web():
    while True:
        cursor.execute('SELECT Lat, Lon FORM GPSTBL;') #쿼리문이 그대로 DB에서 실행됨
       
        #data를 하나씩 fetch해서 출력
        row = cursor.fetchone() #fetchone() : 지정한 테이블 안의 데이터를 한 행씩 추출

        while row:
            coordinate.append([row[0], row[1]])
            row = cursor.fetchone()
        if row is None:
            break

#웹 서버로 folium map 띄우기
app = Flask(__name__)
@app.route('/')
def index():
    new_web()

    #start_coords = (35.11744755557854, 129.09058121349395) : 부경대학교 용당캠퍼스
    folium_map = folium.Map(location= coordinate[-1], zoom_start=18) #location= coordinate[-1] : 부경대학교 대연캠퍼스
    folium.PolyLine(locations=coordinate).add_to(folium_map)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(
        host= "127.0.0.1",
        port= 8080,
        debug=True
    )    

#time.sleep(10)

#연결 끊기
cnxn.close()