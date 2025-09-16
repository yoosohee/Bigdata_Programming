#다음 코드의 실행 결과는?

def cs(n):
  s = 0
  for num in range(n + 1):
    s += num
  return s

print(cs(11))