#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

ERR_CONST = '-1'

# 2. Define function that takes a name as a parameter and displays the name
def print_on_screen(text):
    print(text)

def display_name(name_to_display):
    # print_on_screen('no name to display')
    if len(name_to_display)==0:
        print_on_screen('no name to display')
    else:
        print_on_screen("username: %s" % name_to_display)

# 1. Define function that asks user for his/her name and displays it.
def prompt_question(question):
    return input(question)

def ask_name():
    user_name=prompt_question('what is your name\n')
    display_name(user_name)
    return user_name

# 3. Define function “smallest” that returns the smallest number from a given list.
def smallest(given_list):
    # llaw: try with python buildin function
    try:
        return min(given_list)
    except Exception as e:
        return ERR_CONST

def smallest_detailed(given_list):
    # llaw: if you want my own implementation
    try:
        smallest=float("inf")
        for i in range(0, len(given_list)):
            smallest = min(smallest, given_list[i])
        return smallest
    except Exception  as e:
        return ERR_CONST




# 4. The following code has an error. Please fix the error and make the code display both listA and listaB.
def ask5num():
    # llaw: try best solution as i am not quite sure if i can get the question correctly...
    l=[]

    for i in range(0,5):
        number = input("please provide a number: ")
        l.append(number)

    listA = l
    listB = listA+[1]

    print('list a')
    for j in range(0,len(listA)):
        print("listA[{}] is: {}".format(j, listA[j]))

    print('list b')
    for k in range(0,len(listB)):
        print("listB[{}] is: {}".format(k,listB[j]))


# 5. Please write two functions.

# Function one to create a local variable called “a” that equals the sum of a global variable called “glob” plus 10.

# Function two to create a variable “b” that is the sum of the same “glob” variable plus 100.

# Please display the global variable and both local variables. Set your global variable to 1000.
glob = 1000
def question_5_function_one():
    a = glob + 10
    return a

def question_5_function_two():
    b = glob + 1000
    return b

def display_a():
    print("display a:%d" % question_5_function_one())

def display_b():
    print("display b:%d" % question_5_function_two())

def question_5_display():
    display_a()
    display_b()


def main():
    print('helloworld')


if __name__ == '__main__':
    main()
