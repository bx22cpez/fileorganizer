import os
import shutil

#os.system("date")



#os.mkdir("C:/mynewfolder")


#print (os.getcwd())


# isexist=os.path.exists("C:/Mono")
# print (isexist)

# rootext=os.path.splitext("path C:/mynewfolder/XD.jpg")
# print (rootext[1])
source="C:/mynewfolder/XD.jpg"
dest="C:/pic/XD.jpg"
shutil.copy(source,dest)



source="C:/mynewfolder/attachment.png"
dest="C:/pic/attachment.png"
shutil.move(source,dest)