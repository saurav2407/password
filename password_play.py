import time
remember = open('data.txt', 'r')

dict={'pas':remember.read()}
n=5
remember = open('data.txt', 'r')

while True:
    tut=5
    n-=1
    pas=input('Enter password:')
    if pas==dict['pas']:
        print('access Granted')
        break
    else:
        print('wrong password')
        print(f'Remainss {n} attempt.')

        if (n == 0):
            print('too many attempts')
            print(f'please wait for {tut} seconds')
            time.sleep(tut)
            print('Because of too many attempts\nyyour phone is blocked')
            print('For unblock your mobile \n Enter your e-mail')
            email=input('enter your e-Mail:')
            if email=='sauravpathak24072003@gmail.com':
                print('An otp has been sent to registered email saurav************ account')
                recovery=input('Enter OTP:')
                if recovery=='123456':
                    print('your old password is ',{dict['pas']})
                    new_pass=input('Change Your Password:')
                    dict.update({'pas':new_pass})
                    print('your  New password is',{dict['pas']})
                    remember = open('data.txt', 'w')
                    remember.write(new_pass)
                    remember.close()
                    break            
            else:
                print('An otp has been sent to registered  email saurav************ account')
                recovery=input('Enter OTP:')
                if recovery=='123456':
                    print('your  password is',{dict['pas']})
                    new_pass=input('Change Your Password:')
                    dict.update({'pas':new_pass})
                    print('your  New password is',{dict['pas']})
                    remember = open('data.txt', 'w')
                    remember.write(new_pass)
                    remember.close()
                    break
                elif recovery=='exit':
                    exit()
                else:
                    print('Try Again')
                    continue

                
        
        else:
            continue
print('\nhello sir')
print('welcome to home!!')