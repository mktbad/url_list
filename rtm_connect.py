from slackclient import SlackClient
import get_env
import re

slack_token = get_env.Slack_Bots_APIToken
sc = SlackClient(slack_token)


if sc.rtm_connect():
    while sc.server.connected is True:
        read_content = sc.rtm_read()
        if read_content:
            read_content_text = read_content[0].get('text')
            subtype = read_content[0].get('subtype')
            if subtype == 'bot_message':
                continue
            if read_content_text:
                sub = re.search(
                    r"(https|http)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)",
                    read_content_text)
                if sub is not None:
                    url_part = sub.group()
                    is_user = read_content[0].get('user')
                    if is_user and url_part:
                        sc.rtm_send_message("url_list", url_part)
else:
    print("Connection Failed")
