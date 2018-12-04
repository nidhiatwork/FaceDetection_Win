import pyautogui
import os,sys
import random
import shutil

d = "C:\\Users\\nbhushan\\Desktop\\TestData\\Images\\"
f= "C:\\Users\\nbhushan\\Desktop\\FD_Automation\\Stock\\FreshImgs\\"
os.chdir(d)
l = os.listdir(d)
i=1
for x in range(1000):
    index = random.randint(1,len(l))
    print l[index]
    shutil.copy(d+l[index],f+l[index])
