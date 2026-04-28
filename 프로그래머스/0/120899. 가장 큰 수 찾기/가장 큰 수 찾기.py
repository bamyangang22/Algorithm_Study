def solution(array):
    answer = []
    max_val = max(array)
    answer.append(max_val)
    answer.append(array.index(max_val))
              
    return answer