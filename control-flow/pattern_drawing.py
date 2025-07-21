num = int(input("Enter the size of the pattern: "))
i = 1
j = 1
while i in range(1, num + 1):
    while j in range(1, num + 1):
        print("*", end="")
        j += 1
    print()  
    i += 1
    j = 1 
