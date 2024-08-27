#!/usr/bin/env python3
import ipdb
def happy_new_year():
    i=10
    while (i>= 0):
        if i != 0:
           print(i) 
        else:
            print("Happy New Year!")
        i-=1


def square_integers(int_list):
    # return [intgr * intgr for intgr in int_list]
    new_list= list()
    for intgr in int_list:
        res=intgr * intgr
        new_list.append(res)
    return new_list


def fizzbuzz():
   i=1
   while(i<=100):
       if i % 3 == 0 and i % 5 != 0:
           print("Fizz")
       elif i % 3 != 0 and i % 5 == 0:
           print('Buzz')
       elif i % 3 == 0 and i % 5 == 0:
           print('FizzBuzz')
       else:
           print(i)
       i+=1

