import random
game='snake','water','gun'
gam=input('enter your choice:')

a=random.choices(game)
print(a)

if game=="['snake']":
    print('snake')

elif game=='[water]':
    print('water')
elif game=='gun':
    print('gun')
else:
    print('no data found')







