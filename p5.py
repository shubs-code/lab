n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    print(f"\nProcess {i+1}")
    p = []
    p.append(i + 1)  
    p.append(int(input("Enter Arrival Time: ")))  
    p.append(int(input("Enter Burst Time: ")))  
    p.append(int(input("Enter Priority (lower value indicates higher priority): ")))  
    processes.append(p)

processes.sort(key=lambda x: (x[3], x[1]))

prev = 0
for p in processes:
    start = max(prev, p[1])
    p.append(start)  
    p.append(start + p[2])  
    prev = p[5]

print()

for p in processes:
    print(f'|   P{p[0]:<2}   ', end="")
print("|")

for p in processes:
    print(f'{p[4]:<3}       ', end="")
print(processes[-1][5])

total_wait = 0
total_turnaround = 0

print(f'\nProcess   |Arrival Time   |Burst Time   |Priority   |Turnaround Time  |Waiting Time  ')
for p in processes:
    turnaround_time = p[5] - p[1]
    waiting_time = turnaround_time - p[2]
    print(f'P{p[0]:<9}|{p[1]:<15}|{p[2]:<13}|{p[3]:<11}|{turnaround_time:<17}|{waiting_time}')
    total_wait += waiting_time
    total_turnaround += turnaround_time

print(f"\nAverage Waiting Time {total_wait / n}")
print(f"Average Turnaround Time {total_turnaround / n}")
