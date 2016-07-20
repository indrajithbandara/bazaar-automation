#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
 
files=[r for r in open("test.txt") if os.path.isfile(r.strip())]
dirs=[r for r in open("test.txt") if os.path.isdir(r.strip())]
 
with open("11.txt","w+") as f:
    f.writelines(files)
 
with open("22.txt","w+") as f:
    f.writelines(dirs)
