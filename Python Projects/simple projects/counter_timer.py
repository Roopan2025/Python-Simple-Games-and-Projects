import time

# my_time = int(input("Enter time in seconds: "))

# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int((x / 60) % 60)
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time's up!")


# x = int(input("Enter time in seconds: "))
# while x >= 0:
#     seconds = x % 60
#     minutes = int((x / 60) % 60)
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     x -=  1
#     time.sleep(1)
# print("Time's up!")

x = int(input("Enter time in seconds: "))
while True:
    if x >= 0:
        seconds = x % 60
        minutes = int((x / 60) % 60)
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        x -= 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Time's up!")
        break






