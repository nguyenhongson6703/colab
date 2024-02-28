# *args = parameter that will pack all argument into a tuple
# useful so that a function can accept a varying amount of arguments
# def add(*args):
#     sum = 0
#     stuff = list(args)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
# print(add(1,2,3,4,5,6))

# def hello(**kwargs):
#     print("Hello",  end = " ")
#     for key, value in kwargs.items():
#         print(value, end = " ")
# hello(tittle = "Mr.", first_name = "Bro", last_name = "Dude" )

# str.format() = optional method that give users
#               more control when displaying output
# pi = 3.14
# number = 1000
# print("The number pi is {:.3f}".format(pi))
# print("The number is  {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:X}".format(number))
# name = "Sonny"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {name:10}. Nice to meet you".format(name = "name"))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}.Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))
# animal = "cow"
# item = "moon"
# print("The " + animal + " jump over the "+ item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal,item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon"))


#learn about random library
# import random
# x = random.randint(1,6)
# y = random.random()
# print(x)
# print(y)
# mylist = ['rock', 'paper', 'clound']
# z = random.choice(mylist)
# print(z)
# cards = [1,2,3,4,5,6,7,8,9,"J", "Q", "K","A"]
# random.shuffle(cards)
# print(cards)


#exception = events detected during execution that interupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide:   "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator/ denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can divide by zero! indiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only number please")
# except Exception as e:
#     print(e)
#     print("Something was wrong :) ")
# else :
#     print("The result is {} ".format(result))
# finally:
#     print("This way always occur ! ")

# learning to work with file or directory
# import os
# path = "D:\\Hocki6\\TuHoc\\Python"
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exists")
try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

