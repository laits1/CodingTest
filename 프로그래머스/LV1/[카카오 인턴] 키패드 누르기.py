# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    now_L, now_R = '*', '#'
    keypad = {  1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
              '*':(3,0), 0:(3,1), '#':(3,2)
    }
    left, right = set([1,4,7]), set([3,6,9])
    
    for i in range(len(numbers)) :
        if(numbers[i] in left) :
            answer += "L"
            now_L = numbers[i]
            # print("현재 키패드 L",keypad[now_L], now_L)
        elif (numbers[i] in right):
            answer += "R"
            now_R= numbers[i]
            # print("현재 키패드 R",keypad[now_R], now_R)
        
        else :
            # 왼쪽 거리
            distance_L = abs(keypad[numbers[i]][0] - keypad[now_L][0]) + abs(keypad[numbers[i]][1] - keypad[now_L][1])
            # 오른쪽 거리
            distance_R = abs(keypad[numbers[i]][0] - keypad[now_R][0]) + abs(keypad[numbers[i]][1] - keypad[now_R][1])
           
            if (distance_L == distance_R) :
                if (hand == "right") :
                   answer += "R"
                   now_R = numbers[i]
                else :
                    answer += "L"
                    now_L = numbers[i]
            elif (distance_L < distance_R) :
                answer += "L"
                now_L = numbers[i]
            else :
                answer += "R"
                now_R = numbers[i]
    print(answer)
    return answer

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")      # LLR LLR LLR L
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")	   # LRL LLR LLR RL