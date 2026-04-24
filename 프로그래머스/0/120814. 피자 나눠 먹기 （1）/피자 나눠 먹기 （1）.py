def solution(n):
    is_bonus_pizza_needed = 0
    whole_pizza_count = n//7
    if n % 7 != 0:    
        is_bonus_pizza_needed = 1;
    total_pizza = whole_pizza_count + is_bonus_pizza_needed
    return total_pizza