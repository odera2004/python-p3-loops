#!/usr/bin/env python3

def happy_new_year():
   count = 10
   while count > 0:
    print(count)
    count -= 1
    print("Happy New Year!")
    pass

def square_integers(nums):
    return [num ** 2 for num in nums]
 
nums = [1, 2, 3, 4, 5]
squared_elements = square_integers(nums)
print(squared_elements)
    
    # code goes here!

def fizzbuzz():
    for i in range(1, 101):
       if i % 3 == 0 and i % 5 == 0 :
          print("FizzBuzz")
       elif i % 3 == 0 :
          print("Fizz")
       elif i % 5 == 0 :
          print("Buzz")
       else:
          print(i)
       
    # code goes here!
