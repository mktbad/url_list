import time
from slackclient import SlackClient
import get_env

slack_token = get_env.Slack_Bots_APIToken
sc = SlackClient(slack_token)

if sc.rtm_connect():
    while sc.server.connected is True:
        print(sc.rtm_read())
        time.sleep(1)
else:
    print("Connection Failed")
