# Qtile-dlh alpha
# A true mess made with love and kate

########################################
#   python imports
########################################

import tkinter as tk
import subprocess                                       #to call bash commands (if ever needed)
from tkinter import *
from tkinter.ttk import *                               #to show fancy icons
from tkinter.colorchooser import askcolor               #color picker
from tkinter.filedialog import askopenfilename          #open file dialog
from tkinter import messagebox                          #simple message box
from tkinter.messagebox import askokcancel, showinfo, WARNING  #display warnings and stuff
from pathlib import Path



########################################
#   init main window
########################################

mainwindow = tk.Tk(className = ">Qtile-dlh alpha(!)<")        #This inits the mainwindow an the titlename


########################################
#   variables
########################################

#checkboxes
mainwindow_checkbox_1_selected  = tk.IntVar()
mainwindow_checkbox_2_selected  = tk.IntVar()
mainwindow_checkbox_3_selected  = tk.IntVar()
mainwindow_checkbox_4_selected  = tk.IntVar()
mainwindow_checkbox_5_selected  = tk.IntVar()
mainwindow_checkbox_6_selected  = tk.IntVar()
mainwindow_checkbox_7_selected  = tk.IntVar()
mainwindow_checkbox_8_selected  = tk.IntVar()
mainwindow_checkbox_9_selected  = tk.IntVar()
mainwindow_checkbox_10_selected = tk.IntVar()
mainwindow_checkbox_11_selected = tk.IntVar()
mainwindow_checkbox_12_selected = tk.IntVar()

#textfields
mainwindow_textinput_1          = "enter value"
mainwindow_textinput_2          = "enter value"
mainwindow_textinput_3          = "enter value"
mainwindow_textinput_4          = "enter value"
mainwindow_textinput_5          = "enter value"
mainwindow_textinput_6          = "enter value"
mainwindow_textinput_7          = "enter value"
mainwindow_textinput_8          = "enter value"
mainwindow_textinput_9          = "enter value"
mainwindow_textinput_10         = "enter value"
mainwindow_textinput_11         = "enter value"
mainwindow_textinput_12         = "enter value"

#entryfields
entry_1_var     = tk.StringVar()
entry_2_var     = tk.StringVar()
entry_3_var     = tk.StringVar()
entry_4_var     = tk.StringVar()
entry_5_var     = tk.StringVar()
entry_6_var     = tk.StringVar()
entry_7_var     = tk.StringVar()
entry_8_var     = tk.StringVar()
entry_9_var     = tk.StringVar()
entry_10_var    = tk.StringVar()
entry_11_var    = tk.StringVar()
entry_12_var    = tk.StringVar()

entry_as1_var   = tk.StringVar()
entry_as2_var   = tk.StringVar()
entry_as3_var   = tk.StringVar()
entry_as4_var   = tk.StringVar()
entry_as5_var   = tk.StringVar()

#drop down lists
list_1_var      = tk.StringVar()
list_2_var      = tk.StringVar()
list_barpos_var = tk.StringVar()

#default values
filepath        = "~/.config/qtile/wallpaper.png"
barcolor_set    = "#424242"
accentcolor_set = "#49a1b5"
textcolor_set   = "#f00000"


home = Path.home()
print(home)


########################################
#   methods
########################################

# collect all set values and write it to a config
# the config is used as a interface to move variables to the qtile config
def prime_config():
    global home
    global filepath
    global barcolor_set
    global accentcolor_set
    global textcolor_set

    lines = ["panelsize =" + str(entry_1_var.get()),
            "textsize =" + str(entry_2_var.get()),
            "margin =" + str(entry_3_var.get()),
            "wallpaper_img =" + '"' +  str(filepath) + '"',
            "bgcolor =" + '"' + str(barcolor_set) + '"',
            "fgcolor =" + '"' + str(accentcolor_set) + '"',
            "tecolor =" + '"' + str(textcolor_set) + '"',
            "barpos =" + '"' + str(list_barpos_var.get()) + '"',
            "wallpaper_set =" + '"' + str(list_1_var.get()) + '"',
            "keyboardlayout =" + '"' + str(list_2_var.get()) + '"']

    PRIME = open(str(home) + "/.config/qtile/qdlh_conf.py", "w")
    with open('qdlh_conf.py', 'w', encoding='utf-8') as PRIME:
        PRIME.write('\n'.join(lines))

    messagebox.showinfo("Done", "Press Meta + Ctrl + R for the settings to take effect\n(Does not affect autostart settings)")

# value for colors
def barcolor():
    global barcolor_set
    barcolor_set = askcolor(title = "Choose a color")
    return barcolor_set[1]

def accentcolor():
    global accentcolor_set
    accentcolor_set = askcolor(title = "Choose a color")
    return accentcolor_set[1]

