# This game is for epidemic day and is written by EA '23
def x():
    print("Hi")
def a():
    print("Hi")
def b():
    print("Hi")
def m():
    print("Hi")
def r():
    print("Hi")
x = 0
a = 0
b = 0
m = 0
r = 0

if spread >= 10:
    print(input("you lost"))
    break
# x is the difficulty level, a is the spread of the disease, b is the cure, m is the amount of money they have, and r is the reasearch
x = input(str("Hello and welcome to my game. There is a deadly disease spreading all throughout the world, and it is your job to stop it. You will be asked various questions, and you will answer them based on your knowledge. Please enter your difficulty level. 1 is easy, 2 is medium, 3 is hard:  "))
if x == 1: 
    b = b + 2 and r = r + 4 and m = m + 15
elif x == 2:
    a = a + 1 and b = b + 1 and r = r + 2 and m = m + 12
elif x == 3: 
    a = a + 2 and m = m + 10
else: 
    print("please acutually enter a number from 1 to 3")

first = input(str("What do you want to do next? Buy a fancy car(1) or invest some money in reasearch(2):  "))   
if first == 1:
    (r = r + 5) and (y = y + 1) and (m = m - 3) and (x = x + 1)
if first == 2: 
    y = y + 2 and m = m - 5 

