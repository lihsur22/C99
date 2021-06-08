import os
import shutil

'''
source = "text.txt"
destination = "b.txt"
dest = shutil.copy(source,destination)

path = "C:/Users/Rushil/Desktop/code/python/class/99"
print(os.listdir(path))

src1 = "C:/Users/Rushil/Desktop"
dest1 = "C:/Users/Rushil/Desktop/code/python/class/99/evening.ogg"
shutil.move(dest1,src1)
'''

source = input("Enter name of directory to  be sorted : ")
files = os.listdir(source)
for file in files:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "" :
        continue
    if os.path.exists(source + '/' + ext):
        shutil.move(source+'/'+file, source+'/'+ext+'/'+file)
    else:
        os.makedirs(source+'/'+ext)
        shutil.move(source+'/'+file, source+'/'+ext+'/'+file)

source1= "C:/Users/Rushil/Desktop/code/python/class/98"
dest = input("Enter folder name to put backup in : ")

source1 = source1 + '/'
dest = dest +  '/'

list_of_files = os.listdir(source1)

for file in list_of_files:
    shutil.copy((source1+file),dest)