num1 = float(input("number1: "))
op=str(input("inter your op:"))
num2 = float(input("number2: "))
match op:
    case"+":
     print(num1+num2)    
    case"-":
     print(num1-num2)    
    case"/":
     print(num1/num2)
    case"*":
     print(num1*num2)
    case"_":
     print("eror")