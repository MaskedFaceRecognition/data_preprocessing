
import os
import shutil

#for path, direct, files in os.walk("C:/Users/kheed/Desktop/GraduationProject/Data/lfw"):
#    print(path)
#    print(direct)
#    print(files)

#print(os.getcwd())
os.chdir('C:/Users/kheed/Desktop/GraduationProject/Data/lfw')
print(os.getcwd())

for (path, dir, files) in os.walk(os.getcwd()):
    if len(files) >= 5:
        shutil.move(path, 'C:/Users/kheed/Desktop/GraduationProject/Data')




