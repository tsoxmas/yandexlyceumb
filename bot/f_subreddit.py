from jsonhandler import JSONHandler
import json
from id import UserName
from database import DataBase


class F_Subreddit:
    def handle_msg(self, msg):
        text = list(msg['text'].split())
        if text[0] == '/follow':
            subreddit_name_f = text[1]
            return subreddit_name_f
