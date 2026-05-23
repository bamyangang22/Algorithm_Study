def solution(people, limit):
    left = 0
    right = len(people) - 1
    cnt = 0
    people.sort()
    while left <= right:
        if(people[left] + people[right] <= limit):
            left += 1
            right -= 1
            cnt += 1
        else:
            right -= 1
            cnt += 1
    return cnt

# def solution(people, limit):
#     boat_cnt = 0
#     temp_weight_sum = 0
#     temp_people_cnt = 0
#     people.sort()
#     # 정렬된 people 배열을 탐색하면서 필요한 보트 수 계산.
#     for i in range(len(people)):
#         if(temp_weight_sum + people[i] <= limit and temp_people_cnt != 2):
#             temp_weight_sum += people[i]
#             temp_people_cnt += 1
#         else:
#             temp_weight_sum = people[i]
#             temp_people_cnt = 1
#             boat_cnt += 1
#     # 마지막 인덱스까지 탐색 후 보트에 사람이 남아있는 경우 +1.
#     if(temp_weight_sum != 0):
#         boat_cnt +=1
        
#     return boat_cnt

# cnt = 0
#     left = 0
#     right = len(people) - 1
#     people.sort()
#     while left <= right:
#         if(people[left] + people[right] <= limit):
#             cnt += 1
#             left += 1
#             right -=1
#         elif(people[left] + people[right] > limit):
#             cnt += 1
#             right -=1
#     return cnt