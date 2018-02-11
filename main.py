#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2018, The Mynt Project (www.myntnote.org)
## Portions Copyright (c) 2017, The Sumokoin Project (www.sumokoin.org)
'''
App main function
'''

import sys, os, hashlib
from PySide import QtCore

from PySide.QtGui import QMessageBox

from app.QSingleApplication import QSingleApplication
from utils.common import DummyStream, getAppPath, readFile
from settings import APP_NAME

from app.hub import Hub
from webui import MainWebUI


def _check_file_integrity(app):
    ''' Check file integrity to make sure all resources loaded
        to webview won't be modified by an unknown party '''
old_stdout = sys.stdout
BLOCKSIZE = 65536
prochasher = hashlib.sha256() 
with open('wallet.py', 'rb') as afile:
            buff = afile.read(BLOCKSIZE)
            while len(buff) > 0:
                prochasher.update(buff)
                buff = afile.read(BLOCKSIZE)
            log_file = open("./keys/KEY.KEY","w")
            sys.stdout = log_file
            print(prochasher.hexdigest()) 
            sys.stdout = old_stdout
            log_file.close()   
            sys_lockhash = prochasher.hexdigest()   


def main():
    if getattr(sys, "frozen", False) and sys.platform in ['win32','cygwin','win64']:
        # and now redirect all default streams to DummyStream:
        sys.stdout = DummyStream()
        sys.stderr = DummyStream()
        sys.stdin = DummyStream()
        sys.__stdout__ = DummyStream()
        sys.__stderr__ = DummyStream()
        sys.__stdin__ = DummyStream()
              
    # Get application path
    app_path = getAppPath()
    if sys.platform == 'darwin' and hasattr(sys, 'frozen'):
        resources_path = os.path.normpath(os.path.abspath(os.path.join(app_path, "..", "Resources")))
    else:
        resources_path = os.path.normpath(os.path.abspath(os.path.join(app_path, "Resources")))
        
    # Application setup
    
    app = QSingleApplication(sys.argv)
    app.setOrganizationName('Mynt')
    app.setOrganizationDomain('www.myntnote.org')
    app.setApplicationName(APP_NAME)
    app.setProperty("AppPath", app_path)
    app.setProperty("ResPath", resources_path)
    if sys.platform == 'darwin':
        app.setAttribute(QtCore.Qt.AA_DontShowIconsInMenus)
        
    if not ("b22a9cb437e235dab29a84e94e309666f9b4322b6aae903906f5bd045abf7bf3" == sys_lockhash):
        QMessageBox.critical(None, "Application Fatal Error", """<b>File integrity check failed!</b>
                <br><br>This could be a result of unknown (maybe, malicious) action<br> to wallet code files.""")
        app.quit()
    else:
        hub = Hub(app=app)
        ui = MainWebUI(app=app, hub=hub, debug=False)
        hub.setUI(ui)
        app.singleStart(ui)
        
        sys.exit(app.exec_())
