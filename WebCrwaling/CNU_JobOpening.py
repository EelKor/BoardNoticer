from urllib import response
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

# 오늘날짜 불러오기
currentDay = datetime.now().date()
HTMLdatetimeFormat = "%Y.%m.%d"
print(currentDay)

# 정보가 최신인지 확인
isNew = True

# 웹 페이지 5페이지 까지 검색
for page in range(1,5):

    # 접속 주소
    url = "https://plus.cnu.ac.kr/_prog/recruit/?site_dvs_cd=kr&menu_dvs_cd=07080401&gubun=1&skey=&sval=&GotoPage="+str(page)
    tr = []
    response = requests.get(url)

    print("PAGE",page)

    # 만약 웹페이지가 정상적으로 불러왔으면
    if response.status_code == 200:

        html = response
        soup = BeautifulSoup(html.content.decode('utf-8','replace'), 'html.parser')

        # 구인구직 목록 접근
        for i in range(1,11):
            selector = '#txt > div.tb_wrap > table > tbody > tr:nth-child(' + str(i) + ')'
            job = soup.select_one(selector)
            dates = datetime.strptime(job.find('td',{'class':'data'}).text, HTMLdatetimeFormat).date()

            # 만약 게시글 날짜가 오늘이면 실행, 아니면 정지
            if dates == currentDay:
                isNew = True
            else:
                isNew = False
                break

            num = job.find('td',{'class':'num'}).text
            title = job.find('td',{'class':'title'}).text
            center = job.find('td',{'class':'center'}).text
            print(num,title,center,dates)

    else:
        print(response.status_code)

    # 게시글이 오늘날짜가 아니면 5분간 정지
    if(not isNew):
        print("No New Info, Sleeping...")
        isNew = True
        time.sleep(300)
        
