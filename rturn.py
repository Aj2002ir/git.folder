def max(a,b):
    if a>b:
        return a
    elif a==b:
        res="balance" 
        return res
    else:
        return b
a=int(input(""))
b=int(input(""))
max_of_nums= max(a,b)
print(f"max of nums {a} and {b} is {max_of_nums}")