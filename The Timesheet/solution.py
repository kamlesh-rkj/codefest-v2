# Import required libraries
import datetime
from collections import defaultdict

# Define function to calculate time difference in hours
def get_time_diff(start_time, end_time):
    time_diff = end_time - start_time
    hours, remainder = divmod(time_diff.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

# Read input from file
with open('TT_large.txt', 'r') as f:
    T = int(f.readline().strip())
    timelogs = []
    for i in range(T):
        line = f.readline().strip().split()
        if len(line) < 4:
            continue
        emp_id = line[0]
        timestamp = datetime.datetime.strptime(line[1] + ' ' + line[2], '%Y-%m-%d %H:%M:%S')
        status = line[3]
        timelogs.append((emp_id, timestamp, status))


# Define variables for tracking hours per month per employee
hours_per_month = defaultdict(lambda: defaultdict(int))

# Loop through timelogs to calculate hours worked per month per employee
for log in sorted(timelogs, key=lambda x: (x[0], x[1])):
    emp_id, timestamp, status = log
    month = timestamp.strftime('%Y-%m')
    if status == 'clock-in':
        start_time = timestamp
        break_time = None
    elif status == 'break-start':
        break_time = timestamp
    elif status == 'break-stop':
        start_time = start_time + (timestamp - break_time)
        break_time = None
    elif status == 'clock-out':
        end_time = timestamp
        if end_time.time() > datetime.time(19, 30):
            end_time = datetime.datetime.combine(end_time.date(), datetime.time(19, 30))
        if break_time:
            start_time = start_time + (break_time - start_time) - datetime.timedelta(minutes=30)
            break_time = None
        hours, minutes, seconds = get_time_diff(start_time, end_time)
        hours_per_month[emp_id][month] += hours + (minutes / 60) + (seconds / 3600)

# Define variables for tracking best and worst employee for each month
best_employee = defaultdict(lambda: (None, 0))
worst_employee = defaultdict(lambda: (None, float('inf')))

# Loop through hours per month per employee to identify best and worst employee for each month
for emp_id in hours_per_month:
    for month in hours_per_month[emp_id]:
        hours = hours_per_month[emp_id][month]
        if hours > best_employee[month][1]:
            best_employee[month] = (emp_id, hours)
        if hours < worst_employee[month][1]:
            worst_employee[month] = (emp_id, hours)

# Define variables for tracking average working hours per month
avg_hours_per_month = defaultdict(float)

# Loop through hours per month per employee to calculate average working hours per month
for emp_id in hours_per_month:
    for month in hours_per_month[emp_id]:
        avg_hours_per_month[month] += hours_per_month[emp_id][month] / len(hours_per_month)

# Write output to file
with open('TT_large_output.txt', 'w') as f:
    for month in sorted(best_employee.keys()):
        best_emp, best_hours = best_employee[month]
        worst_emp, worst_hours = worst_employee[month]
        avg_hours = avg_hours_per_month[month]
        f.write(f'{month},{best_emp},{worst_emp},{best_hours:.2f},{worst_hours:.2f},{avg_hours:.2f}\n')
