# web2.py

# 웹서버에 요청
import urllib.request as rq

#크롤링
from bs4 import BeautifulSoup as bs


for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=1" + str(i)
    data = rq.urlopen(url)

    soup = bs(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")

    # <td class="title">
    # <a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
    # </td>

    for item in cartoons:
        title = item.text.strip()
        print(title)

