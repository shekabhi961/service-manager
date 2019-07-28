import pytweening
from tkinter import *
import tkinter as tk
import mysql.connector
from datetime import datetime,timedelta,date
from PIL import ImageTk, Image
import tkinter.messagebox as tm
import smtplib

#GUI Window-----------------------------------------------------

root = Tk()
root.title("User Panel")
root.minsize(width=500,height=300)
root.resizable(0,0)

#add photo--------------------------------------------

photo = ImageTk.PhotoImage(Image.open("F:/logo.ico"))
panel = Label(root, image=photo)
panel.pack(side=TOP, fill=BOTH, expand=YES)

######################################################

id = StringVar()
nm = StringVar()
add = StringVar()
exp_date = StringVar()
start_date = StringVar()

id1 = StringVar()
nm1 = StringVar()
add1 = StringVar()
exp_date1 = StringVar()
start_date1 = StringVar()

id2 = StringVar()
nm2 = StringVar()
add2 = StringVar()
exp_date2 = StringVar()
start_date2 = StringVar()





class demo(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("DOMAIN")
        self.window = tk.Toplevel()
        self.window.title("DOMAIN DATABASE")
        self.window.minsize(width=300, height=100)

        self.photo = ImageTk.PhotoImage(Image.open("F:/logo.ico"))
        self.pan = Label(self.window, image=photo)
        self.pan.pack()

        def dem():
            head = Label(self.window, text="Domain Database", font=("arial", 20, "bold")).pack()

            label_3 = Label(self.window, text="Id", font=("arial", 10, "bold")).pack()
            entry_3 = Entry(self.window, textvariable=id).pack()

            label = Label(self.window, text="Name", font=("arial", 10, "bold")).pack()
            entry = Entry(self.window, textvariable=nm).pack()

            label_1 = Label(self.window, text="Address", font=("arial", 10, "bold")).pack()
            entry_1 = Entry(self.window, textvariable=add).pack()

            label_2 = Label(self.window, text="Exp_date", font=("arial", 10, "bold")).pack()
            entry_2 = Entry(self.window, textvariable=exp_date).pack()

            label3 = Label(self.window, text="Start_date", font=("arial", 10, "bold")).pack()
            entry3 = Entry(self.window, textvariable=start_date).pack()

            var = IntVar()
            Gender = Label(self.window, text='Status', font=("arial", 10, "bold")).pack()
            radio = Radiobutton(self.window, text="Purchased", variable=var, value=0).pack()
            radio_1 = Radiobutton(self.window, text="Rented", variable=var, value=1).pack()

            submit = Button(self.window, text="submit", font=("arial", 10, "bold"), command=domain).pack()
            btn1 = Button(self.window, text="quit", font=("arial", 10, "bold"), command=quit).pack()

        dem()


class demo1(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("HOST")
        self.window = tk.Toplevel()
        self.window.title("HOST DATABASE")
        self.window.minsize(width=300, height=100)

        self.photo = ImageTk.PhotoImage(Image.open("F:/logo.ico"))
        self.pan = Label(self.window, image=photo)
        self.pan.pack()

        def dem1():
            head = Label(self.window, text="Host Database", font=("arial", 20, "bold")).pack()

            label_3 = Label(self.window, text="Id", font=("arial", 10, "bold")).pack()
            entry_3 = Entry(self.window, textvariable=id1).pack()

            label = Label(self.window, text="Name", font=("arial", 10, "bold")).pack()
            entry = Entry(self.window, textvariable=nm1).pack()

            label_1 = Label(self.window, text="Address", font=("arial", 10, "bold")).pack()
            entry_1 = Entry(self.window, textvariable=add1).pack()

            label_2 = Label(self.window, text="Exp_date", font=("arial", 10, "bold")).pack()
            entry_2 = Entry(self.window, textvariable=exp_date1).pack()

            label3 = Label(self.window, text="Start_date", font=("arial", 10, "bold")).pack()
            entry3 = Entry(self.window, textvariable=start_date1).pack()

            var = IntVar()
            Gender = Label(self.window, text='Status', font=("arial", 10, "bold")).pack()
            radio = Radiobutton(self.window, text="Purchased", variable=var, value=0).pack()
            radio_1 = Radiobutton(self.window, text="Rented", variable=var, value=1).pack()

            submit = Button(self.window, text="submit", font=("arial", 10, "bold"), command=Host).pack()
            btn1 = Button(self.window, text="quit", font=("arial", 10, "bold"), command=quit).pack()

        dem1()


class demo2(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("SSL")
        self.window = tk.Toplevel()
        self.window.title("SSL DATABASE")
        self.window.minsize(width=300, height=100)

        self.photo = ImageTk.PhotoImage(Image.open("F:/logo.ico"))
        self.pan = Label(self.window, image=photo)
        self.pan.pack()

        def dem2():
            head = Label(self.window, text="SSL Database", font=("arial", 20, "bold")).pack()

            label_3 = Label(self.window, text="Id", font=("arial", 10, "bold")).pack()
            entry_3 = Entry(self.window, textvariable=id2).pack()

            label = Label(self.window, text="Name", font=("arial", 10, "bold")).pack()
            entry = Entry(self.window, textvariable=nm2).pack()

            label_1 = Label(self.window, text="Address", font=("arial", 10, "bold")).pack()
            entry_1 = Entry(self.window, textvariable=add2).pack()

            label_2 = Label(self.window, text="Exp_date", font=("arial", 10, "bold")).pack()
            entry_2 = Entry(self.window, textvariable=exp_date2).pack()

            label3 = Label(self.window, text="Start_date", font=("arial", 10, "bold")).pack()
            entry3 = Entry(self.window, textvariable=start_date2).pack()

            var = IntVar()
            Gender = Label(self.window, text='Status', font=("arial", 10, "bold")).pack()
            radio = Radiobutton(self.window, text="Purchased", variable=var, value=0).pack()
            radio_1 = Radiobutton(self.window, text="Rented", variable=var, value=1).pack()

            submit = Button(self.window, text="submit", font=("arial", 10, "bold"), command=SSL).pack()
            btn1 = Button(self.window, text="quit", font=("arial", 10, "bold"), command=quit).pack()

        dem2()


######################################
#DATABASE CONNECT----------------------------
#######################################

connect = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database='test')

cursor = connect.cursor()

######----DOMAIN----########

def domain():
    uid=id.get()
    name=nm.get()
    Add=add.get()
    e_date=exp_date.get()
    s_date =start_date.get()

    try:
        cursor.execute('CREATE TABLE domain (domain_id VARCHAR(25),domain_name VARCHAR(50),Address VARCHAR(100),'
                       'Start_date DATE, Exp_date DATE)')
        cursor.execute("INSERT INTO domain (domain_id,domain_name,Address,Start_date,Exp_date) VALUES (%s,%s,%s,%s,%s)",
                   (uid,name,Add,s_date,e_date))

    except:
        cursor.execute("INSERT INTO domain (domain_id,domain_name,Address,Start_date,Exp_date) VALUES (%s,%s,%s,%s,%s)",
                       (uid, name, Add, s_date, e_date))

    connect.commit()


######----HOST----########

def Host():
    uid=id1.get()
    name=nm1.get()
    Add=add1.get()
    e_date=exp_date1.get()
    s_date =start_date1.get()

    try:
        cursor.execute('CREATE TABLE host (host_id VARCHAR(25),host_name VARCHAR(50),Address VARCHAR(100),'
                   'Start_date DATE,Exp_date DATE)')
        cursor.execute("INSERT INTO host (host_id,host_name,Address,Start_date,Exp_date) VALUES (%s,%s,%s,%s,%s)",
                   (uid,name,Add,s_date,e_date))
    except:
        cursor.execute("INSERT INTO host (host_id,host_name,Address,Start_date,Exp_date) VALUES (%s,%s,%s,%s,%s)",
                       (uid, name, Add, s_date, e_date))

    connect.commit()

######----SSL----########

def SSL():
    uid=id2.get()
    name=nm2.get()
    Add=add2.get()
    e_date=exp_date2.get()
    s_date =start_date2.get()

    try:
        cursor.execute('CREATE TABLE sl (s_id VARCHAR(25),s_name VARCHAR(50),Address VARCHAR(100),'
                   'Start_date DATE,Exp_date DATE)')
        cursor.execute("INSERT INTO sl (s_id,s_name,Address,Start_date,Exp_date) VALUES (%s,%s,%s,%s,%s)",
                    (uid, name, Add, s_date, e_date))
    except:
        cursor.execute("INSERT INTO sl (s_id,s_name,Address,Start_date,Exp_date) VALUES (%s,%s,%s,%s,%s)",
                       (uid, name, Add, s_date, e_date))

    connect.commit()

###################################
#Notification---------------------
###################################

SUCCESS_BACKGROUND = "#60a917"
WARNING_BACKGROUND = "#fa6800"
ALERT_BACKGROUND = "#ce352c"
INFO_BACKGROUND = "#59cde2"

class Notification(Toplevel):
    def __init__(self, notification_manager, builder, index, x, y, h, v, padx, pady, background=None, on_hide=None):
        Toplevel.__init__(self)

        self._notification_manager = notification_manager

        # Removes the native window boarder.
        self.overrideredirect(True)

        notification_frame = Frame(self)
        notification_frame.pack(expand=True, fill=BOTH, padx=padx, pady=pady)

        top_row = Frame(notification_frame)
        top_row.pack(fill=X)

        if not hasattr(notification_manager, "_close_icon"):
            notification_manager._close_icon = PhotoImage(
                data="R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6"
                     "cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEA"
                     "LoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+A"
                     "LE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBB"
                     "ANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8"
                     "X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJi"
                     "eGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7"
                     "vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                     "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                     "AAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+P"
                     "QgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4s"
                     "ELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFW"
                     "IAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw==")

        close_button = Button(top_row, image=notification_manager._close_icon, highlightthickness=0, borderwidth=0,
                              command=exit)
        close_button.pack(side=RIGHT, anchor=E)

        self.interior = Frame(notification_frame)
        self.interior.pack(expand=True, fill=BOTH)

        if builder:
            builder(self.interior)

        if background is not None:
            top_row.config(background=background)
            notification_frame.config(background=background)
            self.config(background=background)
            self.interior.config(background=background)
            close_button.config(background=background)

        self.place(x, y, h, v)

    @property
    def x(self):
        return self._offset_x

    @property
    def y(self):
        return self._offset_y

    @property
    def h(self):
        return self._h

    @property
    def v(self):
        return self._v

    def place(self, x, y, h, v):
        ''' The windows overall position on the screen  '''
        self.wm_geometry("{h}{x}{v}{y}".format(x=x, y=y, h=h, v=v))

        self._offset_x = x
        self._offset_y = y
        self._h = h
        self._v = v

    def start_animation(self, easing_function, ticks, duration, start_time=0):
        self._tick = 0
        self._total_ticks = int(ticks)
        self._easing_function = easing_function
        self._duration = duration

        self._interval_time = int(duration * 1000 / self._total_ticks)

        if start_time != 0:
            self.after(int(start_time * 1000), self._animate)
        else:
            self._animate()

    def _animate(self):
        t = self._tick / self._total_ticks
        # This changes the alpha value (How transparent the window should be).
        # It ranges from 0.0 (completely transparent) to 1.0 (completely opaque).
        self.attributes("-alpha", self._easing_function(1 - t))

        self._tick += 1

        if self._tick <= self._total_ticks:
            self.after(self._interval_time, self._animate)
        else:
            self.after(self._interval_time, self.quit)

#Notification---------------------------

class Notification_Manager(object):
    def __init__(self, offset_x=12, offset_y=8, corner=N + E, background=None, spacing=5, ticks=15,
                 easing_function=pytweening.linear, duration=3, start_time=3, padx=5, pady=5):
        if corner == N + W:
            self._h = "+"
            self._v = "+"
        elif corner == N + E:
            self._h = "-"
            self._v = "+"
        elif corner == S + W:
            self._h = "+"
            self._v = "-"
        elif corner == S + E:
            self._h = "-"
            self._v = "-"
        else:
            raise ValueError("Not a valid corner value: %s" % corner)

        self._list_of_notifications = []

        self._offset_x = offset_x
        self._offset_y = offset_y
        self._padx = padx
        self._pady = pady
        self._corner = corner
        self._background = background
        self._ticks = ticks
        self._duration = duration
        self._easing_function = easing_function
        self._spacing = spacing
        self._start_time = start_time

    @property
    def corner(self):
        return self._corner

    @property
    def background(self):
        return self._background

    @property
    def duration(self):
        return self._duration

    @property
    def spacing(self):
        return self._spacing

    @property
    def ticks(self):
        return self._ticks

    def create_notification(self, builder, start_time=None, duration=None, easing_function=None, ticks=None,
                            background=None, padx=None, pady=None, on_hide=None):
        if ticks is None:
            ticks = self._ticks

        if builder is None:
            builder = self._builder

            notification.on_hide = on_hide

        if duration is None:
            duration = self._duration

        if easing_function is None:
            easing_function = self._easing_function

        if background is None:
            background = self._background

        if padx is None:
            padx = self._padx

        if pady is None:
            pady = self._pady

        if start_time is None:
            start_time = self._start_time

        if len(self._list_of_notifications) == 0:
            x = self._offset_x
            y = self._offset_y

            index = 0
        else:
            last_notification = self._list_of_notifications[-1]
            last_notification.update_idletasks()

            x = self._offset_x
            y = last_notification.y + last_notification.winfo_height() + self._spacing

            index = len(self._list_of_notifications)

        notification = Notification(self, builder, index, x, y, self._h, self._v, padx, pady, background, on_hide)
        self._list_of_notifications.append(notification)

        notification.start_animation(easing_function=easing_function, ticks=ticks, duration=duration,
                                     start_time=start_time)

    def simple_notification(self, text, foreground, background, font=None, width=None, anchor=None, justify=None,
                            wraplength=None, start_time=None, duration=None, easing_function=None, ticks=None,
                            padx=None, pady=None, on_hide=None):
        builder = self.create_builder(text, foreground, background, font=font, width=width, anchor=anchor,
                                      justify=justify, wraplength=wraplength)
        self.create_notification(builder, background=background, start_time=start_time, duration=duration,
                                 easing_function=easing_function, ticks=ticks, padx=padx, pady=pady, on_hide=on_hide)

    def success(self, text, font=None, width=None, anchor=None, justify=None, wraplength=None, start_time=None,
                duration=None, easing_function=None, ticks=None, padx=None, pady=None, on_hide=None):
        self.simple_notification(text, "white", SUCCESS_BACKGROUND, font=font, width=width, anchor=anchor,
                                 justify=justify, wraplength=wraplength, start_time=start_time, duration=duration,
                                 easing_function=easing_function, ticks=ticks, padx=padx, pady=pady, on_hide=on_hide)

    def warning(self, text, font=None, width=None, anchor=None, justify=None, wraplength=None, start_time=None,
                duration=None, easing_function=None, ticks=None, padx=None, pady=None, on_hide=None):
        self.simple_notification(text, "white", WARNING_BACKGROUND, font=font, width=width, anchor=anchor,
                                 justify=justify, wraplength=wraplength, start_time=start_time, duration=duration,
                                 easing_function=easing_function, ticks=ticks, padx=padx, pady=pady, on_hide=on_hide)

    def alert(self, text, font=None, width=None, anchor=None, justify=None, wraplength=None, start_time=None,
              duration=None, easing_function=None, ticks=None, padx=None, pady=None, on_hide=None):
        self.simple_notification(text, "white", ALERT_BACKGROUND, font=font, width=width, anchor=anchor,
                                 justify=justify, wraplength=wraplength, start_time=start_time, duration=duration,
                                 easing_function=easing_function, ticks=ticks, padx=padx, pady=pady, on_hide=on_hide)

    def info(self, text, font=None, width=None, anchor=None, justify=None, wraplength=None, start_time=None,
             duration=None, easing_function=None, ticks=None, padx=None, pady=None, on_hide=None):
        self.simple_notification(text, "white", INFO_BACKGROUND, font=font, width=width, anchor=anchor, justify=justify,
                                 wraplength=wraplength, start_time=start_time, duration=duration,
                                 easing_function=easing_function, ticks=ticks, padx=padx, pady=pady, on_hide=on_hide)

    def create_builder(self, text, foreground, background, font=None, width=None, anchor=None, justify=None,
                       wraplength=None):
        kwargs = dict(text=text, fg=foreground, background=background)

        if font:
            kwargs["font"] = font

        if anchor:
            kwargs["anchor"] = anchor

        if justify:
            kwargs["justify"] = justify

        if width:
            kwargs["width"] = width

        if wraplength:
            kwargs["wraplength"] = wraplength

        def builder(interior):
            Label(interior, **kwargs).pack()

        return builder

notification_manager = Notification_Manager(background="white")

#database----------------------------------------------

now = datetime.now().date()

##################################
###---Send Email---###
##################################


def send_email(user, password, recipient, subject, body):
    gmail_user = user
    gmail_pwd = password
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()

#function to check database file is currently running or expired------

###########################################-------------------------------------

def checkone():
    cursor.execute("SELECT Exp_date FROM domain")
    row = cursor.fetchall()
    for i in row:
        res = i[0]
        compare = res - now
        print(compare)

        from datetime import timedelta

        if compare > timedelta():

            cursor.execute("SELECT domain_name FROM domain ")
            varp = cursor.fetchall()
            for i in varp:
                r = i[0]
                print(r)

                if r :
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + r + str(compare.days) + " is expiring soon ")

                    notification_manager.alert(str(compare.days) + " days remaining, Please update")

                    break

        elif compare == timedelta():
            cursor.execute("SELECT domain_name FROM domain ")
            varm = cursor.fetchall()
            for i in varm:
                resp = i[0]
                print(resp)

                if resp:
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                           "Hey!!" + resp + str(compare.days) + " is expiring today, Update Immediately " )

                    notification_manager.warning("warning! your account may discontinued from tomorrow")

                    break

        elif compare < timedelta():
            cursor.execute("SELECT domain_name FROM domain ")
            vare = cursor.fetchall()
            for i in vare:
                resps = i[0]
                print(resps)

                if resps:
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                           "Hey!!" + resps + str(compare.days) + " is expired, Please Contact Service Provider " )

                    notification_manager.info("your account is expired")

                    break

