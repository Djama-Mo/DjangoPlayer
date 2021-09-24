import requests
from bs4 import BeautifulSoup as bs
import lxml

URL = 'https://karmapolitan.ru/chart'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 '
                  'Safari/537.36 OPR/69.0.3686.77'}

r = requests.get(url=URL, headers=HEADERS)
soup = bs(r.text, 'lxml')
block = soup.select_one('div.chart-table-body')
songs = block.select('div.info-track')
covers = block.select('div.cover')
export_songs = []
for (index, song), cover in zip(enumerate(songs), covers):
    position = index + 1
    cover_url = cover.select_one('img').get('data-src')
    author = song.select_one('div.info-track__author.text--cut').text
    title = song.select_one('div.info-track__title.text--cut').text
    export_songs.append({'title': title,
                         'artist': author,
                         'position': position,
                         'cover_url': cover_url
                         })
