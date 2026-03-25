# 해당 풀이 예상 시간 복잡도 O(n), n = nums 길이(n^4)
def solution(nums):
    
    # 1. 타입 중복 제거 O(n)
    type_set = set(nums)
    # 2. 타입 종류 확인 O(1)
    type_count = len(type_set)
    # 3. 최대 선택 갯수 확인 O(1)
    # 만약 nums 길이가 짝수가 아닌 경우 /2했을 때 어떻게 처리하는지 디렉션이 있을 경우 주의!
    max_pick =int(len(nums)/2)
    
    # 4. 가장 많은 종류 선택 로직 O(1)
    return min(type_count, max_pick)
    # if type_count >= max_pick:
    #     return max_pick
    # else:
    #     return type_count