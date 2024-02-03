#Simple Calculator
"""summation , division, multiplication,subtraction,Exponentation,Rootover"""
import math


def sum(a,b):
    s=a+b
    print(s)
def div(c,d):
    d=c/d
    print(d)
def mult(e,f):
    n=e*f
    print(n)
def sub(g,h):
    g=g-h
    print(g)
def expo(a,m):
    f=a**m
    print(f)
def root(r):
    a=math.sqrt(r)
    print(a)

while True:
    print("If You Want to get root ,Enter Only the Value of A ,and set b to 0")
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))

    print("1.Summation\n2.Subtraction\n3.Multiplication\n4.Divission")
    print("5.Power\n6.Root\n7.exit")

    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        sum(a,b)
    elif ch == 2:
        sub(a,b)
    elif ch == 3:
        mult(a,b)
    elif ch == 4:
        div(a , b)
    elif ch == 5:
        expo(a,b)
    elif ch == 6:
        root(a)
    elif ch ==7:
        print("Thank you for using our calculator")
        break

    else:
        print("Your Choice Is Not Correct!Enter a correct Choice!")


"""Created By AAKHS B1 ! 
siam , Shakib , Jahid , Himel , Rashed , Maria , Mahabuba"""