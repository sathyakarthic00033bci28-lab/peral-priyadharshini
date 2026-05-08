for row in range(0,7):
    for column in range(0,5):
        if(row==0 and column in {1,2,3}):
            print('*',end=' ')
        elif(row==6 and column in {1,2,3}):
            print('*',end=' ')
        elif(row in{1,2,3,4,5} and column in {0,4}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



for row in range(0,4):
    for column in range(0,5):
        if(row==0 and column in {0,4}):
            print('*',end=' ')
        elif(row==1 and column in{1,3}):
            print('*',end=' ')
        elif(row==3 and column in {2}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
            
            
            
for row in range(0,4):
    for column in range(0,5):
        if(row==0 and column in {0,3}):
            print('*',end=' ')
        elif(row==1 and column in{0,1,3}):
            print('*',end=' ')
        elif(row==2 and column in {0,2,3}):
            print('*',end=' ')
        elif(row==3 and column in {0,3}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
            
for row in range(0,4):
    for column in range(0,3):
        if(row==0 and column in {0,1,2}):
            print('*',end=' ')
        elif(row==1 and column in{0,1}):
            print('*',end=' ')
        elif(row==2 and column in {0,1}):
            print('*',end=' ')
        elif(row==3 and column in {0,2}):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()            
