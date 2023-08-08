print('Pathak General Kirna Storre')
print("Recipt Bill")
sum=0
while True:
    try:
        user=input('Enter your Product Price:\n')
        if user!='q':
            sum=sum+int(user)
            print(sum)
        else:
            print(f'Total payment{float(sum)} \n.')
            print('Thank You for Visiting ')

    except Exception as e:
        print(e)
