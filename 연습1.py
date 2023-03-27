#n!을 구하는 재귀함수
# 5! = 5!*(5-1)!


def factorial(n):
    if n == 1:
        return 1

    result = n*factorial(n-1)
    return result


print(factorial(5))