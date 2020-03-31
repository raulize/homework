import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',

                    headers = headers

                    )

soup = BeautifulSoup(data.text, 'html.parser')
list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for lank in list:

    lankNum = lank.select_one('td.number')
    title = lank.select_one('a.title.ellipsis')
    artist = lank.select_one('a.artist.ellipsis')

    if title is not None:

        print(lankNum.text.lstrip(),"/",artist.text.lstrip(),"/",title.text.lstrip())


