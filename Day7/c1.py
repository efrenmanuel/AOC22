from colorama import Fore, Back, Style
import sys



class file:
    name = ""
    size = 0

    def pretty_print(self):
        return "{name_color}{name} {white}- {size}".format(name_color=Fore.WHITE, name=self.name, white=Fore.WHITE, size=self.size)

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class directory:
    files: list[file] = []
    directories: list['directory'] = []
    parent: 'directory' = None
    size = 0
    name = ""

    def set_parent(self, dir: 'directory'):
        self.parent = dir

    def add_file(self, name: str, size: int):
        self.size += size
        self.files.append(file(name, size))
        if (self.parent):
            self.parent.add_size(size)

    def add_dir(self, dir: 'directory'):
        self.directories.append(dir)
        dir.set_parent(self)

    def add_size(self, size: int):
        self.size += size
        if (self.parent):
            self.parent.add_size(size)

    def get_dir_by_name(self, name):
        result = list(filter(lambda x: x.name == name, self.directories))[0]
        if result is None:
            pass
        return result

    def get_parent(self):
        return self.parent

    def get_sub_dirs_bigger_than(self, size: int, recursive: bool = False):
        dirlist = [d for d in filter(
            lambda dir: dir.size > size, self.directories)]
        if recursive:
            for directory in filter(lambda dir: dir.size > size, self.directories):
                dirlist += directory.get_sub_dirs_bigger_than(size, True)
        return dirlist

    def get_sub_dirs_smaller_than(self, size: int, recursive: bool = False):
        dirlist = [d for d in filter(
            lambda dir: dir.size < size, self.directories)]
        if recursive:
            for directory in self.directories:
                dirlist += directory.get_sub_dirs_smaller_than(size, True)
        return dirlist

    def pretty_print(self, indent: int = 0):
        string = '{indent} {name_color}{dirname} {white}- {size}\n'.format(name_color=Fore.YELLOW,
                                                                           indent="│ " * 0, white=Fore.WHITE, dirname=self.name, size=self.size)
        indent += 1

        for dir in self.directories:
            if dir.name == "zssdlnc":
                pass
            symbol = "├" if dir != self.directories[-1] or len(
                self.files) > 0 else "└"
            string += '{indent} {symbol}{name}'.format(
                indent=" │" * (indent-1), symbol=symbol, name=dir.pretty_print(indent))

        for file in self.files:

            symbol = "├" if file != self.files[-1] else "└"

            indent_symbol = " │" if file != self.files[-1] else "  "
            string += '{indent} {symbol}{name}\n'.format(
                indent=" │" * (indent-1), indent2=indent_symbol, symbol=symbol, name=file.pretty_print())

        return string

    def __init__(self, name: str):
        self.name = name
        self.directories = []
        self.files = []
        self.size = 0
        self.parent = None


def interpret_line(line):
    global root, currdir
    if line == '192153 wdjdppzm':
        pass
    match line.split():
        case ['$', 'cd', '/']:
            #print('vamo a root')
            currdir = root

        case ['$', 'cd', '..']:
            #print('vamo parriba')
            if (currdir.get_parent()):
                currdir = currdir.get_parent()

        case ['$', 'cd', args]:
            #print('vamo a '+args)
            currdir = currdir.get_dir_by_name(args)

        case ['$', 'ls']:
            # print('listando')
            pass

        case ['dir', name]:
            currdir.add_dir(directory(name))

        case [size, name]:
            currdir.add_file(name, int(size))


def p1():
    global root
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split("\n")
        #x=map(interpret_line, lines)
        for line in lines:
            # print(line)
            interpret_line(line)
        #print(root.pretty_print())

        '''for dir in root.get_sub_dirs_smaller_than(100000, True):
            print(dir.size)
            print(dir.name)'''
        print(sum(map(lambda d: d.size, root.get_sub_dirs_smaller_than(100000, True))))


def p2():
    global root
    total_space = 70000000
    required = 30000000
    available_space = total_space - root.size
    missing_space=required-available_space
    print(missing_space)
    print(sorted(root.get_sub_dirs_bigger_than(missing_space,  True),key= lambda a : a.size)[0].size)


# p1()
root = directory('/')
currdir = root

d1 = directory("rodolfa")
d2 = directory("rodolfson")
d1.add_dir(d2)

p1()
p2()
