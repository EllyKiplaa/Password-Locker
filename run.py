#!/usr/bin/env python3.6
from user import User
import random

def create_user(username,number,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,number,email,password)
    return new_user

def save_new_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user (user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def check_existing_users(number):
    '''
    Function that check if a users exists with that number and return a Boolean
    '''
    return User.user_exist(number)    


def main():
    print("Hello Welcome to the Password locker.Write your name then press enter")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("cu - create user account,  du - Display users, fu -find a user account, ex -exit from the password locker  ")
        short_code = input(">>>").lower()
        print('\n')
        if short_code == "cu":
            print ("New User")
            print("-"* 10)

            print ("Enter first name....")
            f_name = input(">>>")

            print ("Enter last name...")
            l_name = input(">>>")
            

            print ("Enter user email address...")
            acc_address = input (">>>")

            print ("Enter the account password...")
            acc_password = input (">>>")
            print('\n')

            save_new_user(create_user(f_name, l_name, acc_address,acc_password)) # create and save new user.
            print('\n')
            print (f"New user account {f_name} {f_name} created")
            print('\n')


        elif short_code == 'du':  
            if display_users():
                print("Here is the list of users..")
                print('\n')

                for user in display_users():
                    print(f"{user.username} {user.number} {user.email}.....{user.password}")
                    
                    print('\n')
            else:
                print('\n')
                print("You don't seem to have any users account")
                print('\n')


        elif short_code == 'fu':

            print("Enter the number you want to search for")


            search_number = input()
            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.number}")
                print(f"Email address.......{search_user.email}")
            else:
                                    print("That user does not exist")

        elif short_code == "ex":
                            print("Bye .......")
                            break
        else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
                             