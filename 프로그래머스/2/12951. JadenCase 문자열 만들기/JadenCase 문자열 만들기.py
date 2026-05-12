def solution(s):
    answer = ''
    cap_s_list = []
    
    s_list = s.split(" ")
    print(s_list)
    for word in s_list:
        cap_s_list.append(word.capitalize())
    
    answer = " ".join(cap_s_list)
    print(answer)
    
    
    return answer