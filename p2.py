n = int( input("enter number of processes : ") )

processes = [ ]


for i in range(n):
    print(f"\nProcess {i+1}")
    p = []
    p.append( i+1 )
    p.append( int( input("Enter Arrival Time : ") ) )
    p.append( int( input("Enter Burst Time : ") ) )
    processes.append(p)

processes.sort(key= lambda x:x[1])

prev = 0
for p in processes:
    start = max(prev, p[1])
    p.append(start)
    p.append(start + p[2])
    prev = p[4]

print()

for p in processes:
    print(f'|   P{p[0]:<2}   ',end="")
print("|")

for p in processes:
    print(f'{p[3]:<3}       ',end="")
print(processes[-1][4])

total_wait = 0
total_turnaround = 0

print(f'\nProcess   |Arrival Time   |Burst Time   |Turnaround Time  |Waiting Time  ')
for p in processes:
    print(f'P{p[0]:<9}|{p[1]:<15}|{p[2]:<13}|{p[4]-p[1]:<17}|{p[4]-p[1]-p[2]}')
    total_wait += p[4]-p[1]-p[2]
    total_turnaround += p[4]-p[1]

print(f"\nAverage Waiting Time {total_wait/n}")
print(f"Average TurnAround Time {total_turnaround/n}")