from bs4 import BeautifulSoup
import requests
from datetime import date


#웹페이지 불러오기
newboard_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0701&site_dvs_cd=kr&menu_dvs_cd=0701")
#웹페이지 파싱
newboard_soup = BeautifulSoup(newboard_html.content.decode('utf-8','replace'), 'html.parser')

#파싱작업 끝난 데이터 필요한 부분만 추출
newboard = newboard_soup.find('div' , {'class':'board_list'})
newboard_list = newboard.find_all('td', {'class':'title nt'})
newboard_date = newboard.find_all('td',{'class','date nt'})

print("============= 새소식 ============ ")
for i in range(0,3):
    print(newboard_list[i].text, newboard_date[i].text)


#웹페이지 불러오기
academicInfo_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0702&site_dvs_cd=kr&menu_dvs_cd=0702")
#웹페이지 파싱
academicInfo_soup = BeautifulSoup(academicInfo_html.content.decode('utf-8','replace'), 'html.parser')

#파싱작업 끝난 데이터 필요한 부분만 추출
academicInfo = academicInfo_soup.find('div' , {'class':'board_list'})
academicInfo_list = academicInfo.find_all('td', {'class':'title nt'})
academicInfo_date = academicInfo.find_all('td',{'class','date nt'})

print("============= 학사정보 ============ ")
for i in range(0,3):
    print(academicInfo_list[i].text, " ", academicInfo_date[i].text)

#웹페이지 불러오기
eduInfo_html = requests.get("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0704&site_dvs_cd=kr&menu_dvs_cd=0704")
#웹페이지 파싱
eduInfo_soup = BeautifulSoup(eduInfo_html.content.decode('utf-8','replace'), 'html.parser')

#파싱작업 끝난 데이터 필요한 부분만 추출
eduInfo = eduInfo_soup.find('div' , {'class':'board_list'})
eduInfo_list = eduInfo.find_all('td', {'class':'title'})
eduInfo_date = eduInfo.find_all('td',{'class','date'})

print("============= 교육정보 ============ ")
for i in range(0,3):
    print(eduInfo_list[i].text,"  ",eduInfo_date[i].text)