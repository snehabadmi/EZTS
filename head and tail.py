def coin(s):
    score = 0
    consecutive_heads = 0
    
    for char in s:
        if char == 'H':
            score += 2
            consecutive_heads += 1
            if consecutive_heads == 3:
                break
        else:
            score -= 1
            consecutive_heads = 0

    return score
s = "TTTHH"
print(coin(s))  
