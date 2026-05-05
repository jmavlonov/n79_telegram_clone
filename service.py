import time

from models.message import Message
from session import Session
from utils import Response,generate_chat_id
from models.user import User
from models.chat import Chat
session = Session()



def add_contact(new_contact_name : str):
    users = User.load()
    user = session.check_session()
    if user is None:
        return Response("You are not logged in",401)

    if new_contact_name not in users:
        return Response(f"This user({new_contact_name} is not found your telegram db)",401)

    if new_contact_name in users[user.username]["contacts"]:
        return Response(f"This user({new_contact_name} is already added)",401)

    if new_contact_name == user.username:
        return Response("You cannot add yourself",401)


    users[user.username]["contacts"].append(new_contact_name)
    User.save(users)
    return Response("Contact added✅✅",201)


def create_chat(receiver : str):
    users = User.load()
    user = session.check_session()
    if user is None:
        return Response("You are not logged in", 401)

    chats = Chat.load()

    chat_id = generate_chat_id(user.username,receiver)

    if chat_id in chats:
        return Response(f"This chat({chat_id}) already exists",401)

    if receiver not in users:
        return Response(f"This user({receiver} is not found your telegram db)",401)

    if receiver == user.username:
        return Response("You cannot create chat with yourself",401)

    chat = Chat(chat_id)
    chat.users.append(user.username)
    chat.users.append(receiver)
    chats[chat_id] = chat.__dict__
    chat.save(chats)
    return Response(f"Chat({chat_id}) successfully created",201)



def send_message():
    users = User.load()
    messages = Message.load()
    user = session.check_session()
    if user is None:
        return Response("You are not logged in", 401)

    for index, username in enumerate(user.contacts,1):
        print(f"{index} => {username}")

    receiver = input("Enter your telegram username: ")
    message = input("Enter your message: ")

    if receiver not in user.contacts: # user.contacts
        return Response(f"This user({receiver} is not found telegram db )",401)

    chats = Chat.load()
    chat_id = generate_chat_id(user.username,receiver)
    if chat_id not in chats:
        return Response(f"This chat({chat_id}) does not exist",401)

    message = Message(
        user.username,
        receiver,
        message
    )

    messages.append(message.__dict__)
    Message.save(messages)

    chats[chat_id]["messages"].append(message.__dict__)
    Chat.save(chats)
    return Response(f"Message({chat_id}) successfully sent", 201)




def read_message():
    '''
    1) login => active user topiladi
    2) active userdagi chatlarni royxati => chat_id
    3) chats = Chat.load()
    4) chat = chats[chat_id]["messages"]

    5) for message in chats[chat_id]["messages"]:
        pass
    :return:
    '''


# sql => Structure Query Language => Postgresql









