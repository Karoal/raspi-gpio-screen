import screen
import time

while True:
    screen.sendStr(time.asctime())
    time.sleep(1)
