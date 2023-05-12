

"""n=int(input("enter the numer"))
for i in range(n,0,-2):
    print(i)"""


"""n=int(input("enter the number of rows"))
k=65
for i in range(n):
    for j in range(0,i+1):
        print(chr(k+j),end="")
    print()"""

"""n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

""""n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()"""


n=int(input("enter the number of rows"))
k=65
for i in range(n):
    for j in range(1,i+1):
        print(chr(k+j),end="")
    print()