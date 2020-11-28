# Libraries
import pyautogui as pag
import time
import os
import subprocess

def moveToCenter():
    screenWidth, screenHeight = pag.size()
    pag.moveTo(screenWidth / 2, screenHeight / 2)
    time.sleep(2)
    pag.click(button = 'right')
    pag.moveTo(screenWidth/2, 500)
    
def moveEverywhere(x,y):
    pag.moveTo(x,y)
    pag.click(button = 'right')


def test():
    os.startfile("notepad.exe")
    pag.moveTo(900,400)
    pag.click()
    time.sleep(1)
    for i in range(10):
        pag.typewrite('You have been hacked \n')
        
def test2():
    f = open('test.docx', 'w')
    f.close()
    os.system("start test.docx")
    pag.moveTo(800,250)
    pag.click()
    time.sleep(1)
    for i in range(1):
        pag.typewrite('You have been hacked \n')    
        
def test3():
    subprocess.Popen(["C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE"])
        
def test4():
    screenWidth, screenHeight = pag.size()
    for i in range(1, screenWidth, 10):
        pag.moveTo(i,screenHeight/2)
        time.sleep(0.001)



# Main
if __name__ == '__main__':
    test4()

    
