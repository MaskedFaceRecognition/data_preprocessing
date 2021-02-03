#### 결손 자료 검색


import os


os.chdir('C:/Users/kheed/Desktop/GraduationProject/cutAndMasking/nonMaskedOutput/train')
count = 0
idx = 0
for (path, dir, files) in os.walk(os.getcwd()):
    if len(files) == 0:
        count+=1
        print(path)
        print(files)
        #shutil.copy("path", "../test3.txt")
    idx += 1

print(count)
