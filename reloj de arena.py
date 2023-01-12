n = int(input("Ingrese el tamaño de la figura: "))

p = (n//2)+1
for f in range(1,p):
    for c in range(1,n+1):
        if f==1:
            print("*",end="")
        else:
            if c==f:
                print("*",end="")
            else:
                if c+f==n+1:
                    print("*",end="")
                else:
                    print(end=" ")
 
    print()

for i in range(3,p+1):
    for u in range(1,n+1):
        if i+u==(n//2)+2:
            print("*",end="")
        else:
            if u-i==(n//2):
                print("*",end="")
            else:
                if i==p:
                 print("*",end="")
                else:
                    print(end=" ")
    print()
