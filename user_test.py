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

def test_save_user(self):
        '''
        test_save_user test case to test if the User object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_info),1)

def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_info
        '''
        self.new_user.save_user()
        test_user = User("Test","Eli","20088") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_info),2) 


if __name__ == '__main__':
    unittest.main()
    