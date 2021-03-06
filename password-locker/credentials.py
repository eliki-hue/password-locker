import string
import random

from click import confirm

class Credentials:
    '''
    Credential class to store username and passwords
    '''
    pass

    accountsCredentials = [] #an array to store all accounts credential information

    def __init__(self, accountName, userName, password):
        '''
         __init__ method that defines the properties of Credential account.
        '''

        self.accountName = accountName
        self.userName = userName
        self.password = password
    
    def saveAccount(self):
        '''
        a function that saves a new account by appending 
        it to the accountsCredentials array
        '''

        self.accountsCredentials.append(self)

    @classmethod
    def displayAccounts(cls):
        '''
        function that returns a list of all accounts
        '''

        return cls.accountsCredentials

    def deleteAccount(self):
        '''
        function that delete a specific account credentials
        '''
        Credentials.accountsCredentials.remove(self)

    def passwordGenerator():
        '''
        a function that generates a random password to set for a new account password
        '''
        
        characters = list(string.ascii_letters + string.digits)
        passwordLength = int(input("Enter the password length: ")) # enables the user to choose the password length

        random.shuffle(characters) # mixes the letters and numbers
        
        generateAnotherPassword = True
        while generateAnotherPassword:
            passwordList=[]

            for i in range(passwordLength):
                passwordList.append(random.choice(characters)) # picks a random character from character list

            password =(''.join(passwordList)) # converts the passwordList to string
            print(password)
            likePassword = confirm("Do you like the generated password? ")  #let the user decide whether they like the generated password, else a different one is generated
            
            if likePassword:
                generateAnotherPassword =False
            else:
                print('Alternative password')
        return password

