from tkinter import *
import tkinter.font as tkfont
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# hardwares
red = LED(14)
blue = LED(4)
green = LED(15)

# GUI Definitions
win = Tk()
win.title("LED 3 way systems")
myFont = tkfont.Font(family = 'Helvetica', size = 12, weight = "bold")

# Functions
def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"] = "TURN RED ON"
    else:
        red.on()
        blue.off()
        green.off()
        redButton["text"] = "TURN RED OFF"
        blueButton["text"] = "TURN BLUE ON"
        greenButton["text"] = "TURN GREEN ON"

def blueToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "TURN BLUE ON"
    else:
        blue.on()
        red.off()
        green.off()
        blueButton["text"] = "TURN BLUE OFF"
        redButton["text"] = "TURN RED ON"
        greenButton["text"] = "TURN GREEN ON"

def greenToggle():
    if green.is_lit:
        green.off()
        greenButton["text"] = "TURN GREEN ON"
    else:
        green.on()
        red.off()
        blue.off()
        greenButton["text"] = "TURN GREEN OFF"
        blueButton["text"] = "TURN BLUE ON"
        redButton["text"] = "TURN RED ON"

def exitConsole():
    GPIO.cleanup()
    win.destroy()

### Widgets

#Red LED light trigger and layout
redButton= Button(win, text = 'TURN RED ON', font = myFont, command = redToggle, bg = 'red', height = 1, width = 26)
redButton.grid(row=0,column=1)

#Blue LED light trigger and layout
blueButton = Button(win, text = 'TURN BLUE ON', font = myFont, command = blueToggle , bg = 'blue', height = 1, width = 26)
blueButton.grid(row=1,column=1)

#Green LED light trigger and layout
greenButton = Button(win, text = 'TURN GREEN ON', font = myFont, command = greenToggle, bg = 'green', height = 1, width = 26)
greenButton.grid(row=2,column=1)

#Exit button to safely close the sytem and layout
exitButton = Button(win, text = 'EXIT', font = myFont, command = exitConsole, bg = 'white', height = 1, width = 26)
exitButton.grid(row=3,column=1)

win.protocol("WM_DELETE_WINDOW", exitConsole) #close window
             
win.mainloop()
