import json
from database import DataBase


class IdGetter:
    def handle_msf(self, msg):
        if msg['text'] == '/start':
            id = msg['id']
            return id
