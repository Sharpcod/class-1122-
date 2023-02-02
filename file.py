import os
import shutil
from_dir="C:\\Users\\shrey\\Downloads"
to_dir="C:\\Users\\shrey\\OneDrive\\Desktop\\IMAGES DOWNLOAD"
list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpeg','.jpg','.jfif']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+'Images'
        path3=to_dir+'/'+'Images'+'/'+file_name


        if os.path.exists(path2):
            print('moving'+file_name+'.....')
            shutil.move(path1,path3)
        else:
            print('Folder does not exist. So creating it.....')
            os.makedirs(path2)
            print('moving'+file_name+'.....')
            shutil.move(path1,path3)

