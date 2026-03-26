# input -> ["옷", "옷 종류"]의 배열
# output -> 서로 다른 조합의 수.
# size of n = 의상의 수 = 30

def solution(clothes):
    answer = 1
    hash = {}
    
    # 옷 종류와 갯수를 파악하기 위해 옷 종류=key, 갯수= value로 저장
    for cloth in clothes:
        hash[cloth[1]] = hash.get(cloth[1], 0) + 1
    
    # 경우의 수 계산;
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수는
    # (N+1)(M+1) 이때 아무것도 입지 않는 경우 1가지를 빼면 정답
    for type_count in hash.values():
        answer *= type_count + 1        
    return answer - 1