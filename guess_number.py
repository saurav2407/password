print('This is Guess Number Game\nIn this you have to choose number around 10 to 100')
print('choose between : 10,20,30,40,50,60,70,80,90,100')
n=9
for x in range(n):
    n-=1
    enter=int(input('Guess The number:'))
    if enter==30:
        if n==0:
            print('you lost the game!!')
            print('better luch next time!!')
            
        if n==1:
            print('you give the correct answer in 8th attempt!!')
            
        if n==2:
            print('you give the correct answer in 7th attempt !!')
            
        if n==3:
            print('you give the correct answer in 6th attempt!!')
            exit
        if n==4:
            print('you give the correct answer in 5th attempt!!')
            
        if n==5:
            print('you give the correct answer in 44th attempt!!')
            
        if n==6:
            print('you give the correct answer in 3rd attempt!!')
            
        if n==7:
            print('you give the correct answer in 2nd attempt!!')
            
        if n==8:
            print('you give the correct answer in 1st attempt!!')
            print('congratulations!!!!')

                
        print('Your Guess number is true')
        print('you Won the prize!!')
                
        break
    elif enter >=30:
        print('guess low')
    else:
        print('guess High')
    
