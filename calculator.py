print("enter 2 numbers ")
while(True):
    num1=int(input())
    num2=int(input())
    operator = input("enter an operator(+,-,*,/) ")
    if(operator == '+'):
        print(num1 + num2)
    elif(operator == '-'):
        print(num1 - num2)
    elif(operator == '*'):
        print(num1*num2)
    elif(operator == "/"):
        try:
            print(num1/num2)
        except Exception as e:
            print("ERROR", e)
    else:
        print("enter a proper operator ")
        print("enter 2 numbers ")
        continue
    cond=input(' type "e" to exit or anything else to continue : ')
    if(cond == 'e'):
        exit(0)
    print("enter 2 numbers")
    