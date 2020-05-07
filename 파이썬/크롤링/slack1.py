from slackclient import SlackClient
from bs4 import BeautifulSoup
import requests as rq

def notification(msg):
	slack_token = 'xoxp-634835311463-621555241475-632974133685-f74641c66e47253cf9ec651e30bd4331'
	sc = SlackClient(slack_token)
	sc.api_call(
		"chat.postMessage",
		channel="#general",
		text=msg)

base_url = 'https://pjt3591oo.github.io/'

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')
posts = soup.select('body main.page-content div.wrapper div.home div.p')

result = []

for post in posts :
	title = post.find('h3').text.strip()
	des = post.find('h4').text.strip()
	author = post.find('span').text.strip()
	result.append(title)
	print(title, des, author)

notification('%d개 데이터 수집 완료'%len(result))