import pyperclip
class Credentials:
    '''
     Class that generates new instances of credentials    
    
    '''
    credentials_list = []
def __init__(self, username,number,email,password,):
    '''
    defining the object properties
    '''    

    self.username = username
    self.number = number
    self.password = password
    self.email = email

def save_credentials(self):
    '''
    this method will save infomation of the user
    '''
    Credentials.credential_list.append(self)

def delete_credentials(self):
    '''

    delete_contact method deletes a saved contact from the users_list

    '''
    Credentials.credentials_list.remove(self)


@classmethod
def find_by_number(cls,number):
    '''
    Method that takes in a number and return a user that matches that number.
    '''
        
    for credentials in cls.credentials_list:
            if credentials.number == number:
                return credentials

def credentials_exist(cls,number):
    for credentials in cls.credentials_list:
            if credentials.number == number:
                return credentials
                
                return True        

@classmethod
def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.user_list 

@classmethod
def copy_email(cls,number):
        credentials_found = Credentials.find_by_number(number)
        pyperclip.copy(credentials_found.email)