###########################################-------------------------------------

def checktwo():
    cursor.execute("SELECT Exp_date FROM host")
    row = cursor.fetchall()
    for i in row:
        res = i[0]
        compare = res - now
        print(compare)

        from datetime import timedelta

        if compare > timedelta():
            cursor.execute("SELECT host_name FROM host ")
            varp = cursor.fetchall()
            for i in varp:
                r = i[0]
                print(r)

                if r:
                    notification_manager.info(str(compare.days)+ " days remaining, " + " your account is is expiring soon")
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + r + str(compare.days) + " is expiring soon ")

                    break

        elif compare == timedelta():
            cursor.execute("SELECT host_name FROM host ")
            varm = cursor.fetchall()
            for i in varm:
                resp = i[0]
                print(resp)

                if resp:
                    notification_manager.info("your account is expiring today, Update Immediately")
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + resp + str(compare.days) + " is expiring today, Update Immediately ")
                    break


        elif compare < timedelta():
            cursor.execute("SELECT host_name FROM host ")
            vare = cursor.fetchall()
            for i in vare:
                resps = i[0]
                print(resps)

                if resps:
                    notification_manager.info("your account is expired")
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + resps + str(compare.days) + " is expired, Please Contact Service Provider ")
                    break

###########################################-------------------------------------

