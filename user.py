class User:
    '''
     Class that generates new instances of users    
    
    '''
    user_list = []
def __init__(self, username,number,email,password):
    '''
    defining the object properties
    '''    

    self.username = username
    self.number = number
    self.password = password
    self.email = email

def save_user(self):
    '''
    this method will save infomation of the user
    '''
    User.user_info.append(self)

def delete_user(self):
    '''
    delete_contact method deletes a saved contact from the users_list

    '''
    User.user_list.remove(self)


@classmethod
def find_by_number(cls,number):
    '''
    Method that takes in a number and return a user that matches that number.
    '''
        
    for user in cls.user_list:
            if user.number == number:
                return user

# class Credential:
#     '''
#     Class which helps the users remember their account's information easily
#     '''

# def __init__(self,Names,):
#     '''
    # '''
