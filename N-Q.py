print("Enter the value of N:",end='\n')

n = int(input())
A = []

if(n==1):
    print("X")
    
if(n>1 and n<4):
    print("No Solution!")
elif(n>4):
    if(n%2==0):
        p, q = 0,1
        for i in range(n):
            if(i<n/2):
                A.append(q)
                q = q+2
            if(i>=n/2):
                A.append(p)
                p = p+2
    if(n%2==1):
        p, q = 1,0
        for i in range(n):
            if(i<=n/2):
                A.append(q)
                q = q+2
            if(i>n/2):
                A.append(p)
                p = p+2


def printboard(A):
    for i in range(n):
        for j in range(n):
            if(j== A[n-1-i]):
                print("X", end=' ')
            else:
                print("0", end=' ')
        print('',end='\n')

    printboard(A)
    print("\n")
