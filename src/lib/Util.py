import os
from PIL import Image
import time
import datetime

def hell():
    return "Hello Hell Wordl"

def getAllFiles(path, recursive=True, types=[], excludeDir=[]):
    files = []
    Filter=False
    if len(types) > 0:
        Filter = True

    for root, dirs, filenames in os.walk(path, topdown=True):
        [dirs.remove(d) for d in list(dirs) if d in excludeDir]
        for filename in filenames:
            if Filter:
                ext = filename.split('.')[-1]
                if ext.lower() in types:
                    files.append({'type': ext.lower(), 'file': os.path.join(root, filename)})
            else:
                files.append({'type': None, 'file': os.path.join(root, filename)})

    return files

def getImageDate(img):
    dt = None
    try:
        dsting=Image.open(img)._getexif()[36867]
        dt = datetime.datetime.strptime(dsting, "%Y:%m:%d %H:%M:%S").date()
    except:
        pass

    if dt == None:
        dt = datetime.datetime.fromtimestamp(os.path.getmtime(img))

    return dt

def getVideoDate(img):
    dt = None
    try:
        dt = datetime.datetime.fromtimestamp(os.path.getmtime(img))
    except:
        pass

    return dt