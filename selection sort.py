#Selection sort -> find minimum at put it at start
l = list(map(int, input("Enter the numbers: ").split()))
n = len(l)  # Get the length of the list
for j in range(n):
    pos = j
    min_val = l[j]
    for i in range(j, n):
        if l[i] < min_val:
            min_val = l[i]
            pos = i
    l[j], l[pos] = l[pos], l[j]  # Swap the elements

print("Sorted list:", l)