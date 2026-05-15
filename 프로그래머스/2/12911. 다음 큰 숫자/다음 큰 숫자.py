def solution(n):
    answer = 0
    count_1 = bin(n).count("1")
    print(count_1)
    next_big_num = -1
    while(True):
        n += 1
        if(bin(n).count("1") == count_1):
            next_big_num = n
            break
        
    return next_big_num
