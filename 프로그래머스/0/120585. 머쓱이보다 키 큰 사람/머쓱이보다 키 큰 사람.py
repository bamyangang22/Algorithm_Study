def solution(array, height):
    taller_count = 0
    for h in array:
        if h > height:
            taller_count += 1
    
    return taller_count