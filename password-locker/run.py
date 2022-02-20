
from user import User
from credentials import Credentials
from click import confirm


def main():
    print("Hello Welcome to your pasword locker.")
    print('Creat an account to store all your passwords safe and in one place')
    proceed =confirm('continue?')
    if proceed:
        print('here we are')
        
        user_name = input('Enter the username: ')
        myPassword = input("password: ")
        confirm_password = input("Confirm password: ")
       
        if myPassword != confirm_password:
             print("Password does not match")
             while myPassword != confirm_password:
                 myPassword = input("password: ")
                 confirm_password = input("Confirm password: ")
                
        print(f"{user_name} you have been loged in successfully!")
        new_user = User(user_name, myPassword)
        print(len(User.user_login_information))
        User.saveLoginInfo(new_user)
        print(len(User.user_login_information))
        print(User.user_login_information
        )
        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : cc - create a new account credentials, dc - display all account credentials, fc -find a contact, ex -exit the contact list ")

                short_code = input().lower()

                if short_code == 'cc':
                       
                        print ("Account name ....")
                        name = input()

                        print("username ...")
                        username = input()

                        print("Password ...")
                        password = input()

                        new_account = Credentials(name, username, password)
                        Credentials.saveAccount(new_account) # create and save new account.
                        print ('\n')
                        print(f"New Account credentials {user_name} {password} for {name} account created")
                        print ('\n')

               
if __name__ == '__main__': 
    main()