import os
import sys


DUMMY_DIR = 'dummy_backup'
MAP_DIR = 'small.sav'
DEFAULT_DUMMY = '-1,0'


def validate_input(x, y):
    fname = f'spawnnull{x},{y}'
    if os.path.exists(os.path.join(MAP_DIR, fname)):
        raise ValueError(f'{fname} already exist')


def copy_file(src, dest):
    src_path = os.path.join(DUMMY_DIR, src)
    dest_path = os.path.join(MAP_DIR, dest)

    os.system(f'cp "{src_path}" "{dest_path}"')


def copy_files(x, y):
    os_name = f'spawnnull{DEFAULT_DUMMY}'
    oj_name = f'map{DEFAULT_DUMMY}.png'
    om_name = f'map{DEFAULT_DUMMY}'

    s_name = f'spawnnull{x},{y}'
    j_name = f'map{x},{y}.png'
    m_name = f'map{x},{y}'

    copy_file(os_name, s_name)
    copy_file(oj_name, j_name)
    copy_file(om_name, m_name)


def main():
    args = sys.argv
    if len(args) < 3:
        print(f'Usage: python3 {args[0]} <x> <y>')
        sys.exit(1)

    x = args[1]
    y = args[2]
    force = False
    if len(args) >= 4 and args[3].lower() == 'force':
        force = True
    print(f'Your input x: {x}, y: {y}, force: {force}\n')

    if not force:
        validate_input(x, y)
    copy_files(x, y)


if __name__ == '__main__':
    main()
