def solution(n, k):
    answer = 0
    discount = n // 10
    answer = 12000*n + 2000*(k - discount) 
    return answer