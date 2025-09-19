data = {
    'bgnde': '2025.03.01',
    'sj': '삼일절',
    'endde': '2025.03.01'
}

for key in data.keys():
    print(key)

print('-'*50)
for value in data.values():
    print(value)

print('-'*50)
for item in data.items():
    print(item)
    print(item[0], item[1])

for k, v in data.items():
    print(k, v)