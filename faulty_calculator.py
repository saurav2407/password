print('This calci gives wrong answer of specific numbers \n')
print('\nlike:\n    55 + 7 = 57\n \n    10 - 5 = 105 \n\n    10 * 5 = 500 \n\n    2 ** 2 = 9')
print('__'*25)
print('\n')
while True:

    a=input('enter first number:')
    c=input('enter operation')
    b=input('enter second number:')
    

    if a=='55' and c=="+" and b=="7":
        print('57')
    elif a=='10' and c=="-" and b=="5":
        print('105')
    elif a=='10' and c=="*" and b=="5":
        print('500')
    elif a=='2' and c=="**" and b=="2":
        print('9')
    elif c=='+':
        print(int(a)+int(b))
    elif c=='-':
        print(int(a)-int(b))
    elif c=='*':
        print(int(a)*int(b))
    elif c=='/':
        print(int(a)/int(b))
    elif c=='**':
        print(int(a)**int(b))
    else:
        print('Invalid Operation!!!')
        
    
    


    
    
    
    
    