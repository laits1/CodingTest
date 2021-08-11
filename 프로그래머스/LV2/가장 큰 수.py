# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    answer = ''
    mok = []
    for i in range(len(numbers)) :
        if (numbers[i] / 10 < 1) :
            print(numbers[i])
        else :
            print(numbers[i] / 10)
    return answer

numbers = [3, 30, 34, 5, 9]    # 6210

solution(numbers)