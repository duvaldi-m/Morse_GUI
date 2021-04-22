import tkinter as tk
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#letter to select from with morse code mapping
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morseCode = ["*-", "-***", "-*-*", "-**","*","**-*", "--*", "****", "**", "*---","-*-", "*-**","--","-*", "---", "*--*", "--*-", "*-*", "***", "-","**-", "***-", "*--", "-**-","-*--", "--**"]

## hardware
led_blue = LED(17)


## GUI DEFFINITIONS ##
win = tk.Tk()
nameVar = tk.StringVar()


win.title("Morse code blinker")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

### EVENT FUNCTIONS ###

#main blinking and error handling fuction
#if name valid, map letters in name to morse code and blink

def submit():
	led_blue.off()
	errorMessage["text"]=""
	name = nameVar.get()
	name = name.lower()
	if len(name) > 12:
		errorMessage["text"]="Too long, 12 characters max"
		time.sleep(3)
		entry.delete(0,'end')
		
	else:
		for idx, char in enumerate(name):
			if char in letters:
				index =	letters.index(char)
				toBlink = morseCode[index]
				for item in toBlink:
					if item == '*':
						shortBlink()
					elif item == '-':
						longBlink()
			else:
				errorMessage["text"]="Only enter alpabetical characters"	

			nameVar.set("")
			entry.delete(0,'end')
	

def shortBlink():
	led_blue.on()
	time.sleep(0.3)
	led_blue.off()
	time.sleep(0.5)


def longBlink():
	led_blue.on()
	time.sleep(1)
	led_blue.off()
	time.sleep(0.5)

def close():
	GPIO.cleanup()
	win.destroy()

### WIDGETS ###

lable1 = tk.Label(win, text="Enter name to blink in morse code", bg = 'teal')
lable2 = tk.Label(win, text="Only enter alphabetical characters", bg = 'yellow')
entry = tk.Entry(win,textvariable = nameVar, bd =5)
submit_button=tk.Button(win,text = 'Submit', command = submit)
errorMessage = tk.Label(win, text="")

exit_button = tk.Button(win, text = 'close', 
font = myFont, command = close,bg = 'grey', 
height = 1, width = 6)

lable1.grid(row = 1, column = 20)
lable2.grid(row = 8, column = 20)
entry.grid(row = 16, column = 20)
submit_button.grid(row = 24, column = 20)
errorMessage.grid(row = 30, column = 20)

exit_button.grid(row = 300, column = 300)

win.protocol("WM DELETE WINDOW",close)
win.geometry("300x200+10+20")
win.mainloop()
