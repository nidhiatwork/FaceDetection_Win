import pyautogui
import sys
name = str(sys.argv[1])
technology = str(sys.argv[2])

if technology=="Mona":
    pyautogui.screenshot("C:\\Users\\nbhushan\\Desktop\\FD_Automation\\ScreenshotSamples\\Mona\\Screenshot_Mona_"+name[:name.find(".")] + ".jpg")
else:
    pyautogui.screenshot("C:\\Users\\nbhushan\\Desktop\\FD_Automation\\ScreenshotSamples\\Cognitive\\Screenshot_Cognitive_"+name[:name.find(".")] + ".jpg")