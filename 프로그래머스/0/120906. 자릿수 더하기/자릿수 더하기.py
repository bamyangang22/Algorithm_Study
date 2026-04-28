def solution(n):
    answer = 0
    line = str(n)
    for ch in line:
        answer += int(ch)
    return answer