import os
from cryptography.fernet import Fernet

finalenc = []
#creates list that will be used to know what to encrypt

folder = str(input("enter path for your folder here"))
#defining the directory we want

direc = os.listdir(folder)
#sets the list of files as a varialbe

os.chdir(folder)

for file in direc:
    if file == "Encrypt.py":
        direc.remove("Encrypt.py")
    if file == "README.md":
        direc.remove("README.md")     
    if file == "Decrypt.py":
        direc.remove("Decrypt.py")  
    if file == "cryptkey.key":
        direc.remove("cryptkey.key")     
    if file == "gitignore":
        direc.remove("gitignore") 


print(direc)

with open("cryptkey.key", "rb") as key:
    secretkey = key.read()

sphrase = "decryptme"
password = input("Enter password to decrypt")

if sphrase == password:
    for file in direc:
        print(file)
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("dubz it got decrypted")
else:
    print("better luck next time bozo")