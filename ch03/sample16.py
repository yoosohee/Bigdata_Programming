list_value_1 = ['1', '2', '3']
list_value_2 = ['4', '5', '6']

print('list_value_1: ', id(list_value_1))
print('list_value_2: ', id(list_value_2))

list_value_1.extend(list_value_2)

print('-'*50)
print(list_value_1)
print(list_value_2)
print('list_value_1: ', id(list_value_1))
print('list_value_2: ', id(list_value_2))

'''
list_value_3 = list_value_1 + list_value_2
print(list_value_1)
print(list_value_2)
print(list_value_3)
'''

'''
list_value_1 = list_value_1 + list_value_2

print(list_value_1)
print(list_value_2)

print(id(list_value_1)) # id가 바뀜
print(id(list_value_2)) 
'''
