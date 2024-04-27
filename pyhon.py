import time  
print(time.strftime("%Y-%m-%d %I:%M:%S %p",time.localtime()))
x = time.localtime()
if 4 < x.tm_hour  < 12 : 
    print("Good morning.Sir!")
elif 12 < x.tm_hour < 18 :
    print("Good afternoon.Sir!")
elif 18 < x.tm_hour < 21 :
    print("Good evening.Sir!")
else :
    print("It's night.Sir!")