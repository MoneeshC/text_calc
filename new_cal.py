def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print ("Division can't be with denominator as ",end="")
        return 0

def sub(a,b):
    return a-b

while True:
    print('Enter the operation to performed:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit')
    i=input('Enter the choice:')

    while not i.isnumeric() :
        print('Enter a valid number : (i.e)1,2,3,4')
        i=input('Enter the choice:')

    i=int(i)
    if i==5:
        break
    
    try:
        a=int(input("Enter the two numbers:\n1st:"))
        b=int(input("2nd:"))
    except ValueError or NameError:
        print ("Enter a number")
    
    if i==1:
        print("The sum is : ",add(a,b))
    elif i==2:
        print("The difference is : ",sub(a,b))
    elif i==3:
        print("The product is : ",mul(a,b))
    elif i==4:
        print("The division is : ",div(a,b))

    cond=input("Want to continue: or q to exit:")
    if cond.upper()=='Q':
        break
    
    print("\n")
