# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import random 


# This function is simply the opening of the program for design purposes no worry!
def display():

  title = "**** Welcome to DataMan!!!! ****"

  print("*" * len(title))

  print(title)

  print("*" * len(title))

  print("-" * 24)


# This function solves the multibules of the random numbers and checks to see if they're correct.
def problem():

# This the loop which continues until the user wants to quit.

  answer = 0
  while answer != -1:

    x = random.randint(0,9)

    y = random.randint(0,9)

    print("How much is " + str(x) + " times " + str(y) + "?")

   

    answer = int(input("What is the answer? -1 to stop "))

# This if statement checks to see if the answer is actually correct or not and gives compliments to those who are right.
    if answer == (x * y):

      correct = ['Very good!', 'Nice work!', 'Keep up the good work!']

      response = random.choice(correct)

      print(response)
# This loop is the one for the wromg answers. This loop allows you to keep going until you get it right.
    while answer != (x * y)and answer !=-1:

      incorrect = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying']

      respond = random.choice(incorrect)

      print(respond)

      print("How much is " + str(x) + " times " + str(y) + "?")

      answer = int(input("What is the answer? "))

      if answer == (x * y):

        print(respond)


def main():

  display()

  problem()


main()
    