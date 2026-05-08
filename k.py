for row in range(0,4):
    for column in range(0,3):
        if(row==0 and column in {0,2}):
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
