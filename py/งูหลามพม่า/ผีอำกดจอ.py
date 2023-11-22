<<<<<<< HEAD
import pyautogui
import time

text = input("Enter the text you want to type: ")
count = int(input("Enter the number of times you want to type the text: "))

time.sleep(5)  # Delay for 5 seconds

for i in range(count):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    time.sleep(0)  # Delay for 0 seconds between each typing
=======
import pyautogui
import time

text = input("Enter the text you want to type: ")
count = int(input("Enter the number of times you want to type the text: "))

time.sleep(5)  # Delay for 5 seconds

for i in range(count):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    time.sleep(0)  # Delay for 0 seconds between each typing
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
