def solution(money):
    buy_count = money // 5500
    change = money % 5500
    
    return [buy_count, change]
