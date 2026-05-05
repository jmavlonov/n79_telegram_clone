from uuid import uuid4
import bcrypt

def generate_id():
    return str(uuid4())


def hash_password(raw_password : str):
    encoded_password = raw_password.encode("utf-8")
    return bcrypt.hashpw(encoded_password,bcrypt.gensalt(8)).decode("utf-8")

def check_password(raw_password : str, hashed_password : str):
    encoded_raw_password = raw_password.encode("utf-8")
    hashed_password = hashed_password.encode("utf-8")
    return bcrypt.checkpw(encoded_raw_password, hashed_password)




class Response:
    def __init__(self,message:str , status_code : int = 200):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"Message: {self.message} \nStatus Code: {self.status_code}"





def generate_chat_id(sender, receiver):
    users = sorted([sender, receiver])
    return f"{users[0]}_{users[1]}"