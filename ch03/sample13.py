my_book = (2002, '파이썬', 200, '1교시')
your_book = [2002, '파이썬', 200, '1교시']
#              0,     1,     2,    3

# other_book = [your_book[0], your_book[1], your_book[2], your_book[3]]
other_book = your_book[0:4] # 이게 더 쉽죵 ^^ ㅎㅎ
# other_book = your_book[:]

print(my_book)
print(your_book)
print(other_book)

print(id(my_book))
print(id(your_book))
print(id(other_book))

other_book[0] = 2025
print('my_book: ', my_book)
print('your_book: ', your_book)
print('other_book: ', other_book)

'''
new_book = your_book[1:3]
print(new_book)

new_book2 = my_book[1:3]
print(new_book2)'''

