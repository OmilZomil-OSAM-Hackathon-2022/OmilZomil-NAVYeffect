import os
path = '../image/res/fd_2'

diff_n = 320


for (root, dirs, files) in os.walk(path):
    for file_name in files:
        src_file_path = os.path.join(root, file_name)

        dst_n = int(file_name.split('.')[0]) + diff_n
        dst_file_name = f'{dst_n}.jpg'

        dst_file_path = os.path.join(root, dst_file_name)

        os.rename(src_file_path, dst_file_path)