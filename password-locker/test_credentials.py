from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    '''
    test class that test the working of credentials class
    '''

    def setUp(self) :
        '''
        set up method to run before each test case.
        '''
        self.new_account = Credentials('facebook', 'eliki','13720')

    def test_init(self):
        '''
        test_init to test if the user login informations are initialized properly
        '''

        self.assertEqual(self.new_account.accountName,'facebook')
        self.assertEqual(self.new_account.userName,'eliki')
        self.assertEqual(self.new_account.password,'13720')

    def test_saveAccountCredentials(self):
        '''
        saving credential test function
        '''

        self.new_account.saveAccount()
        self.assertEqual(len(self.new_account),1)
        




if __name__ == '__main__':
    unittest.main()