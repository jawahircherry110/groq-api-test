users = {
    "jawahir" : "balti_dev"
}

username = input("enter your username  : ")
password  = input("enter your pasword : ")

if username in users and users[username] ==password:
    print("user successfully login")
else:
    print("invalid username or password")


