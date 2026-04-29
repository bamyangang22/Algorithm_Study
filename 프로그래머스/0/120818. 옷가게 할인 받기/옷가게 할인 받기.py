def solution(price):
    answer = 0
    if (10 <= price < 100000):
        return price
    elif (100000 <= price < 300000):
        return int(price*0.95)
    elif (300000 <= price < 500000):
        return int(price*0.9)
    elif (price >= 500000):
        return int(price*0.8)