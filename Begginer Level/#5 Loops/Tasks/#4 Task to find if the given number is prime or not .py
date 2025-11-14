# Task to  find if the given number by user is prime or not 

number= int (input("\t Please enter the number which you want to check \n"))

i=2

while(i<17):
    if (number==0 or number==1 ):
        print ("It is a prime number")
        break
    elif(number/i==0):
        print("It is not a prime number ")
        break

    else :
        print ("It is a prime number  ")
        break

    




