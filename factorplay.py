# 11 Mar 13
# A way to waste time in boring lessons. I type a random number in my
# calculator, use it to find the highest prime factor. Then I add 1 to the
# prime and find the highest prime factor of that. I do that until I get a
# power of 2.
#
# I'm trying to see what are the numbers under 10^10 which have the highest
# number of steps before getting to a power of 2.

import screen
import time

def primality(num):
    for x in range(int(num**0.5) + 1):
        if x > 1 and num % x == 0: return False
    return True

def highest_prim_fact(num, count=0):
    # print(num)
    # Checking if num is a power of 2
    n = 2
    while True:
        if n == num: return count
        if n > num: break
        else: n *= 2

    # Finds highest prime factor and calls recursive function
    for cand in range(int(num**0.5) + 1):
        if cand > 0 and num % cand == 0:
            if primality(num/cand):
                #print(num/cand)
                count = highest_prim_fact((num/cand) + 1, count + 1)

    return count

def print_to_lcd(line1, line2):
    # Used for my Raspberry Pi LCD screen
    screen.gotoLine(0)
    screen.sendStr(line1)
    screen.gotoLine(1)
    screen.sendStr(line2)

# File to save output in case python is killed
a = open('output.txt', 'w')

screen.initScr()

maximum = 0

current_time = ""
max_string = ""
for num in range(10**10):
    # Finds current time once in a while
    if num % 100 == 99:
        current_time = time.asctime()[11:19]
        print_to_lcd(current_time, max_string)

    if num > 2: count = highest_prim_fact(num)
    else: count = 0
    if count >= maximum:
        maximum = count
        max_string = "{0}, {1}".format(count, num)
        a.write(max_string+"\n")
        print_to_lcd(current_time, max_string)
