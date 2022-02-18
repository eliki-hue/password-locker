from user import User #impotting the User class
import unittest #importing the unittest module
from cgi import test
from modulefinder import Module


class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for user behaviour
    '''
    def setUp(self) :
        '''
        set up method to run before each test case.
        '''
        self.new_user = User('elijah', '13720')

    def test_init(self):
        '''
        test_init to test if the user login informations are initialized properly
        '''

        self.assertEqual(self.new_user.loginName,'elijah')
        self.assertEqual(self.new_user.loginPassword,'13720')
    
    def test_saveLoginInfo(self):
        '''
        saveLoginInfo function that test if the login information are saved
        '''
        self.new_user.saveLoginInfo() #saving the user lgin information
        self.assertEqual(len(User.user_login_information),1)


if __name__ == '__main__':
    unittest.main()