import requests
from bs4 import BeautifulSoup

data = requests.get(
    "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303",
    # headers=headers
)
print(data)

soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content > table > tbody > tr')

print(movies)

for m in movies:
    anchor = m.select_one('td.title > div > a')
    point = m.select_one('td.point')
    if anchor is not None:
        print(anchor.text,point.text)
