# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'] # 1월 1일 금요일부터 시작
    total = sum(month[0:a]) + b - 1 # 1을 빼야 나머지가 0일 때 금요일
    return day[total % 7]

a, b = map(int, input().strip().split(' '))
print(f"{solution(a,b)}")   # 5월 24일 TUE