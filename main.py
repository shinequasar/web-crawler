import csv
import requests
from bs4 import BeautifulSoup
import datetime

f = open("event_list.csv","w", encoding="utf-8-sig", newline="")

wr = csv.writer(f)
now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
wr.writerow(['최종 업데이트 날짜', now])

writer = csv.DictWriter(f,
                        fieldnames=["제목", "주최", "대상", "날짜"])
writer.writeheader()

for page_num in range(1, 33):
    url = f"https://www.contestkorea.com/sub/list.php?displayrow=12&int_gbn=1&Txt_sGn=1&Txt_key=all&Txt_word=&Txt_bcode=030210001&Txt_code1=&Txt_aarea=&Txt_area=&Txt_sortkey=a.int_sort&Txt_sortword=desc&Txt_host=&Txt_tipyn=&Txt_actcode=&page={page_num}"

    data = requests.get(url)

    if data.status_code != requests.codes.ok:
        print("접속실패")
        exit()

    html = BeautifulSoup(data.text, "html.parser")

    if data.status_code != requests.codes.ok:
        print("접속실패")
        exit()

    html = BeautifulSoup(data.text, "html.parser")

    events = html.select('.list_style_2 ul > li')

    for event in events[::3]:
        data_dict = {}
        title = event.select_one('.title .txt').text
        host = event.select_one('.host li').text.strip().replace("주최","").replace(".","")
        target = event.select_one('li .icon_2').text.strip().replace("대상","").replace(".","").replace(" ","")
        date = event.select_one('.date div').text

        data_dict["제목"] = title
        data_dict["주최"] = host
        data_dict["대상"] = target
        data_dict["날짜"] = date
        writer.writerow(data_dict)
        print(title, host, target, date)

f.close()
