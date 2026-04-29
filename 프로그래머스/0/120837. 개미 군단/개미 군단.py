def solution(hp):
    answer = 0
    general_geme = hp // 5
    soldier_geme = hp % 5 // 3
    worker_geme = (hp % 5) % 3
    answer = general_geme + soldier_geme + worker_geme
    return answer