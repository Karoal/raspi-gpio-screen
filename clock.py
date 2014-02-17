import screen
import time

screen.initScr()
while True:
    screen.sendStr(time.asctime()[:16])
    time.sleep(1)
