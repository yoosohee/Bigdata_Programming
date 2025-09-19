my_Book = 2002, '파이썬', 200
my_Book2 = (2002, '파이썬', 200)

print(type(my_Book))
print(my_Book)

print(type(my_Book2))
print(my_Book2)

year, title, size = my_Book
print(year)
print(title)
print(size) #언패킹(unpacking)

print('-'*30) #그냥 구분선

print(my_Book[0])
print(my_Book[1])
print(my_Book[2])
# print(my_Book[3]) error!!


print('-'*30)
print(my_Book[-1])
print(my_Book[-2])
print(my_Book[-3])
# print(my_Book[-4]) error!!

print(len(my_Book))
print(my_Book[len(my_Book)-1]) # print(my_Book[-1]) 과 같은 출력이 나오지만, 복잡함
