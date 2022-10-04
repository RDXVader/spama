import pyautogui as p 
import time
Sleep = input("How Mutch You Want For Sleep : ") 
Num = 0
Range = input("How Mutch You Want For Massge : ") 
Massge = input("Massge : ")
time.sleep(int(Sleep))

for i in range(int(Range)):
    Num = Num + 1
    p.typewrite(Massge)
    p.press("enter")
    print("Sent" + str(Num))
