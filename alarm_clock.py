from playsound3 import playsound
import time

def alarm(seconds):
    time_elapsed = 0
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{minutes_left:02d}:{seconds_left:02d}", end="\r")
    playsound("rooster_alarm.mp3")

def main():
    while True:
        time = input("Enter time in minutes: ")
        if time.isdigit():
            time = int(time) 
            break
        else:
            print("Please enter a valid number.")
    
    alarm(time * 60)
if __name__ == "__main__":
    main()