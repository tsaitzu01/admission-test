def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    n1 = numbers[0]
    n2 = find_max(numbers[1:])

    if n1 > n2:
        return n1
    else:
        return n2

def find_position(numbers, target):
    
    pos = 0
    for num in numbers:
        if (target == num) & (pos < len(numbers)): 
            return pos
        elif pos == len(numbers)-1:
            return -1
        else:
            pos += 1
    

print(find_max([1, 2, 4, 5]) )
print(find_max([5, 2, 7, 1, 6]) )

print(find_position([5, 2, 7, 1, 6], 5)) # should print 0 
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1