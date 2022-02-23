number=int(input("Enter a number : "))
t=number
p=int(0)
r=int(0)
while number>0:
    r=(number%10)
    p=p*10+r
    number=number//10
if(t==p):
    print("True")
else:
    print("False")
