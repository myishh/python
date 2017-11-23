def firstFunc():
	print('----%s----'%('This is the 1st func'))
	print('----%s----'%('It is a simple func'))

firstFunc()

import time
currentTime = time.time()
print('Current time : ', currentTime)
localtime = time.localtime(time.time())
print('Local time : ', localtime)
finalTime = time.asctime(time.localtime(time.time()))
print('Final time : ', finalTime)

import calendar
cal = calendar.month(2017, 12)
print('Calender of Dec 2017 :')
print(cal)


import random
a = random.uniform(1,5)
print('a =', a)
b = random.randint(10, 50)
print('b =', b)
c = random.randrange(0, 51, 2)
print('c =', c)
