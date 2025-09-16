#다음 코드의 실행 결과는?

def fnCalculation(x, y):
    result = 0
    for i in range(len(x)):
        temp = x[i:i+len(y)]
        if temp == y:
            result += 1
    return result

a = "abdcabcabca"
p1 = "ab"
p2 = "ca"

out = f"ab{fnCalculation(a, p1)}ca{fnCalculation(a, p2)}"
print(out)