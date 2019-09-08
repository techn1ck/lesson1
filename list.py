test_list = [3, 5, 7, 9, 10.5, 3]
#print(test_list)

test_list.append('python')
#print(len(test_list))

#test_list.sort()
print(test_list.index(9))
print(test_list[0])
print(test_list[-1])
#print(test_list[len(test_list)-1])
print(test_list[1:4])

print('Python' in test_list)

del test_list[-1] # 'python' is out

while test_list.count(3): # 3 is out
    test_list.remove(3)
print(test_list)

