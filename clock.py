import screen
import time

screen.initScr()
while True:
    screen.sendStr(time.asctime())
    time.sleep(1)
