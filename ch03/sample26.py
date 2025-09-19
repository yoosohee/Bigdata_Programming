data = {
    'bgnde',
    'sj',
    'endde'
}

print(type(data))

# 추가
data.add('title')
data.add('title')
# 똑같은 거 추가하면 한 번밖에 안 됨
print(data)

# 삭제
data.remove('sj')
print(data)

if 'sj' in data:
    data.remove('sj')

data.discard('sj')
data.discard('sj')
data.discard('sj')
data.discard('sj') # 이렇게 하면 없는 걸 계속 지워도 error 안 뜸