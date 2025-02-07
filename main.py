from alarm import Alarm
from clock import Clock 

def main():
    hour = int(input("Set alarm hour (24-hour format): "))
    minute = int(input("Set alarm minute: "))
    
    alarm = Alarm(hour, minute)
    
    clock = Clock(alarm)
    
    print(f"Your alarm is set for {hour:02d}:{minute:02d}.")
    
    clock.check_alarm()
    clock.play_alarm()

if __name__ == "__main__":
    main()

