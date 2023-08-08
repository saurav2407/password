import time
a='*'
n=int(input('Enter number:'))
boo=int(input("enter '0' or '1':"))
if boo==0:
    for x in range (1,n+1):
        print(a*int(x))
if boo==1:
    for x in range (n,0,-1):
        # n=int(n)+1
        print(a*int(x))
if boo>1:
    while True:
        time.sleep(0.11)
        for x in range (1,n+1):
            print(a*int(x))
        time.sleep(0.11)
        for x in range (n,0,-1):
            n=int(n)+1
            print(a*int(x))