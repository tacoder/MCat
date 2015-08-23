def getyn():
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    while True:
        choice = raw_input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")

from os import listdir
from os.path import isfile, join
def getFileListRecursively(rootFolderPath):
    folders = []
    files = []
    folders.append(rootFolderPath)
    while(len(folders)>0):
        curPath = folders.pop()
        folderContents = listdir(curPath)
        for f in folderContents:
            if isfile(join(curPath,f)):
                files.append(join(curPath,f))
            else:
                folders.append(join(curPath,f))
    return files

import re
import os

def filterFilesByFormat(listOfFiles):
    pattern = re.compile("\\.\\w+$")
    try:
        desirablef = open(".mediaFormats","r+w")
    except IOError:
        desirablef = open(".mediaFormats","w+")
    try:
        undesirablef = open(".ignoredFormats","r+w")
    except IOError:
        undesirablef = open(".ignoredFormats","w+")

    desirable = desirablef.read().split("\n")
    undesirable = undesirablef.read().split("\n")
    desirablef.seek(0,os.SEEK_END)
    undesirablef.seek(0,os.SEEK_END)
    toReturn = []
    for f in listOfFiles:
        #get file extension::
        ext = pattern.findall(f)[0]
        #see if file extension is desirable?
        if ext in desirable:
            toReturn.append(f)
            continue
        elif ext in undesirable:
            continue
        else:
            print "Unknown file format:"+ext
            print "Is it desirable?"
            if getyn():
                desirablef.write("\n"+ext)
                desirable.append(ext)
                toReturn.append(f)
            else:
                undesirablef.write("\n"+ext)
                desirable.append(ext)
    return toReturn
