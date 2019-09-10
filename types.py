"""
a = 'Hello'
b = 'world'
c = 2
d = a + b + str(c)
#print(d)
d = "{} {}{}!".format(a, b, c)
#print(d)

user=input('who are u: ')
f = 'Hello {name}'.format(name=user)
print(f)

f = f'Hi {user}'.lower().capitalize()
print(f.split(' '))

print(type(f))


number = int(input('Number from 1 to 10, plz: '))
if number>=0 and number<=10:
    print(number + 10)
else:
    print('sorry only 1 to 10 accepted')


name = input('Name: ')
frase = f'Hi {name}! How are u?'
print(frase)

"""


a = 0.1
print(a + 0.2)


#print(float('1'))
#print(int(2.7))
#print(bool(1))
#print(bool(''))
#print(bool(0))