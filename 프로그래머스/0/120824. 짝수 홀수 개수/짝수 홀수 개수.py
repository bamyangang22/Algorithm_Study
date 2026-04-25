def solution(num_list):
    odd_count = 0;
    even_count = 0;
    
    for n in num_list:
        if(n % 2 == 0):
            even_count += 1
        else:
            odd_count += 1
    answer = [even_count,odd_count]    
    return answer