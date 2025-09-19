'''
다음 소스 코드는 40명의 학생에게 50~100(50이상, 100이하) 점 사이의 점수를 무작위로 할당한 딕셔너리
scores를 제공한다. 각 문제의 정답을 제시하기 위한 소스 코드를 작성하고 결과를 입력하시오.
'''

import random

scores = dict()
for i in range(10, 50 + 1):
    scores['S' + str(i)] = random.randrange(50, 100 + 1)

# 40명 학생의 평균 점수를 구하시오
avg = sum(scores.values()) / len(scores)
print(avg)