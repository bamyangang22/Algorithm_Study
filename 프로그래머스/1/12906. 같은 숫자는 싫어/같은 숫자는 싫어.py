def solution(arr):
    answer = []
    top = -1
    
    for number  in arr:
        if top != number:
            answer.append(number)
            top = number
            
    return answer