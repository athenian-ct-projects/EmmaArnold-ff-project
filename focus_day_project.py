# This game is for epidemic day and is written by EA '23
def x():           # x is difficulty
    print("Hi")
def a():           # a is the spread of the disease
    print("Hi")
def b():           # b is the cure progress
    print("Hi")
def m():           # m is the amount of money that they have
    print("Hi")
def r():           # r is the amount of reasearch that they have conducted(You need to set up a thing that prints informtion about the disease when r = certain numbers)
    print("Hi")
def h():           # h is the happiness of the civilians(dont make this affect too much because it isnt doing much in real life either)
    print("Hi")    
def first():       # these are the questions that are asked to the user and the inputs prompt different scenarios
    print("Hi")
def second():
    print("Hi")
def third():
    print("Hi")
def fourth():
    print("Hi")
x = 0
a = 0
b = 0
m = 0
r = 0
first = 0
second = 0 
third = 0 
fourth = 0

if a >= 7:      #when disease spread gets too high, the game ends
    print("You lost. The disease spread across the entire world and everyone died. ")   
    break
# x is the difficulty level, a is the spread of the disease, b is the cure, m is the amount of money they have, and r is the reasearch
x = input(str("Hello and welcome to my game. There is a deadly disease spreading all throughout the world, and it is your job to stop it. You will be asked various questions, and you will answer them based on your knowledge. Please enter your difficulty level. 1 is easy, 2 is medium, 3 is hard:  "))
if x == 1: 
    b = b + 2 and r = r + 4 and m = m + 15    #more money and cure progress and less disease spread
elif x == 2:
    a = a + 2 and b = b + 1 and r = r + 2 and m = m + 12    
elif x == 3: 
    a = a + 3 and m = m + 10        #less money, less cure progress, and more disease spread
else: 
    print("please acutually enter a number from 1 to 3")    #if they dont enter a number from 1 to 3 the game ends
    break 

first = input(int("What do you want to do next? Buy a fancy car(1) or invest some money in reasearch(2):  "))   
if first == 1:
    a = a + 2 and m = m - 5    #spread goes up, money goes way down 
elif first == 2: 
    r = r + 5 and a = a + 1 and m = m - 3 and b = b + 1
else: 
    print ("next time, please enter either 1 or 2 please")      #if number is not 1 or 2, the game ends(maybe try to find another way to do this)
    break 

second = input(int("Next, do you want to invest more money in reasearch(1) or hold an international hugging day(2): "))
if second == 1:
    r = r + 5 and a = a + 1 and m = m - 3 and b = b + 1    
elif second == 2: 
    a = a + 3    #spread goes way up, and on hard difficulty, game ends
else: 
    print ("next time, please enter either 1 or 2 please")
    break 
third = input(int("Next, do you want to cancel all flights(1) or fly to mars to escape the disease(2): "))
if third == 1:
    a = a - 1        # the disease spread is going down
elif third == 2:      #if this one is chosen, game ends
    print("Your goal was to save the world not yourself! Without you there to help save the world, the world falls into anarchy and everyone dies.")
    break 
fourth = input(int("Next, do you want to get a sample of the disease to help further develop a cure(1) or do you want to cancel all country to country transportation(2): "))
if fourth == 1:        #first question that requires some brain power
    b = b + 2           
if fourth == 2:         # sample of disease helps cure go up, canceling transportation helps spread go down
    a = a - 1           # 1 is to try and end the game quickly, 2 is a slow approach
fifth = input(int("You are doing well so far, there is still a chance to save the world. However things are only going to get harder from here. Now do you want to take a slow approach to this situation and invest some time and money in trying and find a cure for the disease(1) or do you want to slow down the spread of the disease by quarentining everyone(2):  "))
if fifth == 1: 
    b = b + 3 and a = a + 2 and m = m - 5
if fifth == 2:
    print("You have slowed down the spread of the disease a lot, however the civilians are not pleased with you, so please take this into account when making further decisions")

    

