# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    return [int (i) for i in list(str(n))][::-1]


n = 12345
print(solution(n))