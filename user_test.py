import unnitest
from user import User

class TestContact(unittest.TestCase):
        '''
        Test class that defines test cases for the user class behaviours


        Args:
        unittest.TestCase: TestCase class that helps in creating test cases

        ''' 

def setUp(self):
        
        '''
        this  Set up method is set to run before each test cases.
    
        '''
        self.new_contact = User("Eli","20088") # create user object

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_username.username,"James")
        self.assertEqual(self.new_password.password,"james@ms.com")
    