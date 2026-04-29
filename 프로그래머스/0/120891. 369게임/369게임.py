def solution(order):
    answer = 0
    k = str(order)
    for n in k:
        if (n == "3" or n == "6" or n == "9"):
            answer += 1
    
    return answer