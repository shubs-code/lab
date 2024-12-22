n = int(input("Enter number of processes: "))
time_quantum = int(input("Enter Time Quantum: "))

processes = []

for i in range(n):
    print(f"\nProcess {i+1}")
    p = []
    p.append(i + 1)  
    p.append(int(input("Enter Arrival Time: ")))  
    p.append(int(input("Enter Burst Time: ")))  
    p.append(p[2])  
    processes.append(p)

processes.sort(key=lambda x: x[1]) 

time = 0
queue = []
gantt_chart = []
completed = 0
total_wait = 0
total_turnaround = 0
waiting_time = [0] * n
turnaround_time = [0] * n

while completed < n:
    for p in processes:
        if p not in queue and p[1] <= time and p[3] == p[2]:
            queue.append(p)

    if not queue:
        time += 1
        continue

    current_process = queue.pop(0)

    start_time = time
    execute_time = min(time_quantum, current_process[3])
    current_process[3] -= execute_time
    time += execute_time
    end_time = time

    gantt_chart.append((current_process[0], start_time, end_time))

    for p in processes:
        if p not in queue and p[1] <= time and p[3] == p[2]:
            queue.append(p)

    if current_process[3] > 0:
        queue.append(current_process)
    else:
        completed += 1
        completion_time = time
        turnaround_time[current_process[0] - 1] = completion_time - current_process[1]
        waiting_time[current_process[0] - 1] = turnaround_time[current_process[0] - 1] - current_process[2]
        total_turnaround += turnaround_time[current_process[0] - 1]
        total_wait += waiting_time[current_process[0] - 1]

print("\nGantt Chart:")
for p, start, end in gantt_chart:
    print(f'| P{p} [{start}-{end}] ', end="")
print("|")

print("\nProcess   |Arrival Time   |Burst Time   |Turnaround Time  |Waiting Time  ")
for p in processes:
    pid = p[0]
    print(f'P{pid:<9}|{p[1]:<15}|{p[2]:<13}|{turnaround_time[pid - 1]:<17}|{waiting_time[pid - 1]}')

print(f"\nAverage Waiting Time: {total_wait / n:.2f}")
print(f"Average Turnaround Time: {total_turnaround / n:.2f}")
