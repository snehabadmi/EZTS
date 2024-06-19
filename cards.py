
def cards(array):
    last_seen = {}
    min_length = float('inf')
    
    for i in range(len(array)):
        if array[i] in last_seen:
            current_length = i - last_seen[array[i]] + 1
            min_length = min(min_length, current_length)
        last_seen[array[i]] = i
    return min_length if min_length != float('inf') else -1
array = [3, 4, 2, 3, 4, 7]
print(cards(array))  



