data = {
    'bgnde': '2025.03.01',
    'sj': '삼일절',
    'endde': '2025.03.01'
}

print(data)
print(type(data))
print(data['sj'])

data['desc'] = '삼일절은 휴강입니다.'
print(data)

data['endde'] = '2025.04.01'
data['endde'] = '2025.05.01'
data['endde'] = '2025.06.01'
data['endde'] = '2025.07.01'
data['endde'] = '2025.08.01'
print(data)