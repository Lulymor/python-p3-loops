#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    new_list = list()
    for num in int_list:
        new_num = (num * num)
        new_list.append(new_num)
    return new_list
        

def fizzbuzz():
    for i in range(101):    
        if i == 0:
            i+1
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz") 
        else:
            print(i)