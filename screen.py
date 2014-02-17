import time
import RPi.GPIO as gpio

# Constants, corresponding to each GPIO pin connected
LCD_RS      = 7         # Register Select - if 0 -> sends commands, if 1 -> sends data
LCD_E       = 11        # Enable pin - toggles to write data
LCD_D4      = 12        # Data pins
LCD_D5      = 13
LCD_D6      = 15
LCD_D7      = 16
OUTPUT_PINS = (LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7)
DATA_PINS = (LCD_D4, LCD_D5, LCD_D6, LCD_D7)

LINE = (0x00, 0x40)

CLEARDISPLAY = 0x01
SETCURSOR = 0x80


# Lower level functions
def initScr():
    # Starts GPIO module
    gpio.setmode(gpio.BOARD)
    for line in OUTPUT_PINS:
        gpio.setup(line, gpio.OUT)

    # Initialises LCD and clears display
    sendByte(0x33)          # initialises
    sendByte(0x32)          # sets to 4-bit mode
    sendByte(0x28)          # 2-line, 5x7 matrix
    sendByte(0x0C)          # Turns cursor off, 0x0E enables
    sendByte(0x06)          # Shifts cursor right
    sendByte(CLEARDISPLAY)  # Removes stray characters


def pulseEnableLine():
    # Sends quick pulse to the Enable pin
    time.sleep(0.0005)
    gpio.output(LCD_E, 1)
    time.sleep(0.0005)
    gpio.output(LCD_E, 0)
    time.sleep(0.0005)


def sendNibble(data):
    # A nibble is 4 bits of data - the 16x2 is in 4 bit mode
    # Two nibbles have to be sent to make the needed 8 bits
    gpio.output(LCD_D4, bool(data & 0x10))
    gpio.output(LCD_D5, bool(data & 0x20))
    gpio.output(LCD_D6, bool(data & 0x40))
    gpio.output(LCD_D7, bool(data & 0x80))


def sendByte(data, RS_mode=False):
    # Sends two nibbles
    gpio.output(LCD_RS, RS_mode)
    sendNibble(data)                # Sends the first 4 bits
    pulseEnableLine()

    data = (data & 0x0F) << 4       # Shifts the data 4 bits to the left
    sendNibble(data)
    pulseEnableLine()


# Higher level functions
def sendChar(ch):
    sendByte(ord(ch), True)


def sendStr(string):
    for ch in string: sendChar(ch)


def gotoLine(row):
    # Moves cursor to row
    if row == 0 or row == 1:
        sendByte(SETCURSOR + LINE[row], 0)


if __name__ == "__main__":
    initScr()
    for ch in "Hello World": sendChar(ch)
