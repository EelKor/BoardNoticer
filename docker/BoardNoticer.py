from datetime import datetime
from distutils.debug import DEBUG
import time
from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

## =========================== 디버그 모드 ====================================== ##
__DEBUG__ = False

## ============================================================================= ##
today = datetime.now().date()
now = datetime.now()
isFirstMail = True
while True:
    if __DEBUG__:
        print("Hour: ",now.hour,"isFirstMail: ", isFirstMail)
    if now.hour == 7 and isFirstMail:

        #웹페이지 불러오기
        newboard_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0701&site_dvs_cd=kr&menu_dvs_cd=0701")
        #웹페이지 파싱
        newboard_soup = BeautifulSoup(newboard_html.content.decode('utf-8','replace'), 'html.parser')
        #파싱작업 끝난 데이터 필요한 부분만 추출
        newboard = newboard_soup.find('div' , {'class':'board_list'})
        newboard_num = newboard.find_all('td', {'class':'num'})
        newboard_list = newboard.find_all('td', {'class':'title'})
        newboard_date = newboard.find_all('td',{'class','date'})


        #웹페이지 불러오기
        academicInfo_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702")
        #웹페이지 파싱
        academicInfo_soup = BeautifulSoup(academicInfo_html.content.decode('utf-8','replace'), 'html.parser')
        #파싱작업 끝난 데이터 필요한 부분만 추출
        academicInfo = academicInfo_soup.find('div' , {'class':'board_list'})
        academicInfo_num = academicInfo.find_all('td', {'class':'num'})
        academicInfo_list = academicInfo.find_all('td', {'class':'title'})
        academicInfo_date = academicInfo.find_all('td',{'class','date'})


        #웹페이지 불러오기
        eduInfo_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0704&site_dvs_cd=kr&menu_dvs_cd=0704")
        #웹페이지 파싱
        eduInfo_soup = BeautifulSoup(eduInfo_html.content.decode('utf-8','replace'), 'html.parser')
        #파싱작업 끝난 데이터 필요한 부분만 추출
        eduInfo = eduInfo_soup.find('div' , {'class':'board_list'})
        eduInfo_list = eduInfo.find_all('td', {'class':'title'})
        eduInfo_num = eduInfo.find_all('td', {'class':'num'})
        eduInfo_date = eduInfo.find_all('td',{'class','date'})

        # smtp 서버 연결
        smtp_gmail = smtplib.SMTP('smtp.gmail.com',587)
        smtp_gmail.ehlo()
        smtp_gmail.starttls()
        smtp_gmail.login('lsver67@gmail.com','wduwnmckycofpblx')
        contents = "============= 새소식 ============ \n"
        for i in range(0,int(len(newboard_list) / 2)):
            contents = contents + newboard_num[i].text + "\t" + newboard_list[i].text + "\t" +  newboard_date[i].text + "\n"
        contents = contents + "\n============= 학사정보 ============ \n"
        for i in range(0,int(len(academicInfo_list) / 2)):
            contents = contents + academicInfo_num[i].text + "\t" + academicInfo_list[i].text + "\t" +  academicInfo_date[i].text + "\n"
        contents = contents + "\n============= 교육정보 ============ \n"
        for i in range(0,int(len(eduInfo_list) / 2)):
            contents = contents + eduInfo_num[i].text + "\t" + eduInfo_list[i].text + "\t" +  eduInfo_date[i].text + "\n"


        if __DEBUG__:
            print(contents)

        else:
            # 메일 내용 작성
            msg = MIMEText(contents)
            msg['Subject'] = '[알림]' + str(today) + "일 학교 공지사항 보고"
            # 메일 전송후 세션 종료
            smtp_gmail.sendmail("lsver67@gmail.com","sslee@o.cnu.ac.kr",msg.as_string())
            smtp_gmail.quit()

        isFirstMail = False
        print("Mail_sended")

    else:
        print("Waiting")
        isFirstMail = True

        if __DEBUG__:
            time.sleep(10)
            
        else:
            time.sleep(3660) ## 1 시간 대기
