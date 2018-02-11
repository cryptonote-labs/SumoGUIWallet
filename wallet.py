#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2018, The Mynt Project (www.myntnote.org)
## Portions Copyright (c) 2017, The Sumokoin Project (www.sumokoin.org)
'''
App boostrap
'''

from main import main
import hashlib, os, sys
from checksha256 import checkmain
old_stdout = sys.stdout
BLOCKSIZE = 65536
StartValue = 0
Limit = 3
AddValue = 1
Counter = StartValue
apphasher = hashlib.sha256()
manhasher = hashlib.sha256()
reshasher = hashlib.sha256()  
for root, directories, filenames in os.walk('./app/'):
         for filename in filenames: 
                 # print(os.path.join(root,filename))
                 with open(os.path.join(root,filename), 'rb') as afile:
                    buf1 = afile.read(BLOCKSIZE)
                    while len(buf1) > 0:
                        apphasher.update(buf1)
                        buf1 = afile.read(BLOCKSIZE)
                    log_file = open("./keys/APP.KEY","w")
                    sys.stdout = log_file
                    print(apphasher.hexdigest()) 
                    sys.stdout = old_stdout
                    log_file.close()
for root, directories, filenames in os.walk('./manager/'):
         for filename in filenames: 
                 # print(os.path.join(root,filename))
                 with open(os.path.join(root,filename), 'rb') as afile:
                    buf2 = afile.read(BLOCKSIZE)
                    while len(buf2) > 0:
                        manhasher.update(buf2)
                        buf2 = afile.read(BLOCKSIZE)
                    log_file = open("./keys/MANAGER.KEY","w")
                    sys.stdout = log_file
                    print(manhasher.hexdigest()) 
                    sys.stdout = old_stdout
                    log_file.close()
for root, directories, filenames in os.walk('./Resources/'):
         for filename in filenames: 
                 # print(os.path.join(root,filename))
                 with open(os.path.join(root,filename), 'rb') as afile:
                    buf3 = afile.read(BLOCKSIZE)
                    while len(buf3) > 0:
                        reshasher.update(buf3)
                        buf3 = afile.read(BLOCKSIZE)
                    log_file = open("./keys/RESOURCES.KEY","w")
                    sys.stdout = log_file
                    print(reshasher.hexdigest()) 
                    sys.stdout = old_stdout
                    log_file.close()
if not ("b99fbff76e6c266a72e9a6054b9fe79f73c65f1e0f789d79bfb5acdbdd8cbfc6" == apphasher.hexdigest()):
	print("APP Not SHA256 Verified")
if not ("1eccf9bc1a830e9b81f4014ceb8280c8ac8eaddbd4449f6e13136132bc94bc35" == manhasher.hexdigest()):
	print("MANAGER Not SHA256 Verified")
if not ("4226811bf4615e939531ca983263f37d7777edf3804d509660cd51f4667a82e0" == reshasher.hexdigest()):
	print("RESOURCES Not SHA256 Verified")
if ("b99fbff76e6c266a72e9a6054b9fe79f73c65f1e0f789d79bfb5acdbdd8cbfc6" == apphasher.hexdigest()):
	print("APP Verified by SHA256")
	print("Adding {} to Passed Checks.".format(AddValue))
	Counter = Counter + AddValue
if ("4226811bf4615e939531ca983263f37d7777edf3804d509660cd51f4667a82e0" == reshasher.hexdigest()):
	print("RESOURCES Verified by SHA256")
	print("Adding {} to Passed Checks.".format(AddValue))
	Counter = Counter + AddValue
if ("1eccf9bc1a830e9b81f4014ceb8280c8ac8eaddbd4449f6e13136132bc94bc35" == manhasher.hexdigest()):
	print("MANAGER Verified by SHA256")
	print("Adding {} to Passed Checks.".format(AddValue))
	Counter = Counter + AddValue
while Counter < Limit:
	print("Counter = {}, Limit = {}".format(Counter, Limit))
if Counter == Limit:
	print("SHA256 Checks: {} and Requirements are: {}.".format(Counter, Limit))
	print("Resources have Succeeded Sha256 Checks. Launching Wallet.")
	checkmain()
	main()