def checkthree():
    cursor.execute("SELECT Exp_date FROM sl")
    row = cursor.fetchall()
    for i in row:
        res = i[0]
        compare = res - now
        print(compare)

        from datetime import timedelta

        if compare > timedelta():
            cursor.execute("SELECT s_name FROM sl ")
            varp = cursor.fetchall()
            for i in varp:
                r = i[0]
                print(r)

                if r:
                    notification_manager.info(str(compare.days) + " days remaining, " + " your account is is expiring soon")
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + r + str(compare.days) + " remaining only, license is expiring soon ")

                    break

        elif compare == timedelta():
            cursor.execute("SELECT s_name FROM sl ")
            varm = cursor.fetchall()
            for i in varm:
                resp = i[0]
                print(resp)

                if resp:
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + resp + str(compare.days) + " is expiring today, Update Immediately ")
                    break


        elif compare < timedelta():
            cursor.execute("SELECT s_name FROM sl ")
            vare = cursor.fetchall()
            for i in vare:
                resps = i[0]
                print(resps)

                if resps:
                    send_email("shekabhi961@gmail.com", "9602311961", "tiwariayush961@gmail.com", "AntMan",
                               "Hey!!" + resps + str(compare.days) + " is expired, Please Contact Service Provider ")
                    break

