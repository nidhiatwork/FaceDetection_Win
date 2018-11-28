import pyautogui
import sys
name = str(sys.argv[1])
technology = str(sys.argv[2])
print "Nidhi screen data below:"
print name
print technology
if technology=="Mona":
    pyautogui.screenshot("C:\\Users\\nbhushan\\Desktop\\FD_Automation\\ScreenshotSamples\\Mona\\Screenshot_Mona_"+name)
else:
    pyautogui.screenshot("C:\\Users\\nbhushan\\Desktop\\FD_Automation\\ScreenshotSamples\\Cognitive\\Screenshot_Cognitive_"+name)