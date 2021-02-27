# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 06:15:15 2021
@author: Patrick

Organizes files into directories based on file type 
based on shutil tutorial from a reddit post by Codex Python
"""

import os
import shutil

path = input("Please enter file path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(path+'/'+extension):
        shutil.move(path+ '/'+file, path+'/'+extension+"/"+file)

    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+"/"+file)

