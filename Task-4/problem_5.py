number=int(input("Enter a number : "))
for i in range (0,number+3):
    for j in range(0,number-i+1):
         print(end=" ")
    for j in range(1,number-j+1):
        print("* ",end="")
    print()
