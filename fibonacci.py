n = int (input("چند جمله؟"))
a , b = 0 , 1
for i in range (n):
    print ( a )
    a , b = b , a + b
