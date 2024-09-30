print("enter your name")

name = input()

print("you are asked to enter a number ", name )

print("enter first number")
try :
 num = int(input())
 if num % 2 == 1:
    print("you have entered an odd number")
 else:
    print("you have entered an even number")
except ValueError:
  print("Error: You refuse to enter a number")    


