columns=[]
d=int(input("Enter no of columns : "))
g=int(input("Enter no of students : "))
e=[]

for i in range(1,d+1):
      s=input()
      columns.append(s)
print(columns)
e.append(columns)
row=[]
for k in range(d):
    t=input()
    row.append(t)
    if(k==1):
          print("2nd Row =",row)
    e.append(row)
    print(row)
    row=[]
print()
print(e)

for x in e:  
    for i in x:    
        print(i, end = " ")  
    print()
