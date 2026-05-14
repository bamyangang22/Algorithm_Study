def solution(numbers, target):
    cnt = 0
    def dfs(idx, total):
        nonlocal cnt
        # 최종합 확인 
        if(idx == len(numbers)):    
            if(target == total):
                cnt += 1
                return 0
        else:
            dfs(idx + 1, total + numbers[idx])
            dfs(idx + 1, total - numbers[idx])
        
    dfs(0, 0)
    return cnt

