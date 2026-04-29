def solution(my_string):
    answer = []
    for ch in my_string:
        if(ch.isdigit()):
            answer.append(int(ch))
    answer.sort()
            
    return answer