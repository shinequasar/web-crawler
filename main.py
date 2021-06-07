import requests
from bs4 import BeautifulSoup

url = "https://www.contestkorea.com/sub/list.php?int_gbn=1&Txt_bcode=030210001"

data = requests.get(url)

if data.status_code != requests.codes.ok:
    print("접속실패")
    exit()

html = BeautifulSoup(data.text, "html.parser")

events = html.select('.list_style_2 ul > li')
for event in events[::3]:
    title = event.select_one('.title .txt').text
    host = event.select_one('.host li').text.strip().replace("주최","").replace(".","")
    target = event.select_one('li .icon_2').text.strip().replace("대상","").replace(".","").replace(" ","")
    date = event.select_one('.date div').text
    print(title, host, target, date)
