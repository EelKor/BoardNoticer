import smtplib
from email.mime.text import MIMEText

# smtp 서버 연결
smtp_gmail = smtplib.SMTP('smtp.gmail.com',587)
smtp_gmail.ehlo()
smtp_gmail.starttls()
smtp_gmail.login('lsver67@gmail.com','wduwnmckycofpblx')

# 메일 내용 작성
msg = MIMEText('내용: 본문내용 테스트')
msg['Subject'] = '제목: 메일보내기 테스트'

# 메일 전송후 세션 종료
smtp_gmail.sendmail("lsver67@gmail.com","sslee@o.cnu.ac.kr",msg.as_string())
smtp_gmail.quit()
