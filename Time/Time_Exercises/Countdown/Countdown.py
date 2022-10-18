
import time         # import the time module
  
# define the countdown func.
def countdown(time_set):
    
    while time_set:
        mins, secs = divmod(time_set, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_set -= 1
      
    print('Time is Up!!!')
  
  
# input time in seconds
time_set = input("Enter the time in seconds: ")
  
# function call
countdown(int(time_set))