n = int( input("enter number of processes : ") )
processes = [ ]

for i in range(n):
    print(f"\nProcess {i+1}")
    p = []
    p.append( i+1 )
    p.append( int( input("Enter Arrival Time : ") ) )
    p.append( int( input("Enter Burst Time : ") ) )
    p.append(p[2])
    p.append( int( input("Enter Priority : ") ) )
    processes.append(p)

processes.sort(key= lambda x:x[1])

time = 0
compeleted = 0
queue = []
chart = []
while compeleted < n : 
    for p in processes:
        if(p[1]==time):
            queue.append(p)
    
    time+=1
    if not queue:
        continue
    
    queue.sort(key= lambda x:x[4])
    p = queue.pop(0)
    p[3]-= 1

    chart.append([p[0], time-1, time])

    if p[3]==0:
        p.append(time-p[1])
        p.append(p[5]-p[2])
        compeleted+=1
    else:
        queue.insert(0,p)


print("\nGantt Chart")

for p in chart:
    print(f'|   P{p[0]:<2} [{p[1]}-{p[2]}]  ',end="")
print("|")


total_wait = 0
total_turnaround = 0

print(f'\nProcess   |Arrival Time   |Burst Time   |Priority  |Turnaround Time  |Waiting Time  ')
for p in processes:
    print(f'P{p[0]:<9}|{p[1]:<15}|{p[2]:<13}|{p[4]:<10}|{p[5]:<17}|{p[6]}')
    total_wait += p[6]
    total_turnaround += p[5]

print(f"\nAverage Waiting Time {total_wait/n}")
print(f"Average TurnAround Time {total_turnaround/n}")