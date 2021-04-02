# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


print(solution(10) == 23)
