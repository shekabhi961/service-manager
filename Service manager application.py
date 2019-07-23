from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os
import psutil
from scratch2 import *
from datetime import datetime


root=Tk()


    # add photo----------------------------------------------------------

photo = ImageTk.PhotoImage(Image.open("logo_HtC_icon.ico"))
panel = Label(root, image=photo)
panel.pack(side=TOP, fill=BOTH, expand=YES)

    #---------------------------------------------------------------------

    # array for program (convert list into dictionary)

thislist = ["sublime_text.exe","firefox.exe","xampp-control.exe"]
appdict = {}
thisdict = {}

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

    # function to open browser for update-----------------------------------

def updateWindow():
    try:
        os.startfile('C:/aunico/firefox/firefox.exe')

    except:
            pass

    #-----------------------------------------------------------------------

    #function to check license is currently running or expired--------------

def checkdesk():
    present = datetime.now()
    user = exp()
    dict_time = user - present
    print(dict_time)

    if user >= present:
        window = tk.Toplevel(root)
        message = Label(window, text="Renew License Soon", font=("arial", 10, "bold"), height=10, width=30).pack()
        b = Button(window, text='update', height=2, width=5, command=updateWindow).pack()
        b1 = Button(window, text='OK', height=2, width=5, command=window.destroy).pack()

        print('Renew License Soon!')

    elif user <= present:
        print('License Expired, Update now')
        exit()

    #--------------------------------------------------------------------------

    # function for start btn---------------------------------------------------

def mainProcess():

    checkdesk() # call function from above-------------------------------------

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
                if ooy=="sublime_text.exe":
                    os.startfile("C:/aunico/sublimetext3/sublime_text.exe")

                elif ooy== "xampp-control.exe":
                    os.startfile("C:/aunico/xampp/xampp-control.exe")

                elif ooy=="firefox.exe":
                    os.startfile("C:/aunico/firefox/firefox.exe")
                pass
        except:
            error = 0
            pass

    #--------------------------------------------------------------------------

    # function for stop button-------------------------------------------------

def stop():
    for item in thislist:
        thisdict[item] = 0

    print(thisdict)

    for state in thislist:
        appdict[state] = 1

    for item, state in appdict.items():
        try:
            if (state == 1 ):
                ooy = item
                for p in psutil.process_iter():
                        try:
                            if p.name() == ooy:
                                p.kill()
                        except:
                            error=1
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