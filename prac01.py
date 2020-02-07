from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

mus = db.music_li.find_one({'title':'가을밤 떠난 너'})

same_artist_music = list(db.music_li.find({'artist': mus['artist']}))

for ssm in same_artist_music:
    print(ssm['title'])

