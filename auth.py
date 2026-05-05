from models.user import User
from utils import hash_password,Response,check_password
from session import Session

session = Session()

def register_user(username : str,password : str):
    user = User(username=username,password=password)
    user.password  = hash_password(user.password)
    users = User.load()
    if username in users.keys():
        return Response("User already exists",400)
    users[user.username] = user.__dict__
    User.save(users)
    return Response("User successfully registered",201)

def login_user(username : str,password : str):
    users = User.load()
    user = session.check_session() # user = None , boshlangich holatda
    if user:
        return Response("User already logged in",404)

    if username not in users:
        return Response("User doesn't exist",404)

    user_data : dict = users[username]
    user = User.from_dict(user_data)

    if not check_password(password,user.password):
        return Response("Wrong password",401)

    session.add_session(user)

    return Response("You successfully logged in ✅✅✅ ",200)



def logout_user():
    if session.check_session():
        session.remove_session()
        return Response("You successfully logged out ✅✅",200)

    return Response("You must be login firstly",401)


