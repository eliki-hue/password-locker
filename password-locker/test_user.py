from user import User
import unittest


class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for user behaviour
    '''
    def setUp(self) :
        '''
        set up method to run before each test case.
        '''
    self.new_user = User()