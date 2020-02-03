import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908' ,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_li = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 1
for music in music_li:
    a_tag = music.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        title = a_tag.text
        artist = music.select_one('td.info > a.artist.ellipsis').text
        print(rank,title,artist)
        doc = {
            'rank' : rank,
            'title' : title,
            'artist' : artist
        }
        db.music_li.insert_one(doc)
        rank += 1



