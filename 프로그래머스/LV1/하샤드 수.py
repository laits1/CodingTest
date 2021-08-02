# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    sum = 0
    nlist = [int(i) for i in str(x)] 
    for i in nlist :
        sum += i
    
    if (x / sum != 0) :
        answer = False
        return answer
    else :
        pass
    return answer

solution(10)