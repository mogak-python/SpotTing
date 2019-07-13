from slacker import Slacker

slack_token = 'xoxb-565300806020-695469067527-xW9C61S3Mr22TieUdqwNzogX'
slack = Slacker(slack_token)
slack.chat.post_message('#bot_test', '우리지금만나')
