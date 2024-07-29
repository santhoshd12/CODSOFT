import time

def Addition(a,b):
        print("The addition of",a,"and",b,"is : ",a+b)

def Subtraction(a,b):
        print("The subtraction of",a,"and",b,"is : ",a-b)

def Multiplication(a,b):
     print("The multipication of",a,"and",b,"is : ",a*b)

def Division(a,b):
        print("The division of",a,"and",b,"is : ",a/b)


while (True):
    time.sleep(1)
    print("\t--- Simple Calculator.. ---")
    time.sleep(2)
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Exit")

    print("\n Enter your choice : ")
    c = int(input())
    if c==1:
        time.sleep(1)
        print("Great your choice was addition..")
        print("Please enter the values..!")
        Addition(float(input("Enter the first value : ")), float(input("Enter the second value : ")))
    elif c==2:
        time.sleep(1)
        print("Great your choice was subtraction..")
        print("Please enter the values..!")
        Subtraction(float(input("Enter the first value : ")), float(input("Enter the second value : ")))
    elif c==3:
        time.sleep(1)
        print("Great your choice was multiplication..")
        print("Please enter the values..!")
        Multiplication(float(input("Enter the first value : ")), float(input("Enter the second value : ")))
    elif c==4:
        time.sleep(1)
        print("Great your choice was division..")
        print("Please enter the values..!")
        Division(float(input("Enter the first value : ")), float(input("Enter the second value : ")))
    else:
        print("Invalid input..")
        break


        