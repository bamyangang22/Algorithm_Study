def solution(n):
    answer = []
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            answer.append(i)
    rev_fac = sorted(answer, reverse = True)
    for num in rev_fac:
        if(num**2 == n):
            continue
        temp = n / num
        answer.append(temp)
    return answer