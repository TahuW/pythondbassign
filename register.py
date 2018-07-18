regname = input("Enter requested username: ")

currusers = open("users.txt", "r+")
usernamelist = currusers.read()

while(regname in usernamelist):
	regname = input("Username already taken, choose a different one: ")

if(regname not in usernamelist):
	currusers.write(regname + "\n")
	newpasswd = open(regname + "passwd.txt", "w+")
newusrpass = input("Enter your password: ")
newpasswd.write(newusrpass + "\n")
newpasswd.close()
currusers.close()