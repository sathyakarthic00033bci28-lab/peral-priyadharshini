
1
n=5
for i in range(n):
    for j in range (n):
        print ('*',end='')

2
n=5
for i in range(n):
    for j in range(n):
        print ('*',end='')
    print( )


3

n=5
for i in range(n):
    for i in range(i+1):
        print('*',end='')
    print()


4
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()
    

5
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i,n-1):
        print('*',end='')
    print()



6
n=5
for i in range(n):
    for j in range(n):
        print ('a',end='')
    print( )



7
n=5
for i in range(n):
    for j in range(n):
        print (j,end='')
    print( )




8
for row in range(0,7):
    for column in range(0,5):
        if(row==0 and column in {1,2,3}):
            print('*',end='')
        elif(row in {1,2,3,4,5,6} and column in {0,4}):
            print('*',end='')
        elif(row==3 and column in {0,1,2,3,4}):
            print('*',end='')
        else:
            print('',end='')
    print()







