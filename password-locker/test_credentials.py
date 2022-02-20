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
        self.assertEqual(len(Credentials.accountsCredentials),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case run
        '''
        Credentials.accountsCredentials = []

    def test_viewCredentials(self):
        '''
        test function for viewCredentials function, it returns a list of  all accounts
        '''
        self.assertEqual(Credentials.displayAccounts(), Credentials.accountsCredentials)

    def test_deleteAccount(self):
        '''
        test function to test the deleteAccount function
        '''
        self.new_account.saveAccount()
        test_account = Credentials("fb","eliki","1234")
        test_account.saveAccount()

        self.new_account.deleteAccount()
        self.assertEqual(len(Credentials.accountsCredentials),1)

    def test_generatePassword(self):
        passwordLength =8

        Credentials.passwordGenerator(self)
        



        




if __name__ == '__main__':
    unittest.main()