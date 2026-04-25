def solution(my_string, letter):
    answer = ''
    str = my_string
    for ch in str:
        if ch == letter:
            continue
        else:
            answer += ch

    return answer