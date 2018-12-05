import os,sys
import time

Mode = "Image"

os.system("C:\\Users\\nbhushan\\Downloads\\runsikulix.cmd -r C:\\Users\\nbhushan\\Desktop\\FD_Automation\\TestScripts\\TestDriver.sikuli --args TestPRE_FaceDetection.test_UI_FaceDetection" + " Cognitive " + Mode)


print "Workflow completed with Cognitive technology for " + Mode

time.sleep(5)

os.system("C:\\Users\\nbhushan\\Downloads\\runsikulix.cmd -r C:\\Users\\nbhushan\\Desktop\\FD_Automation\\TestScripts\\TestDriver.sikuli --args TestPRE_FaceDetection.test_UI_FaceDetection" + " Mona " + Mode)

print "Workflow completed with Mona technology for " + Mode