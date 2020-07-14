from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from random import randint

print "get device"
device = MonkeyRunner.waitForConnection()
package = 'cn.com.bjx.bjxtalents'
activity = 'cn.com.bjx.bjxtalents.activity.MainActivity'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)

#use commands like device.touch and device.drag to simulate a navigation and open my activity

#with your activity opened start your monkey test
print "start monkey test"
for i in range(1, 10000):  device.touch(randint(0, 1080), randint(75, 1700), 'DOWN_AND_UP')
device.drag(randint(0, 1080), randint(75, 1800),randint(100, 1000),10)

    #here i go emulate only simple touchs, but i can emulate swiper keyevents and more... :D


print "end monkey test"