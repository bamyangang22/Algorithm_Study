# 1. 문제 이해하기
# input -> 전화번호 str의 배열
# output -> 접두어인 경우 false 없으면 true
# 한 문자열이 다른 문자열 안에 포함되어 있는지 확인하는 문제.
# input size = phone_book 배열의 길이 = 10^6 즉, O(n)의 시간복잡도를 가져야 함 O(nlogn)은 애매

# 근데 O(n)인 솔루션을 어케 내지.. 일단 완전 탐색으로 브루트 포스 방식으로 접근
# 2. 접근 방법
# 첫번째 문장 꺼내서 이후 모든 문장에 속하는 지 확인

# 3. 문제 구현 계획
# for문 맨 앞 str 이후 원소들이랑 비교 -> 기본적으로 이중 for문..
# 그리고 각 문자열마다 속하는지 확인 for문: 문자열 길이만큼
# 이렇게 구현하면 아마 O(n^2)의 시간복잡도를 가지게 됨.

def solution(phone_book):
    hash_table = {}
    # 해시 테이블로 초기화
    for n in phone_book:
        hash_table[n] = 1
    # 해당 원소에 해당하는 접두어가 있는지 확인
    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num
            if arr in hash_table and arr != nums:
                return False
    return True