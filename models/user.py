from json import JSONDecodeError
from models.language import Language
from utils import generate_id
from datetime import datetime
import json


class User:
    def __init__(self,
                 username : str,
                 password : str,
                 full_name : str | None = None,
                 contacts : list | None = None,
                 language : Language | None = None,
                 created_at : datetime | None = None,
                 ):
        self.id = generate_id()
        self.username = username
        self.password = password
        self.full_name = full_name
        self.language = language or Language.ENGLISH.value
        self.created_at = created_at or str(datetime.now())
        self.contacts = contacts or []



    @staticmethod
    def load():
        try:
            with open('database/users.json', 'r') as file:
                return json.load(file)
        except JSONDecodeError as e:
            return {}

    @staticmethod
    def save(users : dict[str,dict[str,str]]):
        with open('database/users.json', 'w') as file:
            json.dump(users, file,indent = 4)

    @staticmethod
    def from_dict(user_data : dict):
        return User(
            username = user_data.get('username'),
            password = user_data.get('password'),
            full_name = user_data.get('full_name'),
            language = user_data.get('language'),
            created_at = user_data.get('created_at'),
            contacts = user_data.get('contacts'),
        )









