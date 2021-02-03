### 한 사람당 샘플 데이터 수 20장 이상인 사람 수 check

import os
import shutil
import distutils.dir_util

os.chdir('C:/Users/kheed/Desktop/GraduationProject/Data0/lfw')
print(os.getcwd())
path = os.getcwd()
os.chmod(path, 0o444)
morethan20 = 0

for (path, dir, files) in os.walk(path):
    if len(files) >= 20:
        morethan20+=1
        shutil.move(path, "../../Data0_20up")

print(morethan20)