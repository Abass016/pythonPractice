#this project is for the user to guess a number correctly from the range of 1-10

#import random

#print("Enter your name")
#name = input()


#print("You are asked to guess a number correctly from 1-10 " + name )

#secret_key = random.randint(1, 10)

#for trial in range(1, 6):
 #print("Guess the number")

 #guess = int(input())
 #if guess < secret_key:
  #print("your guess is low")

 #elif guess > secret_key:
  #print("your guess is high")

 #elif guess == secret_key:
  #print("your guess is correct")
  #break


#if guess == secret_key:
 #print("good Job " + name + " you have the secret number in " + str(trial) + " guess")

#else:
 #print("You guess incorrectly, The secret number is " +  str(secret_key)   +  name)   


import random

print("What is your name")

name = input()

print("You are asked to guess a number correctly within 5 trials ")

secret_key = random.randint(1, 10)

trial = 0
while trial < 5:
    
    trial+=1
    print("Guess a number")
    guess = int(input())
    if guess < secret_key:
        print("Your guess is low")

if guess == secret_key :
   print("Good Job, " + name + " you have guess the number correctly in " + str(trial) +  " guess" )  
else:
   print("You have guess the number wrongly, " + name + " the correct number is " + str(int(secret_key)))     
  


