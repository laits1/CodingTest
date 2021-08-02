# https://programmers.co.kr/learn/courses/30/lessons/12944


def solution(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)


arr = [1,2,3,4]
solution(arr)
