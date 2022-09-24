import hashlib
import os
import time
###############

#Clear Screen

os.system("clear")

# Question1

time.sleep(0.5)
y = input("[+] Please select for continue [y/N] ? ")

if y == "y":
    print("")
    print("[!] You can continue !!")
    print("")

else:
    print("")
    print("[!] You can not continue !!")
    print("")
    quit()

# banner

time.sleep(0.5)
os.system("figlet Md5-Hash")

# Inputs

print("")
passwd_hash = input("Enter md5 hash ===> ")
print("")
wordlist = input("Enter Wordlist file ===> ")
flag = 0

# Pass file

try:
    passfile = open(wordlist, "r")
except:
      print("No file found !!")
      quit()
for word in passfile:
    enc = word.encode("utf-8")
    digest = hashlib.md5(enc.strip()).hexdigest()
    if digest == passwd_hash:
        print("")
        print("Password found !!")
        print("")
        print("Password is " + word)
        flag = 1
        break
if flag == 0:
    print("")
    print("Password is not in the list !!")
