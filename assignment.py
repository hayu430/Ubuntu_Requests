def addition(num1,num2):
    print("wel come to addition part")
    print("result is :",num1+num2)
def substraction(num1,num2):
    print("welcome to substraction part")
    print(num1-num2)
def mulplication(num1,num2):
    print("wel come to multiplication part")
    print("result is:",num1*num2)
def division(num1,num2):
    print("wel come to multiplication part")
    if(num2==0):
        print("divison for zero is invalid")
    else:
        print("result is :",num1/num2)
    


print("wel come to culculating")
num1=float(input("enter the first number : "))
operator=input("enter operator : ")
num2=float(input("enter the second number : "))
if(operator=="+"):
    addition(num1,num2)
elif(operator=="-"):
    substraction(num1,num2)
elif(operator=="/"):
    division(num1,num2)
elif(operator=="*" or operator=="x"):
    mulplication(num1,num2)      


   