# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = 0
    sum = 0
    for i in range(count) :
        sum = sum + (i+1) * price
        
    if (money < sum) :
        answer = sum - money

    return answer


print(solution(3,20,4))