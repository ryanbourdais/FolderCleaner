
import os
import glob
import time
import sys 
import datetime
import logging

def FileDeleter():
    print("What Folder would you like to clean up? ")
    file_path = input("Input D for Downloads, R for Recycle Bin, T for Temp folder ")
    if file_path == "R":
        path = 'Recycle Bin'
        path_name = 'C:\$Recycle.Bin\%S-1-5-21-133842441-3379276907-3848524732-1001%'
    if file_path == "D":
        path = 'C:/Users/Bourdais/Downloads'
        path_name = 'Downloads'
    if file_path == "T":
        path = 'C:/windows/temp'
        path_name = 'Temp'
    # end of conditionals

    os.chdir(path)

    for filename in glob.glob('*'):
        filename = os.path.join(path, filename)
        mod_date = datetime.date.fromtimestamp(os.stat(filename).st_mtime)
        if mod_date < (datetime.date.today() - datetime.timedelta(days=1)):
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
            except:
                pass
    print("All items older than 24 hours have been Cleared from the {} Directory ".format(path_name))
FileDeleter()
