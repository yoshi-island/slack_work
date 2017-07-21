# utf-8
# python3.5.0

from slackclient import SlackClient
import os
import password_list
import sys

# 別ディレクトリ呼び込む
sys.path.insert(0, './python-o365')
import test_o365_cal
o365_cal = test_o365_cal

token = password_list.token
channel = password_list.channel

slack_token = token
sc = SlackClient(slack_token)

o365_results = o365_cal.execution()
#start,end,start_month,category_all,category_all_month
start = o365_results[0]
end = o365_results[1]
start_month = o365_results[2]
category_all = o365_results[3]
category_all_month = o365_results[4]

msg1 = 'start: ' + start + '    end: ' + end + '\n' + category_all
msg1 = str(msg1)

msg2 = 'start: ' + start_month + '    end: ' + end + '\n' + category_all_month
msg2 = str(msg2)

sc.api_call(
  "chat.postMessage",
  channel=channel,
  text="<@channel>" + msg1,
  as_user=True
)

sc.api_call(
  "chat.postMessage",
  channel=channel,
  text="<@channel>" + msg2,
  as_user=True
)
