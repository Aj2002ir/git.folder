file = open("tese.txt","w")
file.write("سلام")
file.close()
file = open("test.txt","r")
print(file.read())
file.close
file = open("test.txt","a")
file.write("/n")
file.close()
file = open("test.txt","r")
for line in file:
    print(line)
file.close()
