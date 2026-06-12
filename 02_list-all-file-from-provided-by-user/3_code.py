import os

try:
    Folder=input("Enter Folder Name With Space Between: ").split()
    for i in Folder:
        files=os.listdir(i)
        print(files)

    for file in files:
        print(file)

except FileNotFoundError:
    print("not found")

#python code.py
#input=01_Basic