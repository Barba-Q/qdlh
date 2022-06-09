import os.path
import tkinter as tk
import subprocess                                       #to call bash commands
from tkinter import *                                   #I really don't know if this is necessary
from tkinter.ttk import *                               #to show fancy icons
from tkinter import messagebox                          #to show, you guessed it, a message box
from tkinter.messagebox import askokcancel, showinfo, WARNING  #display warnings and stuff to dismiss with a single click


#software to implement:


#gnome-software

#thunderbird
#evolution
#kmail
#gparted
#gnome-terminal
#xterm
#gnome system monitor
#gedit


bg_color = "#424242"
text_color = "#ffffff"



mainwindow = tk.Tk(className = ">qdlh_menu<")   

softwarepath = '/usr/share/applications/'
softwarelist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0


def Mainwindow():
    global mainwindow, softwarelist, softwarepath, count
    row_cnt = 1
    col_cnt = 0
    col_max = 9
    setpadx = 10
    setpady = 20
    
# get window size
    mainwindow['background'] = bg_color,
    windowWidth = mainwindow.winfo_reqwidth()
    windowHeight = mainwindow.winfo_reqheight()
# get both half the screen width/height and window width/height
    positionRight = int(mainwindow.winfo_screenwidth()/3 - windowWidth/2)
    positionDown = int(mainwindow.winfo_screenheight()/3 - windowHeight/2)
# position the window in the center of the screen.
    mainwindow.geometry("+{}+{}".format(positionRight, positionDown))
# set windowgrid
    mainwindow.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=90, weight=2)
    mainwindow.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=100, weight=2)


    Label_1 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Qtile Menu", background = bg_color, fg = text_color)
    Label_1.grid(row = 0, column = 4, sticky = "nsew")

#A
    if os.path.exists(softwarepath+'audacity.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Audacity",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['audacity'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#B
    if os.path.exists(softwarepath+'barrier.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Barrier",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['barrier'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#C
    if os.path.exists(softwarepath+'clementine.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Clementine",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['clementine'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#D

    if os.path.exists(softwarepath+'org.kde.discover.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Discover",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['plasma-discover'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'org.kde.dolphin.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Dolphin",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['dolphin'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0
#E

    if os.path.exists(softwarepath+'org.gnome.Evolution.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Evolution",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['evolution'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#F
    if os.path.exists(softwarepath+'org.kde.falkon.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Falkon",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['falkon'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'firefox.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Firefox",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['firefox'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'org.freeciv.gtk3.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady,
        padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "FreeCiv",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['freeciv-gtk3'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#G
    if os.path.exists(softwarepath+'org.gnome.gedit.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Gedit",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['gedit'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'gimp.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Gimp",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['gimp'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'org.gnome.Software.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Gnome\nSoftware",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['gnome-software'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'google-chrome.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Chrome",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['google-chrome'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'gparted.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Gparted",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['gparted'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#H

#I

#J

#K
    if os.path.exists(softwarepath+'org.kde.kate.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Kate",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['kate'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'org.kde.kdenlive.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Kdenlive",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['kdenlive'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'systemsettings.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Kde Settings",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['systemsettings5'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'kmail_view.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "KMail",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['kmail'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'org.kde.konsole.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Konsole",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['konsole'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#L
    if os.path.exists(softwarepath+'lxqt-config.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "LXQT Settings",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['lxqt-config'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#M

#N
    if os.path.exists(softwarepath+'org.gnome.Nautilus.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Nautilus",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['nautilus'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#O
    if os.path.exists(softwarepath+'com.obsproject.Studio.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "OBS-Studio",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['obs'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0
        
    if os.path.exists(softwarepath+'libreoffice-startcenter.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Office",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['libreoffice'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#P
    if os.path.exists(softwarepath+'pcmanfm-qt.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "PCMan-FM",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['pcmanfm-qt'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'PrusaSlicer.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Prusa Slicer",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['prusa-slicer'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#Q

#R

#S
    if os.path.exists(softwarepath+'steam.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Steam",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['steam'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

    if os.path.exists(softwarepath+'org.kde.systemmonitor.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "System\nMonitor",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['systemmonitor'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#T
    if os.path.exists(softwarepath+'thunderbird.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "Thunderbird",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['thunderbird'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#U

#V
    if os.path.exists(softwarepath+'vlc.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "VLC",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['vlc'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#W

#X

#Y
    if os.path.exists(softwarepath+'org.opensuse.YaST.desktop') == TRUE:
        button_1 = tk.Button(mainwindow,
        pady=setpady, padx=setpadx,
        background = bg_color,
        fg = text_color,
        text = "YaST",
        compound = TOP,
        command = lambda:[mainwindow.destroy(), subprocess.call(['xterm','-e', 'su -c /sbin/yast2'])],
        relief = FLAT)
        button_1.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
        col_cnt = col_cnt + 1
        if col_cnt == col_max:
            row_cnt = row_cnt + 1
            col_cnt = 0

#Z

#Buttons
    button_101 = tk.Button(mainwindow,
    pady=setpady, padx=setpadx,
    background = bg_color,
    fg = text_color,
    text = "Qtile Settings",
    compound = TOP,
    command = lambda:[mainwindow.destroy(), subprocess.call(['qdlh'])],
    relief = FLAT)
    button_101.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
    col_cnt = col_cnt + 1
    if col_cnt == col_max:
        row_cnt = row_cnt + 1
        col_cnt = 0
    
    button_102 = tk.Button(mainwindow,
    pady=setpady, padx=setpadx,
    background = bg_color,
    fg = text_color,
    text = "Reboot",
    compound = TOP,
    command = lambda:[mainwindow.destroy(), subprocess.call(['xterm','-e', 'su -c reboot'])],
    relief = FLAT)
    button_102.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
    col_cnt = col_cnt + 1
    if col_cnt == col_max:
        row_cnt = row_cnt + 1
        col_cnt = 0

    button_103 = tk.Button(mainwindow,
    pady=setpady, padx=setpadx,
    background = bg_color,
    fg = text_color,
    text = "Shutdown",
    compound = TOP,
    command = lambda:[mainwindow.destroy(), subprocess.call(['xterm','-e', 'su -c init 0'])],
    relief = FLAT)
    button_103.grid(row = row_cnt, column = col_cnt, sticky = "nsew")
    col_cnt = col_cnt + 1
    if col_cnt == 8:
        row_cnt = row_cnt + 1
        col_cnt = 0


    button_100 = tk.Button(mainwindow,
    pady=setpady, padx=setpadx,
    background = bg_color,
    fg = text_color,
    text = "Close",
    compound = TOP,
    command = lambda:[mainwindow.destroy()],
    relief = FLAT)
    button_100.grid(row = row_cnt +1, column = 4, sticky = "nsew")
  

Mainwindow()
mainwindow.mainloop()
