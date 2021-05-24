import os
from shutil import copyfile

# You only need to change this line to your dataset download path
download_path = '../PKUSketchRE-ID_V1'

if not os.path.isdir(download_path):
    print('please change the download_path')

save_path = download_path + '/pytorch'
if not os.path.isdir(save_path):
    os.mkdir(save_path)

#---------------------------------------
#train_all
train_path = download_path + '/photo'
train_save_path = download_path + '/pytorch/train_all_photos'
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = train_path + '/' + name
        dst_path = train_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)


#---------------------------------------
#train_val
train_path = download_path + '/photo'
train_save_path = download_path + '/pytorch/train_photos'
val_save_path = download_path + '/pytorch/val_photos'
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)
    os.mkdir(val_save_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = train_path + '/' + name
        dst_path = train_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
            dst_path = val_save_path + '/' + ID[0]  #first image is used as val image
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)
