def solution(my_string, n):
    answer = ""
    for ch in my_string:
        answer = answer + ch * n
    return answer