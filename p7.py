def FCFS(requests, initial_position):
    seek_count = 0
    current_position = initial_position

    for request in requests:
        seek_count += abs(current_position - request) 
        current_position = request

    return requests, seek_count

def SSTF(requests, initial_position):
    seek_count = 0
    current_position = initial_position
    seek_sequence = []
    remaining_requests = requests[:]

    while remaining_requests:
        distances = [abs(current_position - request) for request in remaining_requests]
        
        shortest_seek_time_index = distances.index(min(distances))
        nearest_request = remaining_requests.pop(shortest_seek_time_index)
        
        seek_count += abs(current_position - nearest_request)  
        seek_sequence.append(nearest_request)
        current_position = nearest_request

    return seek_sequence, seek_count

requests = [55, 58, 60, 98, 140, 180, 25, 40, 80, 120]
initial_position = 50

seek_sequence, total_seek_count = SSTF(requests, initial_position)
print("SSTF Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)


seek_sequence, total_seek_count = FCFS(requests, initial_position)
print("FCFS Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)
