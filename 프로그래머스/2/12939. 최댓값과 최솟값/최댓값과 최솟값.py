def solution(s):
    answer = ''
    # num_list = s.split(" ")으로 두번째 예시 정렬 시 -1,-2,-3,-4 순서가 됨. 주의!
    num_list = [int(x) for x in s.split()]
    print(num_list)
    min_num = min(num_list)
    answer = str(min_num)+ " "
    
    max_num = max(num_list)
    answer += str(max_num)
    return answer