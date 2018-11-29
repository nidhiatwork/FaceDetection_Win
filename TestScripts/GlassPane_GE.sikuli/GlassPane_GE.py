import utils
reload(utils)
from utils import *
import os
import sys
import unittest
import shutil
import datetime

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):
        close_AA_PRE_And_Launch_AA_PRE()

    def test_UI_GlassPane_GE(self):
        wait(1)
        os.chdir(Constants.CollectionFolder)
        setAutoWaitTimeout(60)
        l = os.listdir(Constants.CollectionFolder)
        l.sort()
        i=1
        for filename in l:
            if filename.find(".")==0:
                continue
            now = datetime.datetime.now()
            postfix = str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second)
            if Constants.Mode=="Image":

                newfilename = "Image#" + str(i) + "_"+ postfix + filename[filename.find("."):]
            else:
                newfilename = "Video#" + str(i) + "_"+ postfix + filename[filename.find("."):]

            print "Filename changed from " + filename + " to " + newfilename
            shutil.copy(Constants.CollectionFolder+filename,Constants.CollectionFolder+newfilename)
            os.remove(Constants.CollectionFolder+filename)
            clickElement("AddMedia.png")
            clickElement("FilesAndFolders.png")
            findElement("TextBox_ImportMediaPath.png")
            clickElement("TextBox_ImportMediaPath.png")
            typeKeys(Constants.CollectionFolder+newfilename)
            type(Key.ENTER)
            wait(3)
            launchAA()
            clickElement("ToolsIcon.png")
            if Constants.Mode=="Image":
                clickElement("Pan_and_Zoom.png")
                wait(5)
                findElement("Done.png")
                os.system("python " + Constants.BatFilesFolder + "TakeScreenshot.py " + newfilename + " " + Constants.Technology)
                clickElement("Done.png")
            else:
                clickElement("SmartTrim.png")
                clickElement("ShowPresets.png")
                clickElement("PeoplePreset.png")
                wait(2)
                setAutoWaitTimeout(900)
                findElement(Pattern("HidePresets.png").similar(0.90))
                
                os.system("python " + Constants.BatFilesFolder + "TakeScreenshot.py " + newfilename + " " + Constants.Technology)                
                clickElement(Pattern("CloseButton.png").similar(0.90))
                findElement("No.png")
                clickElement("No.png")
                setAutoWaitTimeout(60)
            findElement("AddMedia.png")
            wait(3)
            type("N", Key.CTRL)
            findElement("No.png")
            clickElement("No.png")
            wait(2)
            findElement("Cancel.png")
            clickElement("Cancel.png")
         
            print "Completed screenshot taking process for file: " + newfilename
            i = i+1
            wait(2)
    def tearDown(self):
       closePRE()