import json
from datetime import datetime
from json import JSONDecodeError


class Message:
    def __init__(self,
                 sender: str,
                 receiver : str,
                 message : str,
                 created_at : datetime | None = None):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.created_at = created_at or str(datetime.now())

    @staticmethod
    def load():
        try:
            with open('database/messages.json', 'r') as file:
                return json.load(file)
        except JSONDecodeError as e:
            return []

    @staticmethod
    def save(messages: dict[str, dict[str, str]]):
        with open('database/messages.json', 'w') as file:
            json.dump(messages, file, indent=4)

