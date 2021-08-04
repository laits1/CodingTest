# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    min_num = min(arr)
    
    # for i in range(len(arr)):
    arr.remove(min_num)
    if arr == [] :
        answer = [-1]
    else :
        answer = arr
    print(answer)
    return answer


arr = [1,2,3,4]

# arr.remove(min(arr))
# print(arr)
# 리스트.remove(제거할 요소 값)
solution(arr)