import os
path = './image/full_dress_uniform/person'


for index, file_name in enumerate(os.listdir(path)):
    src_file_path = os.path.join(path, file_name)
    dst_file_path = os.path.join(path, f'{index}.jpg')
    os.rename(src_file_path, dst_file_path)