def textcolor():
    global textcolor_set
    textcolor_set = askcolor(title = "Choose a color")
    return textcolor_set[1]

# path of the wallpaper // should check for png and jpg files in the future
def wallpaper_path():
    global filepath
    filepath = askopenfilename()
    return filepath

# quit button

def quit():
    exit()


########################################
#   main window contents
########################################

def Mainwindow():
    global mainwindow
    global contents
    setpadx = 2
    setpady = 2

# windowgrid (should use pack in the future)
    mainwindow.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20],
                            minsize=1, weight=1)
    mainwindow.rowconfigure(18, minsize=1, weight=20)   # this is just for aesthetics

    mainwindow.columnconfigure(0, minsize=1, weight=1)
    mainwindow.columnconfigure(1, minsize=1, weight=2)
    mainwindow.columnconfigure(2, minsize=1, weight=2)
    mainwindow.columnconfigure(3, minsize=1, weight=2)
    mainwindow.columnconfigure(4, minsize=1, weight=2)
    mainwindow.columnconfigure(5, minsize=1, weight=2)
    mainwindow.columnconfigure(6, minsize=1, weight=20) # this is just for aesthetics

    
########################################
#   main window first column
########################################

# head
    label_head_1 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Qtile dirty little helper")
    label_head_1.grid(row = 0, column = 1, columnspan = 1, sticky = "NW")

    label_head_2 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "ALPHA VERSION.")
    label_head_2.grid(row = 0, column = 2, columnspan = 2, sticky = "NW")


# barsize
    label_barsize = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Bar size:")
    label_barsize.grid(row = 5, column = 1, columnspan = 1, sticky = "NW")

    entry_1 = tk.Entry(mainwindow, textvariable = entry_1_var)
    entry_1.insert(END, "24")
    entry_1.grid(row = 5, column = 2, columnspan = 1, sticky = "NW")


# textsize
    label_textsize = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Font size:")
    label_textsize.grid(row = 6, column = 1, columnspan = 1, sticky = "NW")

    entry_2 = tk.Entry(mainwindow, textvariable = entry_2_var)
    entry_2.insert(END, "12")
    entry_2.grid(row = 6, column = 2, columnspan = 1, sticky = "NW")


# gapsize / margin
    label_gapsize = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Window gapsize:")
    label_gapsize.grid(row = 7, column = 1, columnspan = 1, sticky = "NW")

    entry_3 = tk.Entry(mainwindow, textvariable = entry_3_var)
    entry_3.insert(END, "12")
    entry_3.grid(row = 7, column = 2, columnspan = 1, sticky = "NW")


# spacer
    label_spacer1 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "")
    label_spacer1.grid(row = 8, column = 1, columnspan = 2, sticky = "NW")


# wallpaper
    label_wallpaper = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Wallpaper:")
    label_wallpaper.grid(row = 9, column = 1, columnspan = 1, sticky = "NW")

    button_wallpaper = tk.Button(mainwindow, text = "Choose Wallpaper", command = wallpaper_path)
    button_wallpaper.grid(row = 9, column = 2, columnspan = 1, sticky = "NW")


# wallpaper options
    label_wallpaper2 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Wallpaper mode:")
    label_wallpaper2.grid(row = 10, column = 1, columnspan = 1, sticky = "NW")

    wallpaper_options = ["none", "fill", "stretch"]
    list_1_var.set(wallpaper_options[1])
    list_1 = tk.OptionMenu(mainwindow, list_1_var, *wallpaper_options)
    list_1.config(width=10)
    list_1.grid(row = 10, column = 2, columnspan = 1, sticky = "NW")


# spacer
    label_spacer2 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "")
    label_spacer2.grid(row = 11, column = 1, columnspan = 2, sticky = "NW")
    

# bar position
    label_barpos = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Bar position (unavailable!):")
    label_barpos.grid(row = 12, column = 1, columnspan = 1, sticky = "NW")

    barpos_options = ["top", "bottom"]
    list_barpos_var.set(barpos_options[1])
    list_barpos = tk.OptionMenu(mainwindow, list_barpos_var, *barpos_options)
    list_barpos.config(width=10)
    list_barpos.grid(row = 12, column = 2, columnspan = 1, sticky = "NW")


# panelcolor
    label_paco = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Bar color:")
    label_paco.grid(row = 13, column = 1, columnspan = 1, sticky = "NW")

    button_paco = tk.Button(mainwindow, text = "Choose color", command = barcolor)
    button_paco.grid(row = 13, column = 2, columnspan = 1, sticky = "NW")


# accent color
    label_acco = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Accent color:")
    label_acco.grid(row = 14, column = 1, columnspan = 1, sticky = "NW")

    button_acco = tk.Button(mainwindow, text = "Choose color", command = accentcolor)
    button_acco.grid(row = 14, column = 2, columnspan = 1, sticky = "NW")


