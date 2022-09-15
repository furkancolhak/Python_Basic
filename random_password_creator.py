# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


""" Firstly import our libraries"""
import string
import random


""" With string library define char_list with all characters in computer"""
char_list = [string.punctuation , string.digits , string.ascii_lowercase , string.ascii_uppercase]



""" Define password as a empty string"""
password = ''


""" We want to choose all different characters as two of lowercase characters ande two of punctuation characters etc. 
    and add these random characters to empty password string"""
    
for i in range(4):
    password += random.choice(char_list[0])
for i in range(4):
    password += random.choice(char_list[1])
for i in range(4):
    password += random.choice(char_list[2])
for i in range(4):
    password += random.choice(char_list[3])
    
""" After that you need shuffle because return of these comments is always same order. Before than shuffle you need to
    turn your string to list"""
password = list(password)

random.shuffle(password)


""" When you print password you are going to see your password as a list. You need to convert to string again."""

new_password = ''
for i in (password):
    new_password += i

print("Your password is : " , new_password)