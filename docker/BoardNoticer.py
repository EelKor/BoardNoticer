from datetime import datetime
import time
from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

DEBUG_MODE = True
today = datetime.now().date()
now = datetime.now()
isFirstMail = True
while True:

    if now.hour == 7 and isFirstMail:
        #웹페이지 불러오기
        newboard_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0701&site_dvs_cd=kr&menu_dvs_cd=0701")
        #웹페이지 파싱
        newboard_soup = BeautifulSoup(newboard_html.content.decode('utf-8','replace'), 'html.parser')
        #파싱작업 끝난 데이터 필요한 부분만 추출
        newboard = newboard_soup.find('div' , {'class':'board_list'})
        newboard_list = newboard.find_all('td', {'class':'title'})
        newboard_date = newboard.find_all('td',{'class','date'})
        #웹페이지 불러오기
        academicInfo_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702")
        #웹페이지 파싱
        academicInfo_soup = BeautifulSoup(academicInfo_html.content.decode('utf-8','replace'), 'html.parser')
        #파싱작업 끝난 데이터 필요한 부분만 추출
        academicInfo = academicInfo_soup.find('div' , {'class':'board_list'})
        academicInfo_list = academicInfo.find_all('td', {'class':'title'})
        academicInfo_date = academicInfo.find_all('td',{'class','date'})
        #웹페이지 불러오기
        eduInfo_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0704&site_dvs_cd=kr&menu_dvs_cd=0704")
        #웹페이지 파싱
        eduInfo_soup = BeautifulSoup(eduInfo_html.content.decode('utf-8','replace'), 'html.parser')
        #파싱작업 끝난 데이터 필요한 부분만 추출
        eduInfo = eduInfo_soup.find('div' , {'class':'board_list'})
        eduInfo_list = eduInfo.find_all('td', {'class':'title'})
        eduInfo_date = eduInfo.find_all('td',{'class','date'})

        # smtp 서버 연결
        smtp_gmail = smtplib.SMTP('smtp.gmail.com',587)
        smtp_gmail.ehlo()
        smtp_gmail.starttls()
        smtp_gmail.login('lsver67@gmail.com','wduwnmckycofpblx')
        contents = "============= 새소식 ============ \n"
        for i in range(0,10):
            contents = contents + newboard_list[i].text + " " +  newboard_date[i].text + "\n"
        contents = contents + "\n============= 학사정보 ============ \n"
        for i in range(0,10):
            contents = contents + academicInfo_list[i].text + " " +  academicInfo_date[i].text + "\n"
        contents = contents + "\n============= 교육정보 ============ \n"
        for i in range(0,10):
            contents = contents + eduInfo_list[i].text + " " +  eduInfo_date[i].text + "\n"



        # 메일 내용 작성
        msg = MIMEText(contents)
        msg['Subject'] = '[알림]' + str(today) + "일 학교 공지사항 보고"
        # 메일 전송후 세션 종료
        smtp_gmail.sendmail("lsver67@gmail.com","sslee@o.cnu.ac.kr",msg.as_string())
        smtp_gmail.quit()
        isFirstMail = False
    else:
        print("Waiting")
        isFirstMail = True
        time.sleep(3660)
