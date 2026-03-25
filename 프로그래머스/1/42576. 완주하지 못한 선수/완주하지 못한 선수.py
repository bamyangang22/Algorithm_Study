'''
1. 문제 이해하기
    1-1. input/output 확인
    -> 참여자, 완주자 배열이 주어짐 그리고 완주하지 못한 한 사람을 리턴
    1-2. input Size N 확인
    -> participant는 10^5 비교 대조를 해야하는데 O(NlogN) 알고리즘 설계
    1-3. 제약 조건 확인
    -> 이름 1~20자 사이의 문자열
    -> 참여자는 무조건 1명이상이라서 0인 케이스 고려X
    1-4. 예상할 수 있는 오류 파악
    
2. 접근 방법
    2-1. 직관적으로 생각하기
        - 완전탐색으로 시작
        - 문제 상황을 단순화하여 생각
        - 문제 상황을 극한화하여 생각
        완주자 명단을 해시테이블로 만들고 for in을 사용하여 완주자 명단에 없는 경우 출력.
    2-2. 자료구조와 알고리즘 활용
        - (1)에서 파악한 내용을 토대로 어떤 자료구조를 사용하는게             적합한지 결정
    2-3. 메모리 사용
        - 시간복잡도를 줄이기 위해 메모리 사용하는 방법
        - 대표적으로 해시테이블
3. 코드 설계
참여자를 해시에 담고 완주자 명단에서 이름을 꺼내 참여자와 비교하는 방식
참여자에 동명이인이 있을 수 있으니 해시화할 때 동명이인이 존재하면 value를 +1하는 방식으로 처리

'''

def solution(participant, completion):
    participant_hash = {}
    # 참여자 명단을 해시에 추가(이름: 인원수)
    for p in participant:
        participant_hash[p] = participant_hash.get(p, 0) + 1
    for c in completion:
        participant_hash[c] -= 1
    for name, count in participant_hash.items():
        if count != 0:
            return name
        
    