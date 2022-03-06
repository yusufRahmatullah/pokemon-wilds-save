from logging.config import valid_ident
import os
from re import L
import sys

AVAILABLE_COMMANDS = ['update', 'refresh']
DUMMY_DIR = 'dummy_backup'
MAP_DIR = 'small.sav'


def error(msg):
    print(msg)
    sys.exit(1)


def generate_file_path(loc, parent):
    s_path = os.path.join(parent, f'spawnnull{loc}')
    p_path = os.path.join(parent, f'map{loc}.png')
    m_path = os.path.join(parent, f'map{loc}')
    return [s_path, p_path, m_path]


def copy_file(src_path, dest_path):
    os.system(f'cp "{src_path}" "{dest_path}"')


class Argument:
    def __init__(self, command, params) -> None:
        self.command = command
        self.params = params
        self._validate()

    def perform(self):
        error(f'Command {self.command} not perform any action')

    def _validate(self):
        pass


class RefreshArgument(Argument):
    default_target = {
        'main': '0,1'
    }
    valid_locs = {
        'main': '-1,0',
        'regi': '0,-1'
    }

    def __init__(self, command, params) -> None:
        super().__init__(command, params)
        self._init_loc()
        self._init_target()

    def perform(self):
        src_loc = self.valid_locs[self.loc]
        src_paths = generate_file_path(src_loc, DUMMY_DIR)

        dest_loc = self.target
        dest_paths = generate_file_path(dest_loc, MAP_DIR)

        for src, dest in zip(src_paths, dest_paths):
            print(f'will copy file from "{src}" to "{dest}"')
            copy_file(src, dest)

    def _init_loc(self):
        loc = self.params[0].lower()
        if loc not in self.valid_locs:
            error(f'Location should be one of: {" | ".join(self.valid_locs)}')
        self.loc = loc

    def _init_target(self):
        if len(self.params) == 1:
            self.target = self.default_target[self.loc]
            return
        self.target = self.params[1]

    def _validate(self):
        if len(self.params) == 0:
            error('Params should be exist')

class UpdateArgument(Argument):
    valid_locs = {
        'main': '-1,0',
        'regi': '0,-1'
    }

    def __init__(self, command, params) -> None:
        super().__init__(command, params)
        self._init_loc()

    def perform(self):
        src_loc = self.valid_locs[self.loc]
        src_paths = generate_file_path(src_loc, MAP_DIR)

        dest_loc = self.valid_locs[self.loc]
        dest_paths = generate_file_path(dest_loc, DUMMY_DIR)

        for src, dest in zip(src_paths, dest_paths):
            print(f'will copy file from "{src}" to "{dest}"')
            copy_file(src, dest)

    def _init_loc(self):
        loc = self.params[0].lower()
        if loc not in self.valid_locs:
            error(f'Location should be one of: {" | ".join(self.valid_locs)}')
        self.loc = loc

    def _validate(self):
        if len(self.params) == 0:
            error('Params should be exist')


def parse_args() -> Argument:
    argv = sys.argv
    if len(argv) < 2:
        print(f'Usage: python3 {argv[0]} <command>')
        print(f'Available commands: {" | ".join(AVAILABLE_COMMANDS)}')
        sys.exit(1)
    command = argv[1].lower()
    if command not in AVAILABLE_COMMANDS:
        print(f'Unknown command: {command}')
        print(f'Available commands: {" | ".join(AVAILABLE_COMMANDS)}')
    params = argv[2:]
    if command == 'update':
        return UpdateArgument(command, params)
    elif command == 'refresh':
        return RefreshArgument(command, params)
    else:
        return Argument(command, params)


def main():
    arg = parse_args()
    arg.perform()


if __name__ == '__main__':
    main()
