# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n) :
    n = list(str(n))
    n.sort(reverse=True)

    return int(''.join(n))

n = 118372 
print(solution(n))
