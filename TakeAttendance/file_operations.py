import os
import shutil


def read(path):
    with open(path, "rb") as file:
        data = file.read()

    return data


def write(path, data):
    with open(path, "wb") as file:
        file.write(data)


def open_dir(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def clearDir(path):
    shutil.rmtree(path)
    open_dir(path)


def renameFile(src, dst):
    try:
        os.rename(src, dst)
    except (FileNotFoundError, FileExistsError):
        pass


def convertPath(path):
    counter = 0
    path = list(path)  # change to mutable type
    while counter < len(path):
        if path[counter] == "\\":
            path[counter] = "/"
        counter += 1

    path = "".join(path)  # again convert to string

    return path


def getDirectoryName(dir):
    dir = convertPath(dir)
    return dir.split("/")[-1]


def getRootName(dir):
    dir = convertPath(dir)
    return dir.split("/")[0]


# get directories from path, if directory in the path
def getDirecoryFromPath(path, dirName):
    path = convertPath(path)

    p = path.split("/")

    dir = ""
    counter = 0
    for i in p:
        if dirName == i:
            dir = "/".join(p[counter:])
        else:
            counter += 1

    return dir
