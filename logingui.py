from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk

import os 

path = "/'python database assignment'/"

users = open("users.txt", "w+")
userlist = users.read()

class LoginFrame(Frame):
	def __init__(self, master):

		#code for buttons and labels
		
		super().__init__(master)

		self.label_username = Label(self, text="Username: ")
		self.label_password = Label(self, text="Password: ")
		


		self.entry_username = Entry(self)
		self.entry_password = Entry(self)

		self.label_username.grid(row=0, sticky=E)
		self.label_password.grid(row=1, sticky=E)

		self.entry_username.grid(row=0, column=1)
		self.entry_password.grid(row=1, column=1)
		
		self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
		self.logbtn.grid(columnspan=2)
		
		
		self.regbtn = Button(self, text="Register these credentials", command=self._register_btn_clicked)
		self.regbtn.grid(columnspan=2)
		self.label_version = Label(self, text="VERSION 1.2")
		self.label_version.grid(row=4, sticky=E, column=1)
		self.pack()

	def _login_btn_clicked(self):

		#user login system, used for logging into the account after checking credentials

		username = self.entry_username.get()

		passwd = open(username + "passwd.txt", "r+")
		passwdlist = passwd.read()
		password = self.entry_password.get()

		#credential check and final login
		if username in userlist and password in passwdlist:
			tm.showinfo("Login info", "Welcome, " + username + ". You have been successully logged in")
		else:
			tm.showerror("Login error", "Login failed, if the account is just registered, restart the program and try again")
	def _register_btn_clicked(self):
		#user registration system
		newusrnm = open("users.txt", "r+")
		currentusers = newusrnm.read()
		newuser = self.entry_username.get()

		if newuser in currentusers:
		#if the username is already in use, display an error
			tm.showerror("Registration error", "Registration failed, username already in use.")
		else:	
			#if the username is not in use, register it to a new file
			newusrnm.write(newuser + "\n")
			newregpasswd = open(newuser + "passwd.txt", "w+")
			newpasswd = self.entry_password.get()
			newregpasswd.write(newpasswd)
			newusrnm.close()
			newregpasswd.close()
			


root = Tk()
lf = LoginFrame(root)
root.mainloop()
passwd.close()
users.close