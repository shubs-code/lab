def SCAN(arr, head, direction):
    arr.sort()
    left = [i for i in arr if i < head]
    right = [i for i in arr if i > head]
    left.reverse()
    
    total_distance = 0
    sequence = []
    
    if direction == 'left':
        for i in left + right[::-1]:
            total_distance += abs(head - i)
            sequence.append(i)
    elif direction == 'right':
        for i in right + left[::-1]:
            total_distance += abs(head - i)
            sequence.append(i)
    
    return total_distance, sequence

def C_SCAN(arr, head, direction):
    arr.sort()
    left = [i for i in arr if i < head]
    right = [i for i in arr if i > head]
    
    total_distance = 0
    sequence = []
    
    if direction == 'right':
        for i in right:
            total_distance += abs(head - i)
            sequence.append(i)
        total_distance += abs(head - max(arr))
        head = max(arr)
        for i in left:
            total_distance += abs(head - i)
            sequence.append(i)
    elif direction == 'left':
        for i in left:
            total_distance += abs(head - i)
            sequence.append(i)
        total_distance += abs(head - 0)
        head = 0
        for i in right:
            total_distance += abs(head - i)
            sequence.append(i)
    
    return total_distance, sequence

request_queue = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50
direction = 'right'

distance, sequence = SCAN(request_queue, head, direction)
print("SCAN Total Seek Distance:", distance)
print("SCAN Service Sequence:", sequence)

distance, sequence = C_SCAN(request_queue, head, direction)
print("C-SCAN Total Seek Distance:", distance)
print("C-SCAN Service Sequence:", sequence)
