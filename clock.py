import screen
import time

screen.initScr()
while True:
    screen.sendStr(time.asctime()[11:19])
    screen.gotoLine(0)
    time.sleep(1)
