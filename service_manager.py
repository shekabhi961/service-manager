from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os
import psutil
import winshell
from win32com.client import Dispatch
import subprocess

exist = 0

#xampp exist or not--------

if os.path.exists("C:/aunico/xampp") :
    print("ok")

elif 0==exist:
    os.startfile("C://aunico//xampp.exe")

#create shortcut launcher.bat------
if(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')):
        print("ok")

elif 0 == exist:

        desktop = winshell.desktop()
        path = os.path.join(desktop, "launcher.lnk")

        target = r"C:/aunico/launcher.bat"
        wDir = r"C:/aunico"
        icon = r"C:/aunico/launcher.bat"

        shell = Dispatch('WScript.shell')
        shortcut = shell.CreateShortCut(path)

        shortcut.Targetpath = target

        shortcut.WorkingDirectory = wDir

        shortcut.IconLocation = icon
        shortcut.save()


#Starting UI -------------
root=Tk()

    # add photo----------------------------------------------------------

photo = ImageTk.PhotoImage(Image.open("C://aunico//logo_HtC_icon.ico"))
panel = Label(root, image=photo)
panel.pack(side=TOP, fill=BOTH, expand=YES)

    #---------------------------------------------------------------------
    # array for program (convert list into dictionary)

thislist = ["firefox.exe","bakau.vbs","view.vbs"]
golist = ["firefox.exe","httpd.exe","mysqld.exe"]
appdict = {}
thisdict = {}
onlist = ["httpd.exe", "mysqld.exe"]
ondict = {}

#---------------------------------------------------------------------

    # more button function

def moreWindow():
    try:
        os.startfile('https://aunico.in')

    except:
            pass

    #----------------------------------------------------------------------

    #Contact button function-----------------------------------------------

def contact():
    window = tk.Toplevel(root)
    message = Label(window, text="Call us at +919116161661 from 9AM to 6PM", height=5, width=40).pack()
    Button(window, text='OK', height=2, width=5, command=window.destroy).pack()
    #-----------------------------------------------------------------------

    # function for start btn---------------------------------------------------

def mainProcess():

    for item in thislist:
        thisdict[item] = 0

    for item in thisdict:
        for process in psutil.process_iter():
            try:
                if process.name() == item:
                    thisdict[item] = 1
            except psutil.AccessDenied:
                error = 1

    print(thisdict)

    for state in thislist:
        appdict[state] = 0

    for item, state in thisdict.items():
        try:
            if (state == 0):
                ooy = item
                if ooy =="firefox.exe":
                    os.startfile("C:/aunico/firefox/firefox.exe")

                if ooy == "view.vbs":
                    subprocess.call(r"start cmd /c C:/aunico/view.vbs", shell=True)

                if ooy == "bakau.vbs":
                    subprocess.call(r"start cmd /c C:/aunico/bakau.vbs", shell=True)

        except:
            error = 1
            pass

    #--------------------------------------------------------------------------
    # function for stop button-------------------------------------------------

def stop():
    for item in golist:
        thisdict[item] = 0

    print(thisdict)

    for state in golist:
        appdict[state] = 1


    for item, state in appdict.items():
        try:
            if (state == 1):
                ooy = item
                for p in psutil.process_iter():
                    try:
                        if p.name() == ooy:
                            p.kill()
                    except:
                        error = 1
            pass
        except:
            error = 1

#-----------------------------------------------------------------
    #class for frame,title and button --------------------------------

class Ayush(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Ayush")
        self.start = Button(self, text="Start", font=("arial", 10, "bold"), height=5, width=10,fg="green", command=mainProcess)
        self.start.grid(row=0, column=0)
        self.stop = Button(self, text="Stop", font=("arial", 10, "bold"), height=5, width=10,command = stop)
        self.stop.grid(row=0, column=1)
        self.more = Button(self, text="More", font=("arial", 10, "bold"), height=5, width=10,command=moreWindow)
        self.more.grid(row=0, column=2)
        self.contactt= Button(self, text="Contact", font=("arial", 10, "bold"), height=5, width=10, command=contact)
        self.contactt.grid(row=0, column=3)
        self.quit = Button(self, text="QUIT", font=("arial", 10, "bold"), width=10, height=5,fg="red",command=self.quit)
        self.quit.grid(row=0, column=4)



com = Ayush()
root.mainloop()
