# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)) :
        if i < (len(phone_number) - 4) :
            answer += "*"
            # print("*", end="")
        else :
            answer += phone_number[i] 
            # print(answer[i], end="")
    print(answer)
    return answer

# phone_number = input()
solution('027778888')
