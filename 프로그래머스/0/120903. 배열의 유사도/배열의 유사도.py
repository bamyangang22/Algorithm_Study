def solution(s1, s2):
    answer = 0
    for ch1 in s1:
        for ch2 in s2:
            if ch1 == ch2:
                answer += 1
    
    return answer