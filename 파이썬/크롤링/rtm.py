from slackclient import SlackClient
import time

slack_token = 'xoxp-634835311463-621555241475-632974133685-f74641c66e47253cf9ec651e30bd4331'
sc = SlackClient(slack_token)

if sc.rtm_connect():
	while True:
		receive_data = sc.rtm_read()
		print(receive_data)
		time.sleep(1)
else :
	print("connection failed")