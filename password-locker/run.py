
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
                print("Use these short codes : cc - create a new account credentials, dc - display all account credentials, fc -find a contact, del - to delete an account, ex -exit the contact list ")

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

                elif short_code == 'dc':

                        if Credentials.displayAccounts():
                                print("Here is a list of all your accounts credentials")
                                print('\n')

                                for account in Credentials.displayAccounts():
                                        print(f"account type: {account.accountName}     username: {account.userName} password: {account.password}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any contacts saved yet")
                                print('\n')

                # elif short_code == 'fc':

                #         print("Enter the number you want to search for")

                #         search_number = input()
                #         if check_existing_contacts(search_number):
                #                 search_contact = find_contact(search_number)
                #                 print(f"{search_contact.first_name} {search_contact.last_name}")
                #                 print('-' * 20)

                #                 print(f"Phone number.......{search_contact.phone_number}")
                #                 print(f"Email address.......{search_contact.email}")
                #         else:
                #                 print("That contact does not exist")

                elif short_code == 'del':

                        try:
                            
                            print("Enter the account name you want to delete")
                            toDelete = input("Name: ")

                            for account in Credentials.accountsCredentials:
                             if account.accountName == toDelete:
                                 confirm_delete = confirm(f'do you really want to delete {account.accountName} username: {account.userName}  password:{account.password}')
                                 if confirm_delete:
                                     Credentials.deleteAccount(account)
                                     print('\n')
                                     print('Account deleted successfully')
                                 else:
                                     break
                        except:
                            print('The account does not exist')
                        

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

if __name__ == '__main__': 
    main()