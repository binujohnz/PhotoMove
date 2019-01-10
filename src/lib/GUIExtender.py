from lib.GUI import MainForm as Form1
from lib.GUI import diaOptions
from lib.GUI import diaLogs

from lib import Util
import wx
import os, time, datetime
import configparser
import threading
from shutil import copy2
from shutil import move


# This Class Extend's GUI Class. You can add all your Extender Class here.
class Options(diaOptions):
    def __init__(self, parent):
        diaOptions.__init__(self, parent)
        self.AppName = parent.AppName

        self.dpickImgDest.SetPath(parent.ImageRootDir)
        self.dpickVideos.SetPath(parent.VideoRootDir)
        self.dpickDup.SetPath(parent.GarbageRootDir)
        self.txtDirFormat.SetValue(parent.DestDirFormat)

        self.parent = parent

    def cancelOpt(self, event):
        self.Show(False)

    def updateOpt(self, event):
        idest = self.dpickImgDest.GetPath()
        vdest = self.dpickVideos.GetPath()
        ddest = self.dpickDup.GetPath()

        if (idest == ""):
            wx.MessageBox("Missing Destination Image Directory", self.AppName, wx.OK | wx.ICON_INFORMATION)
            return False
            
        if (vdest == ""):
            wx.MessageBox("Missing Destination Video Directory", self.AppName, wx.OK | wx.ICON_INFORMATION)
            return False

        self.parent.setExcludeDirList(self.txtExcDirs.GetValue())
        self.parent.DestDirFormat = self.txtDirFormat.GetValue()

        self.parent.setLabels(idest, vdest, ddest)
        self.Show(False)

