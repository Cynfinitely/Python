#!/usr/bin/env python
# coding: utf-8

import sys

print("Welcome to the ATM!")

#to get balance from user.
balance = int(input('Please enter full integer number.What is your balance?: '))

print('What would like to do today?')

menu = print('Menu\n1-)Balance\n2-)Deposit\n3-)Withdrawn\n4-)Exit') 

#we need while loop for reusing of the menu after any action.
while True:
    user_input = input('Select 1,2,3 or 4! ')
    
    if user_input == '1':
        print('Your balance is:',balance)
        answer = input('Do you want to continue?(yes/no) ')
        if answer == 'yes':
            continue
        elif answer == 'no':
            print('Have a nice day!')
            break
        else:
            print('please write yes or no after continue question!')
            continue
            
    elif user_input == '2':
        deposit = int(input('How much do you want to deposit? '))
        balance += deposit
        print('Your balance is:',balance)
        answer = input('Do you want to continue?(yes/no) ')
        if answer == 'yes':
            continue
        elif answer == 'no':
            print('Have a nice day!')
            break
        else:
            print('please write yes or no after continue question!')
            continue

    elif user_input == '3':
        withdrawn = int(input('How much do you want to withdrawn? '))
        balance -= withdrawn
        print('Your balance is:',balance)
        answer = input('Do you want to continue?(yes/no) ')
        if answer == 'yes':
            continue
        elif answer == 'no':
            print('Have a nice day!')
            break
        else:
            print('please write yes or no after continue question!')
            continue
    else:
        sys.exit()
        


