# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    if (not 1<=n<=25) :
        return -1
    answer = ''
    tmp = []
    for i in s :
        if(ord(i) == 32) :
            tmp.append(ord(i))
        else :
            if (65<= ord(i) <=90) :
                if (ord(i) + n < 91) :
                    tmp.append(ord(i) + n)
                else :
                    tmp.append(ord(i) + n - 26)
            elif (97<= ord(i) <= 122) :
                if (ord(i) + n < 123) :
                    tmp.append(ord(i) + n)
                else :
                    tmp.append(ord(i) + n - 26)

            
    for i in range(len(tmp)) :
        answer += chr(tmp[i])
        
    print(answer)
    return answer

s = "a B z"
n = 4
solution(s, n)

    # for i in s :
    #     if(ord(i) != 32) :
    #         if((65<= ord(i) + n <= 90) or (97<= ord(i) + n <= 122)) :
    #             tmp.append(ord(i) + n)
    #         else : 
    #             tmp.append(ord(i) + n - 26)
    #     else :
    #         tmp.append(ord(i))