# try and catch and except

#def div42By(divideby):
 ##   return 42/divideby


#print(div42By(2))
#print(div42By(3))
#print(div42By(0))
#print(div42By(8))



def div45by(divideby):
    try:
        return div45by
    except ZeroDivisionError:
        print("Error: You tried to divide by Zero")


print(div45by(5))
print(div45by(9))
print(div45by(0))
print(div45by(3))    



print("How many cats do you have")

NumCats = input()

try:

 if int(NumCats) > 4:
    print("thats is a lot of cats")
 else:
    print("that is not many cats")

except ValueError       :
   print(" you refused to enyter a number")
