'''CREATED BY MUHAMMAD HANAN ASGHAR
DATA SCIENTIST
PYTHONIST
'''
import requests
from bs4 import BeautifulSoup
import json
def InstagramScrapper(url):
    html_data = requests.get(f"{str(url)}")
    html = html_data.content
    soup = BeautifulSoup(html,"html.parser")
    body = soup.findAll("body")
    scripts = body[0].findAll('script')
    values = []
    value = scripts[0].contents[0][21:]
    page_json = value.split(' = ', 1)[0].rstrip(';')
    data = json.loads(page_json)
    json_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
    values5 = []
    for i in range(len(json_data['edge_felix_video_timeline']['edges'])):
        value = json_data['edge_felix_video_timeline']['edges'][i]['node']['thumbnail_resources'][-1]['src']
        values5.append(value[7:])
    values6 = []
    for i in values5:
        value = i.replace("&amp;","&")
        values6.append(value)
    return values6
scrap = InstagramScrapper("https://www.instagram.com/sunnyleone/?hl=en")
