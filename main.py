from win10toast import ToastNotifier

filename = input("Which file to read? ")

# Open file
try:
    file = open(f'./Schedule/{filename}')
except:
    print("Error: Failure to open file")
    exit()

# Read file
firstLine = file.readline()
print(firstLine)

lines = []
for line in file:
    words = line.split(', ')
    lines.append(words)

print(lines)
# Send notification
# toaster = ToastNotifier()
# toaster.show_toast(title="Scheduler", msg="Sample Notification", duration=None)