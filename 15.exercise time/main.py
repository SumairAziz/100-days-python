import time

timestamp = time.strftime('%H:%M:%S')

hours = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

if (hours == 0 and minutes > 0 and seconds > 0) or (hours >= 1 and hours < 5):
    print("Good after midnight")
elif hours >= 5 and hours < 9:
    print("Good morning")
elif hours >= 9 and hours < 14:
    print("Good noon")
elif hours >= 14 and hours < 18:
    print("Good afternoon")
elif hours >= 18 and hours < 20:
    print("Good evening")
elif hours >= 20 and hours < 23:
    print("Good night")
