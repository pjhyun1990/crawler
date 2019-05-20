from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn','cp949')
resp = urlopen(request)
html = resp.read().decode('cp949')  #euc-kr


bs = BeautifulSoup(html, 'html.parser')
#print(bs.prettify())

tags = bs.findAll('div', attrs={'class': 'tit3'})

for index, tag in enumerate(tags):
    print(index+1, tag.a.text, tag.a['href'], sep=':')

    print("===============================")
