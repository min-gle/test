from datetime import datetime
import time

now = datetime.now()
now_timestamp = time.mktime(now.timetuple()) 
print(now_timestamp)

ytd = 1657313569


result = now_timestamp - ytd
print(result)

#24시간 전

result /= (60*60)

print(result)

current_time = now.strftime("%H:%M:%S")
print(type(current_time))

print("Current Time =", current_time)