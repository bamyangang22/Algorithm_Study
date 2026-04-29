def solution(numbers):
    answer = 0
    l = len(numbers)
    numbers.sort()
    if (numbers[0]*numbers[1] > numbers[l-2]*numbers[l-1]):
        return numbers[0]*numbers[1]
    else:
        return numbers[l-2]*numbers[l-1]