# text color
    label_teco = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Text color:")
    label_teco.grid(row = 15, column = 1, columnspan = 1, sticky = "NW")

    button_teco = tk.Button(mainwindow, text = "Choose color", command = textcolor)
    button_teco.grid(row = 15, column = 2, columnspan = 1, sticky = "NW")


# spacer (i dont think this is necessary)
    label_spacer3 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "")
    label_spacer3.grid(row = 16, column = 1, columnspan = 1, sticky = "NW")

# keyboard layout
    label_keyboardlayout = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Keyboard Layout:")
    label_keyboardlayout.grid(row = 17, column = 1, columnspan = 1, sticky = "NW")

    keyboardlayout = ["setxkbmap -layout de", "setxkbmap -layout us", "setxkbmap -layout fr"]
    list_2_var.set(keyboardlayout[1])
    list_2 = tk.OptionMenu(mainwindow, list_2_var, *keyboardlayout)
    list_2.config(width=16)
    list_2.grid(row = 17, column = 2, columnspan = 1, sticky = "NW")


########################################
#   main window second column
########################################

# the following spacers are for cosmetics only    
# spacer column
    label_spacer4 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer4.grid(row = 5, column = 3, columnspan = 1, sticky = "NW")  
# spacer column
    label_spacer5 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer5.grid(row = 6, column = 3, columnspan = 1, sticky = "NW")   
# spacer column
    label_spacer6 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer6.grid(row = 7, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer7 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer7.grid(row = 8, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer8 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer8.grid(row = 9, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer9 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer9.grid(row = 10, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer10 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer10.grid(row = 11, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer11 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer11.grid(row = 12, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer12 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer12.grid(row = 13, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer13 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer13.grid(row = 14, column = 3, columnspan = 1, sticky = "NW")
# spacer column
    label_spacer14 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "   |   ")
    label_spacer14.grid(row = 15, column = 3, columnspan = 1, sticky = "NW")
    
    
########################################
#   main window third column
########################################

# autostart
    #open(str(home) + "/.config/qtile/autostart.sh", "x")
    with open((str(home)) + "/.config/qtile/autostart.sh") as f:
        contents = f.read().splitlines()
    print(contents)

    label_as_1 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Add software to autostart here. The '&' is important! (for now)")
    label_as_1.grid(row = 3, column = 4, columnspan = 3, sticky = "NW")

##first entry
    label_as_1 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Autostart #1:")
    label_as_1.grid(row = 5, column = 4, columnspan = 1, sticky = "NW")

    entry_as1 = tk.Entry(mainwindow, textvariable = entry_as1_var)
    entry_as1.insert(END, contents[1])
    entry_as1.grid(row = 5, column = 5, columnspan = 1, sticky = "NW")

##second entry
    label_as_2 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Autostart #2:")
    label_as_2.grid(row = 6, column = 4, columnspan = 1, sticky = "NW")

    entry_as2 = tk.Entry(mainwindow, textvariable = entry_as2_var)
    entry_as2.insert(END, contents[2])
    entry_as2.grid(row = 6, column = 5, columnspan = 1, sticky = "NW")

##third entry
    label_as_3 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Autostart #3:")
    label_as_3.grid(row = 7, column = 4, columnspan = 1, sticky = "NW")

    entry_as3 = tk.Entry(mainwindow, textvariable = entry_as3_var)
    entry_as3.insert(END, contents[3])
    entry_as3.grid(row = 7, column = 5, columnspan = 1, sticky = "NW")

##fourth entry
    label_as_4 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Autostart #4:")
    label_as_4.grid(row = 8, column = 4, columnspan = 1, sticky = "NW")

    entry_as4 = tk.Entry(mainwindow, textvariable = entry_as4_var)
    entry_as4.insert(END, contents[4])
    entry_as4.grid(row = 8, column = 5, columnspan = 1, sticky = "NW")

##fifth entry
    label_as_5 = tk.Label(mainwindow, pady = setpady, padx = setpadx, text = "Autostart #5:")
    label_as_5.grid(row = 9, column = 4, columnspan = 1, sticky = "NW")

    entry_as5 = tk.Entry(mainwindow, textvariable = entry_as5_var)
    entry_as5.insert(END, contents[5])
    entry_as5.grid(row = 9, column = 5, columnspan = 1, sticky = "NW")

    
########################################
#   main window bottom
########################################

# bottom / buttons
    button_prime = tk.Button(mainwindow, text = "Apply", command = prime_config)
    button_prime.grid(row = 19, column = 1, columnspan = 1, sticky = "EW")

    button_quit = tk.Button(mainwindow, text = "Quit", command = quit)
    button_quit.grid(row = 20, column = 1, columnspan = 1, sticky = "EW")


def Call_quit():
    mainwindow.destroy()



Mainwindow()
mainwindow.mainloop()


#I cant believe this is working ...