######################################
#Login--------------------
######################################

class Login(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username", font=("arial", 10, "bold"))
        self.entry_username = Entry(self)
        self.label_password = Label(self, text="Password", font=("arial", 10, "bold"))
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0,column=0)
        self.label_password.grid(row=1,column=0)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", font=("arial", 10, "bold"), command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.exitbtn = Button(self, text="Exit", font=("arial", 10, "bold"), command=self.quit)
        self.exitbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "" and password == "":
            tm.showinfo("Login info", "Welcome Ayush")
            Ayush()
            checkone()
            checktwo()
            checkthree()
        else:
            tm.showerror("Login error", "Incorrect username")

#------------------------------------------------------------------


class Ayush(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Ayush")
        self.window = tk.Toplevel()
        self.window.title("DATABASE MANAGEMENT SYSTEM")
        self.window.minsize(width=300, height=200)

        self.photo = ImageTk.PhotoImage(Image.open("F:/logo.ico"))
        self.pan = Label(self.window, image=photo)
        self.pan.grid(row=0,column=5)

        self.database = Label(self.window, text="DATABASE MANAGEMENT", font=("arial", 10, "bold"))
        self.database.grid(row=5, column=5)
        self.domain = Button(self.window, text="Domain", font=("arial", 10, "bold"), command=demo, height=2, width=8,
                             fg="green")
        self.domain.grid(row=8, column=6)
        self.host = Button(self.window, text="Host", font=("arial", 10, "bold"), command=demo1, height=2, width=5,
                           fg="green")
        self.host.grid(row=8, column=4)
        self.sl = Button(self.window, text="SSL", font=("arial", 10, "bold"), command=demo2, height=2, width=5,
                         fg="green")
        self.sl.grid(row=8, column=5)
        self.quit = Button(self.window, text="QUIT", font=("arial", 10, "bold"), width=5, height=2, fg="red",
                           command=exit)
        self.quit.grid(row=9, column=5)


#----------------------------------------------------------------

IF = Login(root)

root.mainloop()

