def solution(my_string):
    sum = 0
    digits = ["1","2","3","4","5","6","7","8","9"]
    for i in my_string:
        if i in digits:
            sum += int(i)
            
    return sum