from user import User #impotting the User class
import unittest #importing the unittest module
from cgi import test


class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for user behaviour
    '''
    def setUp(self) :
        '''
        set up method to run before each test case.
        '''
        self.new_user = User('elijah', '13720')
