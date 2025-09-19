#아래 코드를 참조 해서, 문제 풀이를 제출해 주세요.
import random

scores = dict()
for i in range(11, 50 + 1):
    scores['S' + str(i)] = random.randrange(50, 100 + 1)

best_Student, best_Score = max(scores.items(),
                               key=lambda item:(item[1], -int(item[0][1:])))

print(best_Student, best_Score)

#40명 중 최고 득점을 한 학생과 점수를 출력 하시오.
#여러 명인 경우, 학번이 가장 빠른 한 명만 출력 되도록 하시오.