import keyboard
import time
import random
programSelection = str(input("Which program would you like to run?\nPlease enter the number of the program:\n1: Repeat 'Pi Kapp' a given number of times (not unique)\n2: Print a list of numbers, with all numbers being unique\n"))
numberOfRepetitions = int(input("How many times would you like to send a message? (Pick a number)\n"))
print("Program starting in in 5...")
time.sleep(1)
print("4..")
time.sleep(1)
print("3...")
time.sleep(1)
print("2..")
time.sleep(1)
print("1..")
time.sleep(1)
print("Starting program!")

if "1" in programSelection:
    for i in range(numberOfRepetitions):
       keyboard.write("Pi Kapp")
       keyboard.press("enter")
       keyboard.release("enter")
       time.sleep(0.5)
elif "2" in programSelection:
    for i in numberOfRepetitions:
        keyboard.write(i)
        keyboard.press("enter")
        keyboard.release("enter")
else:
    print("Error! Please make sure you enter in a proper program number and try again.")
print("Program finished running! You can close this window.")
