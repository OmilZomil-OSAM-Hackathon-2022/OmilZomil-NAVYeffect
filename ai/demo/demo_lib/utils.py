import os
import sys


def setImportPath():
    cur_path = os.getcwd()
    res_path = ''
    path_dir_names = cur_path.split('/')
    for i, path_dir_name in enumerate(path_dir_names[::-1]):
        if path_dir_name == 'AI_BE':
            break
    if i == 0:
        res_path = cur_path
    else:
        res_path = '/'.join(path_dir_names[:-i])

    if res_path not in sys.path:
        sys.path.append(res_path)

    engine_path = os.path.join(res_path, 'OZEngine')
    if engine_path not in sys.path:
        sys.path.append(engine_path)
