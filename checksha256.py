#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2018, The Mynt Project (www.myntnote.org)
'''
App boostrap
'''
from main import main
import hashlib, os, sys
old_stdout = sys.stdout
BLOCKSIZE = 65536
keyhasher = hashlib.sha256()
def checkmain():
	with open('main.py', 'rb') as afile:
            buff = afile.read(BLOCKSIZE)
            while len(buff) > 0:
                keyhasher.update(buff)
                buff = afile.read(BLOCKSIZE)
            log_file = open("./keys/MAIN.KEY","w")
            sys.stdout = log_file
            print(keyhasher.hexdigest()) 
            sys.stdout = old_stdout
            log_file.close()   
            sys_lockhash = keyhasher.hexdigest()
            if not ("aeff03972fefb3f981bfae14b6208f34d73fd7165a7ec8bed4acdbef03daf9a9" == sys_lockhash):
            	print("Application Fatal Error. File integrity check failed! This could be a result of unknown (maybe, malicious) action to wallet code files. ")
            	app.quit()
            else:
            	print("MAIN SHA256 checks succeeded")
 