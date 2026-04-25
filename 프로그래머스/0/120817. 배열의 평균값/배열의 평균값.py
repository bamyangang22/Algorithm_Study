def solution(numbers):
    sum = 0
    avg = 0
    for n in numbers:
        sum += n
    avg = sum / len(numbers)
    return avg