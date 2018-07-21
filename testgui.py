#!/usr/bin/env python

import tkinter
from tkinter import *

#definitions for the fucking shit
username = tkinter.Tk()
#coding for widgets (buttons etc)

usrtx = Label(username, text="User Name:")
usrtx.pack( side = LEFT)

usere = Entry(username, bd =2)
usere.pack(side = LEFT)

username.mainloop()