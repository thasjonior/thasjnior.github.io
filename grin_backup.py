import os
import pprint
import platform
#  get all files in directory
#  sort by size 
#  write text file showing file asending order
def SortDir ():
    return entry.is_file()
    
def CreateFile(Path):
    DirList=Path.split('/')
    l=len(DirList)
    return open("{}/{}".format(Path,DirList[l-1]),'w')

def GetSize(entry):
    size= entry.stat().st_size
    if size <= 1024 :
        return "{}bytes".format(size)
    elif size <= 1024000:
        return "{:.2f}KB".format(size/ 1024)
    elif size <= 1024000000:
        return "{:.2f}MB".format(size/1024000)
    else:
        return "{:.2f}GB".format(size/1024000000)

def comparator (entry):
    return entry.stat().st_size  

def DeleteFile (Path):

    Filename=Path.split('/')[len(Path.split('/'))-1]
    Filepath="{}/{}".format(Path,Filename) 
    if bool(Filepath):
        os.remove(Filepath)
        print("File deleted")
    else:
       CreateFile(Path)
       DeleteFile(Path)

 
def GetFile (Path):
    File=CreateFile(Path)
    
    for entry in sorted(os.scandir(Path),key= comparator):
        if entry.is_file():
            pass
            #File.write("FileName:{}    FileSize:{}\n".format(entry.name.upper(),GetSize(entry)))
        elif entry.is_dir():
            DeleteFile(Path)
            pprint.pprint("SubFolder:{}".format(entry.name.upper()))
            GetFile(entry.path)

        else:
            print("UNKNOWN")
GetFile(r'/home/judethaddeus/Documents')