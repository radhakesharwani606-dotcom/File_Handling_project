from pathlib import Path
import os                         #it will use for delete operation

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name:-")
        p=Path(name)
        if not p.exists() and p.is_file:
            with open(p,'w') as fs:
                data=input("what you want to write in this file:-")
                fs.write(data)

            print(f"FILE IS CREATED SUCCESSFULLY...")
        else:
            print("this file already exist")
    except Exception as err:
        print(f"an error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name=input("tell the name of file you want to read:-")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
                
            print("FILE IS READED SUCCESSFULLY")
        else:
            print("file do not exsist..")
    except Exception as err:
        print(f"an error occur as {err}")

def updatefile():
    try:
        readfileandfolder()
        name =input("tell which file you want to update")
        p=Path(name)
        if p.exists and p.is_file():
            print("press 1 for changing the name of file")
            print("press 2 for overwrite the data")
            print("press 3 for appending a file")
            res= int(input("enter the response:-"))
            if res ==1:
                name2=input("tell your new file name:-")
                p2=Path(name2)
                p.rename(p2)
            if res==2:
                with open(p,'w') as fs:
                    data=input("tell what you want to write in the file:-")
                    fs.write(data)  
            if res==3:
                with open(p,'a') as fs:
                    data=input("tell what you want to append in the file:-")
                    fs.write(data) 
    except Exception as err:
        print(f"an error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name=input("which file you want to delete:-")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY..")
        else:
            print("no such file exist")
    except Exception as err:
        print(f"en error occured as {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for  updating a file")
print("press 4 for deleting a file")

check = int(input("tell your response:-"))


if check ==1:
    createfile()

elif check ==2:
    readfile()

elif check==3:
    updatefile()

elif check ==4:
    deletefile()