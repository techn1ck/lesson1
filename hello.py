#print("Hello world")
#print("Привет программист, \nку два раза")
#print(2+2)
#print(10/3)



str1 = '{:4d}'.format(42)    
print(str1)

str1 = '{:04d}'.format(42)
print(str1)
    
    # по левому краю
str1 = '{:<7}'.format('hello')
print(str1)

str1 = '{:*<7}'.format('hello')
print(str1)

    # по правому краю
str1 = '{:>7}'.format('hello')
print(str1)

str1 = '{:*>7}'.format('hello')
print(str1)

