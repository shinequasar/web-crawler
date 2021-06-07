import requests
from bs4 import BeautifulSoup

url = "https://www.contestkorea.com/sub/list.php?int_gbn=1&Txt_bcode=030210001"

data = requests.get(url)

if data.status_code != requests.codes.ok:
    print("접속실패")
    exit()

html = BeautifulSoup(data.text, "html.parser")

events = html.select('.list_style_2 ul > li .title')
for event in events:
    title = event.select_one('.txt')
    print(title.text)