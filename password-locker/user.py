class User:
    '''
    User class to perform user login operations
    '''
    pass
    user_login_information =[] # an array to store user login information
    
    def __init__(self,loginName, loginPassword):
        '''
        __init__ method that defines the properties of user.
        '''
        self.loginName = loginName
        self.loginPassword = loginPassword

    def saveLoginInfo(self):
        '''
        function that saves the users login information
        '''
        User.user_login_information.append(self)

   