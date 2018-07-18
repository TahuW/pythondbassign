usersfile = open("users.txt", "r")
#passfile = open("passwds.txt", "r")

userslist = usersfile.read();
#passwdlist = passfile.read();
user = input("Enter your username: ")

while(user not in userslist):
    print("Username false, please try again.")
    user = input("Enter your username: ")
passfile = open(user +"passwd.txt")
passwdlist = passfile.read();

print("Username correct, please enter your password")
passwd = input("Enter your password: ")

while(passwd not in passwdlist):
    print("Password is incorrect, try again")
    passwd = input("Enter your password: ")

print("Successfully logged in. welcome, "+user+"!")
    