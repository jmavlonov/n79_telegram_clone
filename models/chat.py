import json
from json import JSONDecodeError

from models.user import User
from models.message import Message

class Chat:
    def __init__(self,
                 chat_id : str,
                 ):
        self.chat_id = chat_id
        self.users : list[User] = list()
        self.messages : list[Message] = list()

    @staticmethod
    def load():
        try:
            with open('database/chats.json', 'r') as file:
                return json.load(file)
        except JSONDecodeError as e:
            return {}

    @staticmethod
    def save(chats: dict[str, dict[str, str]]):
        with open('database/chats.json', 'w') as file:
            json.dump(chats, file, indent=4)


    def __str__(self) -> str:
        return f"Chat => {self.chat_id}"







