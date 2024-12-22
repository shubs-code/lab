n = int(input("Enter number of processes: "))

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
completed = 0
total_wait = 0
total_turnaround = 0
gantt_chart = []

while completed < n:
    current_process = None
    for p in processes:
        if p[1] <= time and p[3] > 0:  
            if current_process is None or p[3] < current_process[3]:
                current_process = p

    if current_process is None:  
        time += 1
        continue

    gantt_chart.append(current_process[0])
    current_process[3] -= 1
    time += 1

    if current_process[3] == 0:
        completed += 1
        completion_time = time
        turnaround_time = completion_time - current_process[1]
        waiting_time = turnaround_time - current_process[2]

        current_process.append(completion_time)  
        current_process.append(turnaround_time)  
        current_process.append(waiting_time)  

        total_wait += waiting_time
        total_turnaround += turnaround_time

print("\nGantt Chart:")
for p in gantt_chart:
    print(f'| P{p} ', end="")
print("|")

print(f"\nProcess   |Arrival Time   |Burst Time   |Turnaround Time  |Waiting Time  ")
for p in processes:
    print(f'P{p[0]:<9}|{p[1]:<15}|{p[2]:<13}|{p[5]:<17}|{p[6]}')

print(f"\nAverage Waiting Time {total_wait / n}")
print(f"Average Turnaround Time {total_turnaround / n}")
