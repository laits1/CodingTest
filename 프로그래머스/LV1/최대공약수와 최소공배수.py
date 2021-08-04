# https://programmers.co.kr/learn/courses/30/lessons/12940
# LCM : 최소 공배수
# GCD : 최대 공약수
# answer = [GCD, LCM]
def solution(n, m):
    answer = []
    GCD = 1
    for i in range(1,max(n,m)+1) :  # 1부터 큰수까지 반복
        if (n % i == 0 and m % i == 0) :
            GCD = i
    LCM = int(n / GCD * m) # 최소 공배수

    answer.append(GCD)
    answer.append(LCM)

    return answer


n = 24
m = 30 
 # 24 , 30 [6,120]
solution(n, m)

