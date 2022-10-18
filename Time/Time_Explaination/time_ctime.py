import time

x = time.time()   # current time in seconds since start of UNIX Epoch
y = time.ctime(2147483647) # x converted to human readable time format

# print(x)       
time.sleep(1)  # pauses execution of program for x seconds (1)
print(y)        