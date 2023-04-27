import pyautogui
import time

# pyautogui.moveRel(0,50,duration = 2)
time.sleep(3)


#14 tabs to get to the textfield
for i in range(9):
    pyautogui.press('down')
    time.sleep(1)
    for i in range(13):
        pyautogui.press('tab')  
        print('tab')    
        pyautogui.press('down')
        print('down')
        time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write('Good')
    pyautogui.press('tab')
    pyautogui.press('tab')           

pyautogui.press('tab')

for i in range(5):
    pyautogui.press('down')
    time.sleep(1)
    for i in range(12):
        pyautogui.press('tab')  
        print('tab')    
        pyautogui.press('down')
        print('down')
        time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write('Good')
    pyautogui.press('tab')
    pyautogui.press('tab')           
