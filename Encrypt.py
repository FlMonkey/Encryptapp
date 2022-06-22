import os
from cryptography.fernet import Fernet


#creates list that will be used to know what to encrypt
myfile = open("usrinput.txt")
folder = myfile.read()
myfile.close()

#defining the directory we want

direc = os.listdir(folder)


key = Fernet.generate_key()
    

os.chdir(folder)

for file in direc:
    if file == "Encrypt.py":
        direc.remove("Encrypt.py")
    if file == "README.md":
        direc.remove("README.md")     
    if file == "Decrypt.py":
        direc.remove("Decrypt.py")       
    if file == "gitignore":
        direc.remove("gitignore") 

listlen = len(direc)
listcheck = 0
for file in direc:
    if file == "cryptkey.key":
        input("it seems that you already have a key would you like to use it? (y/n)")
        if input == "y":
            with open("cryptkey.key", "wb") as cryptkey:
                cryptkey.write(key)                
            continue
        if input == "n":
            delete = input("would you like to delete the key and create a new one? (y/n)")
            if delete == "y":
                with open("cryptkey.key", "wb") as cryptkey:
                    cryptkey.write(key)                
                continue
            if delete == "n":
                exit()
    if file != "cryptkey.key":
        listcheck += 1
        if listcheck == listlen:
            print("it apears you have do not have a key, ome will be generated for you")
            with open("cryptkey.key", "wb") as cryptkey:
                cryptkey.write(key)
            continue



direc.remove("cryptkey.key")
    
    
for file in direc:
    print(file)
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("encrypted succesfully")
