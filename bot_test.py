from slacker import Slacker
from config import CONFIG_TOKEN
# slack_token = 'xoxb-565300806020-695469067527-xW9C61S3Mr22TieUdqwNzogX'
slack_token = CONFIG_TOKEN
slack = Slacker(slack_token)
# slack.chat.post_message('#bot_test', '우리지금만나')
if __name__ == "__main__":
    slack.chat.post_message('#bots_test', "우리지금만나")
