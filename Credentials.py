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
    User.user_info.append(self)

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

