import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

current_time = time.strftime('%H:%M:%S')
print(current_time)
print("Enter the time ____________")
hours=input("hour: ")
min=input("minutes: ")
sec=input("seconds: ")
if int(hours)<10:
    hours="0"+hours
if int(min)<10:
    min="0"+min
if int(sec)<10:
    sec="0"+sec
target_time=f"{hours}:{min}:{sec}"
# target_time = "08:17:29"
print("Waiting for", target_time)

while True:
    current_time = time.strftime('%H:%M:%S')
    print(current_time)
    if current_time >= target_time:
        toaster.show_toast("Time Alert", "It's now {}".format(current_time), duration=10)
        break