def solution(str1, str2):
    hash = {}
    #str1에 존재하는 알파벳 중복 제거하여 value값 0으로 초기화한 상태로 해시 생성
    for ch in str1:
        hash[ch] = 0
   
    for ch in str2:
        if ch in hash:
            hash[ch] += 1
    
    max_val = 0
    for count in hash.values():
        if count > max_val:
            max_val = count
    return max_val

T = int(input())
for test_case in range(1, T + 1):
    str1 = input().strip()
    str2 = input().strip()

    result = solution(str1, str2)
    print(f"#{test_case} {result}")


