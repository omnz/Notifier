from win10toast import ToastNotifier
from datetime import date, datetime
# from time import sleep

filename = input("Which file to read? ")

# Open file
try:
    file = open(f'./Schedule/{filename}')
except:
    print("Error: Failure to open file")
    exit()

# Read file
first_line = file.readline()

lines = []
days = {'Sunday': [], 'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': []}
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for line in file:
    words = line.split(',')
    count = 1
    
    # Append each event and time to its corresponding day of the week
    for x in range(0, 7):
        if words[count] != '':
            days[list_of_days[x]].append(words[0])
            days[list_of_days[x]].append(words[count])

        count += 1

# Get current day of the week
today = (date.today().weekday() + 1) % 7

events = days[list_of_days[today]]

while events:
    str_time = events[0]
    event_time = datetime.strptime(str_time, '%I:%M %p')
    event_time = event_time.strftime("%H:%M:%S")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print(current_time)

    # Remove missed events
    if(event_time < current_time):
        print(f"Removed event: {events[1]}, {events[0]}")
        events.pop(0)
        events.pop(0)
    if(event_time == current_time):
        # Send notification
        toaster = ToastNotifier()
        toaster.show_toast(title="Scheduler", msg=f"{events[1]}", duration=1700)

        # # Remove completed events
        # events.pop(0)
        # events.pop(0)
        # sleep(1700)