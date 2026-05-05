from auth import login_user,register_user,logout_user
from service import add_contact, create_chat, send_message
from utils import Response



def menu():
    print("""
        Login        => 1
        Register     => 2
        Logout       => 3 
        Add contact  => 4
        Create Chat  => 5
        Send Message => 6
        Exit        => q
    """)
    return input("...")



def run():
    while True:
        choice = menu()
        if choice == '1':
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            response : Response = login_user(username,password)
            print(response)

        elif choice == '2':
            username = input("Enter your username : ")
            password = input("Enter your password : ")

            response: Response = register_user(username, password)
            print(response)

        elif choice == '3':
            response: Response = logout_user()
            print(response)

        elif choice == '4':
            new_contact_name = input("Enter your new contact name : ")
            response: Response = add_contact(new_contact_name)
            print(response)

        elif choice == '5':
            receiver = input("Enter your receiver : ")
            response : Response = create_chat(receiver)
            print(response)

        elif choice == '6':

            response = send_message()
            print(response)


        elif choice == 'q':
            break



if __name__ == "__main__":
    run()