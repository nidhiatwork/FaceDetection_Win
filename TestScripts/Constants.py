import os, sys, platform
from sikuli import *

AppPath_PRE = "C:\\Users\\nbhushan\\Downloads\\PremiereElements\\PremiereElementsEditor.exe"
AAPath = "C:\\Users\\nbhushan\\Downloads\\PremiereElements\\Elements Auto Creations 2019.exe"

userdir = os.path.expanduser('~')
userdir.replace("\\", "\\\\")

RootFolder = userdir + "\\Desktop\\FD_Automation"
BaselineFolder = RootFolder + "\\BaselineImages\\"
OutputFolder = RootFolder + "\\Output\\"
Sikuli_Path = userdir + "\\Downloads"
ScreenshotsFolder = RootFolder + "\\Output\\Screenshots"
FD_Test_Execution_Data = RootFolder + "\\TestData\\FD_Test_Execution_Data.xls"
BatFilesFolder = RootFolder + "\\BatFiles\\"
CollectionFolder = RootFolder + "\\Collection\\"
Technology = "Mona"