def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    if(y==0):
        return "Division by zero not possible !"
    return x/y    

if __name__=="__main__":
    x = float(input("Enter first number : "))
    y = float(input("Enter second number : "))
    op = input("Which operation do you want to perform ? (+ or - or * or /) ")
    
    if (op=='+'):
        print(add(x,y))
    elif (op=='-'):
        print(sub(x,y))
    elif (op=='/'):
        print(div(x,y))
    elif (op=='*'):
        print(mul(x,y))
    else:
        print("Invalid input !")
