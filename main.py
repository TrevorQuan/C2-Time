import time
#Function time()
print("Seconds since epoch = " + str(time.time()))

countdown = 3
while(countdown >= 0):
  print(countdown)
  countdown -= 1
  time.sleep(1)
print("HAPPY NEW YEAR!")

startTime = time.time()
userName = input("Type your name: ")
endTime = time.time()
print("Elapse time: " + str(endTime-startTime))