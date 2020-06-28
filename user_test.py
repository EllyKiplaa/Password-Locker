import unittest # Importing the unittest module
from user import User



class TestUser(unittest.TestCase):
        '''
        Test class that defines test cases for the user class behaviors


        Args:
        unittest.TestCase: TestCase class that helps in creating test cases

        ''' 

def setUp(self):
        
        '''
        this  Set up method is set to run before each test cases.
    
        '''
        self.new_user = User("Eli","20088") # create user object

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_username.username,"Eli")
        self.assertEqual(self.new_password.password,"20088")

def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_info= []        








if __name__ == '__main__':
    unittest.main()
    