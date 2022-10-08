import os
import shutil


path=input("enter the name of your folder to be sorted -")
listoffiles=os.listdir(path)

for file in listoffiles:
    name,ext=os.path.splitext(file)
    ext=ext[1]
    print (ext)
    if ext=="":
        continue
    
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.makedirs(path + "/" +ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)