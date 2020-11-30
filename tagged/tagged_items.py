from collections import namedtuple
from os import listdir
from os.path import abspath, dirname, join



def get_items_given_path(path: str, name_file: str):
    items = [item for item in sorted(listdir(path))]
    name_file = join(dirname(abspath(__file__)), name_file)
    with open(name_file, 'w') as f:
        for i in items:
            f.write(f'{str(i)}\n')        
    return items

def path_func():
    from os.path import join, abspath
    _path = join('..', 'example_code')
    _path = abspath(_path)
    return _path


if __name__ == '__main__':
    name_f = 'original.txt'
    p = path_func()
    get_items_given_path(p, name_f)