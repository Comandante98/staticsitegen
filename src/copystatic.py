import os
import shutil

def copy(source, destination, first=True):
    if os.path.exists(destination) and first:
        shutil.rmtree(destination)
    first = False
    os.mkdir(destination)
    files = os.listdir(source)
    for f in files:
        joined = os.path.join(source, f)
        if os.path.isfile(joined):
            shutil.copy(joined, destination)
        else:
            copy(joined, os.path.join(destination, f), False)

        