class MainForm(Form1):
    def __init__( self ):
        Form1.__init__( self, None )
        self.AppName = "Photo Matcher"
        self.SourceDir = ""
        self.ImageRootDir = ""
        self.VideoRootDir = ""
        self.GarbageRootDir = ""
        self.ImageTypes = ['jpg','jpeg', 'bmp', 'png']
        self.VideoTypes = ['mpg','mpeg', 'mov', 'avi', 'mp4', '3gp']
        self.ExcludeDirList = ""
        self.t = None
        self.DestDirFormat = ""

        self.stop_threads = False
        self.logDig = diaLogs(self)

        self.configFile = os.path.join(os.path.expanduser('~'), '.photoMath.cfg') 
        self.config = configparser.ConfigParser()

        self.safeLoad()
        self.setLabels()

    def toggleStartButton(self, inp=True):
        # True - Enable Start and hide cancel
        if inp == True:
            self.butCopy.Enable(True)
            self.butCancel.Enable(False)
        else:
            self.butCopy.Enable(False)
            self.butCancel.Enable(True)
        return True

    def setExcludeDirList(self, str):
        self.ExcludeDirList = str

    def validateStart(self):
        rc = True
        if(self.SourceDir == ""):
            wx.MessageBox("No Source Directory Selected!", self.AppName)
            rc = False        
        elif(self.ImageRootDir == ""):
            wx.MessageBox("You must provide directories first!", self.AppName)
            Options(self).Show()
            rc = False
        elif self.DestDirFormat == "":
            wx.MessageBox("Plesae set a valid sub dir format/name!", self.AppName)
            Options(self).Show()
            rc = False

        return rc

    def copyFile(self, file, tDir="", tFile=""):
        if os.path.exists(tFile) and self.cbOverwrite.GetValue() == False:
            self.logger("File {0} already exists in directory {1}, Skipping Copy".format(file, tDir))
            return True
            
        if not os.path.exists(tDir):
            os.makedirs(tDir)
        
        if self.cbMove.GetValue():
            move(file, tFile)
        else:
            copy2(file, tFile)

    def startRun( self, event ):
        self.toggleStartButton(False)
        self.SourceDir = self.dpickSource.GetPath()

        if not self.validateStart():
            self.toggleStartButton(True)
            return False

        def _startRun():
            self.stop_threads = False
            self.stMain.SetStatusText("Searching for Files...")
            sourceImageFiles = []
            sourceVideoFiles = []

            if self.rbSelection.GetStringSelection() in ('Images', 'Both'):
                sourceImageFiles = Util.getAllFiles(self.SourceDir, True, self.ImageTypes, self.ExcludeDirList)

            if self.rbSelection.GetStringSelection() in ('Videos', 'Both'):
                sourceVideoFiles = Util.getAllFiles(self.SourceDir, True, self.VideoTypes, self.ExcludeDirList)

            self.stMain.SetStatusText("Identified {0} file(s)".format(len(sourceImageFiles) + len(sourceVideoFiles)))

            totFiles = len(sourceImageFiles) + len(sourceVideoFiles)
            factor = 100 / (totFiles + 1)

            count = 1
            scnt = 0
            for item in (sourceImageFiles + sourceVideoFiles):
                if self.stop_threads:
                    break

                file  = item['file']
                ftype = item['type']

                dt = None
                destRoot = ""
                
                if ftype in self.ImageTypes:
                    dt = Util.getImageDate(file)
                    destRoot = self.ImageRootDir
                elif ftype in self.VideoTypes:
                    destRoot = self.VideoRootDir
                    dt = Util.getVideoDate(file)

                if(dt == None):
                    self.logger("Failed in extracting date for file {0}".format(file), level="ERROR")
                else:
                    fileName = os.path.basename(file)
                    destSubfolder = os.path.join(dt.strftime(self.DestDirFormat))
                    destPath = os.path.join(destRoot, destSubfolder)
                    destFile = os.path.join(destPath, fileName)

                    self.copyFile(file, tDir=destPath, tFile=destFile)
                    scnt += 1

                self.progress_bar.SetValue(count*factor)
                count+= 1

            self.progress_bar.SetValue(100)
            self.toggleStartButton(True)

            finalMsg = ""
            if totFiles == 0:
                finalMsg = "No Image/Video Files identified for Processing..."
            elif totFiles == scnt:
                finalMsg = "Completed. All files processed successfully..."
            else:
                finalMsg = "Done!. {0}/{1} file(s) processed, please check log for more details.".format(scnt, totFiles)

            self.logger(finalMsg)
            wx.MessageBox(finalMsg, self.AppName)
            self.progress_bar.SetValue(0)
            
        self.pill2kill = threading.Event()
        self.t = threading.Thread(target=_startRun)
        self.t.start()

        return True

    def setOptions( self, event ):
        Options(self).Show()

    def setLabels(self, ipath=None, vpath=None, gpath=None):
        if ipath != None:
            self.ImageRootDir = ipath
        if vpath != None:
            self.VideoRootDir = vpath
        if gpath != None:
            self.GarbageRootDir = gpath
        
        self.lblIroot.SetLabel("Image Root: " + self.ImageRootDir)
        self.lblVroot.SetLabel("Video Root: " + self.VideoRootDir)
        self.lblGroot.SetLabel("Garbage Root: " + self.GarbageRootDir)
        self.lblTypes.SetLabel("Image File Types: {0}\nVideo File Types: {1}".format(", ".join(self.ImageTypes), ", ".join(self.VideoTypes)))
        self.lblExcList.SetLabel("Exclude Directories: {0}".format(self.ExcludeDirList))

    def safeClose(self, event):
        if self.t and self.t.is_alive():
            wx.MessageBox("Please cancel current run", self.AppName, wx.OK | wx.ICON_EXCLAMATION )
            return True
        
        self.config.sections()
        self.config['USER'] = {}
        self.config['USER']['ImageRoot'] = self.ImageRootDir
        self.config['USER']['VideoRoot'] = self.VideoRootDir
        self.config['USER']['GarbageRoot'] = self.GarbageRootDir
        self.config['USER']['ExcludeDirList'] = self.ExcludeDirList
        self.config['USER']['DestDirFormat'] = self.DestDirFormat.replace('%', '%%')
        try:
            with open(self.configFile , 'w') as cfile:
                self.config.write(cfile)
        except:
            print("ERROR: Error in Writing Configuration profile")

        exit(0)

    def safeLoad(self):
        self.stMain.SetStatusWidths([320, -1, -2]) 
        self.progress_bar = wx.Gauge(self.stMain, -1, style=wx.GA_HORIZONTAL|wx.GA_SMOOTH) 
        rect = self.stMain.GetFieldRect(2)
        self.progress_bar.SetPosition((rect.x+2, rect.y+2)) 
        self.progress_bar.SetSize((rect.width-4, rect.height-4)) 


        self.toggleStartButton(True)
        if os.path.exists(self.configFile):
            self.config.read(self.configFile)
            if 'USER' in self.config:
                if 'ImageRoot' in self.config['USER'] and self.config['USER']['ImageRoot'] != "":
                    self.ImageRootDir = self.config['USER']['ImageRoot']
                
                if 'VideoRoot' in self.config['USER'] and self.config['USER']['VideoRoot'] != "":
                    self.VideoRootDir = self.config['USER']['VideoRoot']
                    
                if 'GarbageRoot' in self.config['USER'] and self.config['USER']['GarbageRoot'] != "":
                    self.GarbageRootDir = self.config['USER']['GarbageRoot']

                if 'ExcludeDirList' in self.config['USER'] and self.config['USER']['ExcludeDirList'] != "":
                    self.ExcludeDirList = self.config['USER']['ExcludeDirList']
        
                if 'DestDirFormat' in self.config['USER'] and self.config['USER']['DestDirFormat'] != "":
                    self.DestDirFormat = self.config['USER']['DestDirFormat']
        
    def cancelRun(self, event):
        rc = True
        ret = wx.ID_NO
        if self.t and self.t.is_alive():
            ret = wx.MessageBox("Do you Want to Cancel Current Run?", self.AppName, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION )
        if ret == wx.YES:
            if self.t:
                if self.t.is_alive():
                    self.stop_threads= True
                    self.logger("Terminating Execution..")
        elif(self.t.is_alive()):
            rc= False

        return rc

    def openLogs(self, event):
        self.logDig.Show(True)

    def logger(self, msg, level="INFO"):
        self.logDig.lblLog.SetLabel(self.logDig.lblLog.GetLabel() + "[{0}]: {1}\n".format(level, msg))
