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

