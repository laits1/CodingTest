# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

from math import sqrt

def solution(n):

        return (sqrt(n) + 1) ** 2 if sqrt(n) % 1 == 0 else -1

# n = 121  /  return = 144
n = 121 
print(solution(n)) 
