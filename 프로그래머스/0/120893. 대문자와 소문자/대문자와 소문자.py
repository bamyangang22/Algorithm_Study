def solution(my_string):
    answer = ''
    for ch in my_string:
        if (ch.islower()):
            answer += ch.upper()
        elif(ch.isupper()):
            answer += ch.lower() 
    return answer