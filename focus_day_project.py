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
def fifth():
    print("Hi")
def sixth():
    print("Hi")
def seventh(): 
    print("Hi")
x = 0
a = 0
b = 0
m = 0
r = 0
h = 0
first = 0
second = 0 
third = 0 
fourth = 0
fifth = 0
sixth = 0
seventh = 0
for x in range (5, 0, -1):
    print("The game will start in" ,str(x), "seconds")
x = 0
# x is the difficulty level, a is the spread of the disease, b is the cure, m is the amount of money they have, and r is the reasearch
x = int(input("Hello and welcome to my game. There is a deadly disease spreading all throughout the world, and it is your job to stop it. You will be asked various questions, and you will answer them based on your knowledge. Please enter your difficulty level. 1 is easy, 2 is medium, 3 is hard:  "))
if x == 1: 
    b = b + 2 
    r = r + 4 
    m = m + 15    #more money and cure progress and less disease spread
elif x == 2:
    a = a + 1
    b = b + 1 
    r = r + 2 
    m = m + 12    
elif x == 3: 
    a = a + 2
    m = m + 10        #less money, less cure progress, and more disease spread
else: 
    print("Please acutually enter a number from 1 to 3")    #if they dont enter a number from 1 to 3 the game ends
    exit()

first = int(input("The disease is spreading around the world and you need to make a decision on what to do. Do you want to buy a fancy car(1) or invest some money in reasearch(2):  "))
if first == 1:
    a = a + 2 
    m = m - 5    #spread goes up, money goes way down 
    print("The spread is" ,a, "yay")
elif first == 2: 
    r = r + 5 
    a = a + 1 
    m = m - 3 
    b = b + 1
    print("The spread is" ,a, "yay")
else: 
    print("Next time, please enter either 1 or 2")      #if number is not 1 or 2, the game ends(maybe try to find another way to do this)
    exit()

second = int(input("Next, do you want to invest more money in reasearch(1) or hold an international hugging day(2): "))
if second == 1:
    r = r + 5 
    a = a + 1 
    m = m - 3 
    b = b + 1    
    print("The spread is" ,a, "yay") 
elif second == 2: 
    a = a + 3  
    print("The spread is" ,a, "yay")       #when disease spread gets too high, the game ends
    if a >= 7:      
        print("You lose. The disease spreads across the entire world and everyone dies. ")   
        exit()   
    
else: 
    print("Next time, please enter either 1 or 2")
    exit()
    
third = int(input("Next, do you want to cancel all flights(1) or fly to mars to escape the disease(2): "))
if third == 1:
    a = a + 1        # the disease spread is going down
    if a >= 7:      
        print("You lose. The disease spreads across the entire world and everyone dies. ")   
        exit()   

elif third == 2:      #if this one is chosen, game ends
    print("Your goal was to save the world not yourself! Without you there to help save the world, the world falls into anarchy and everyone dies.")
    exit()
else:
    print("Next time, please enter either 1 or 2") 
fourth = int(input("Next, do you want to get a sample of the disease to help further develop a cure(1) or do you want to cancel all country to country transportation(2): "))
if fourth == 1:        #first question that requires some brain power
    b = b + 2           
    a = a + 1
    if a >= 7:      
        print("You lose. The disease spreads across the entire world and everyone dies. ")   
        exit()   
    if b >= 5:
        print("You have finished the cure, and it has been deployed to everyone in the world. Everyone was sucessfully cured, and you were able to save the world. Congratulations!")
        exit()

elif fourth == 2:         # sample of disease helps cure go up, canceling transportation helps spread go down
    a = a - 1           # 1 is to try and end the game quickly, 2 is a slow approach

else:
    print("Next time, please enter either 1 or 2")
    exit()
fifth = int(input("You are doing well so far, there is still a chance to save the world. However things are only going to get harder from here. Now do you want to take a slow approach to this situation and invest some time and money in trying and find a cure for the disease(1) or do you want to slow down the spread of the disease by quarentining everyone(2):  "))
if fifth == 1: 
    b = b + 3 
    a = a + 2 
    m = m - 5
    if b >= 5:
        print("The cure has been finished and it has been deployed to everyone in the world. Everyone was sucessfully cured, and you were able to save the world. Congratulations!")
        exit()
elif fifth == 2:
    h = h - 5 
    print("You have slowed down the spread of the disease a lot, however the civilians are not pleased with you, so please take this into account when making further decisions")
    sixth = int(input("A lot of people aren't able to feed their families now because they aren't able to go to work now. Do you want to give people stimulus checks(1) or stop the quarentine and just tell people to be more careful and weary(2):  "))
    if sixth == 1:
        m = m - 10
        if m <= -5:
            print("You have put the government majorly in debt. You have been removed from office, and without you to help, the disease spreads across the world, and eventually kills off humanity. Better luck next time.")
            exit()
    if sixth == 2: 
        a = a + 2
else: 
    print("Next time, please enter either 1 or 2")
    exit()
seventh = int(input("Now you have to make a very tough decision. Do you want to fully invest in the cure(1) or do you want to make sure that the disease spread is slowed by issuing a stay at home notice(2)?: "))
if seventh == 1:
    print("The cure has been finished and it has been deployed to everyone in the world. Everyone was sucessfully cured, and you were able to save the world. Congratulations!")
    exit()

if seventh == 2:
    print("You lose. Even though people were supposed to stay at home, a lot of them didn't follow orders, and the super contagious disease was able to spread across the world, and kill off humanity")  
    exit()
