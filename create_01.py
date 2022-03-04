import os

DUMMY_DIR = 'dummy_backup'
MAP_DIR = 'small.sav'
DEFAULT_DUMMY = '-1,0'
TARGET_LOC = '0,1'


def copy_file(src, dest):
    src_path = os.path.join(DUMMY_DIR, src)
    dest_path = os.path.join(MAP_DIR, dest)

    os.system(f'cp "{src_path}" "{dest_path}"')


def copy_files():
    os_name = f'spawnnull{DEFAULT_DUMMY}'
    oj_name = f'map{DEFAULT_DUMMY}.png'
    om_name = f'map{DEFAULT_DUMMY}'

    s_name = f'spawnnull{TARGET_LOC}'
    j_name = f'map{TARGET_LOC}.png'
    m_name = f'map{TARGET_LOC}'

    copy_file(os_name, s_name)
    copy_file(oj_name, j_name)
    copy_file(om_name, m_name)


def main():
    copy_files()


if __name__ == '__main__':
    main()
