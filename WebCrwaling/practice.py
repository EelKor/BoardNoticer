from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://plus.cnu.ac.kr/_prog/_board/?code=sub07_0701&site_dvs_cd=kr&menu_dvs_cd=0701")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.title)
 