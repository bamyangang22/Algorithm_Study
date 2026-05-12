def solution(s):
    answer = True
    cnt = 0
    
    for ch in s:
        if(ch == "("):
            cnt += 1
        elif(ch == ")"):
            cnt -= 1
        if(cnt < 0):
            return False
    if(cnt == 0):
        return True
    else:
        return False