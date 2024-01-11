from sys import argv, exit
from subprocess import Popen
from os import chdir, popen
from traceback import print_exc

filename = argv[1]
python = 'python'


commands = {
    "python" : [["start", python ,argv[1]]],
    "c" : [["make", filename.split('.')[0]], ["start", f"./{filename.split('.')[0]}"]]
}


def main():

    chdir('\\'.join(filename.split('\\')[:-1]))

    with open(filename) as file:
        for line in reversed(file.readlines()):
            if line.startswith("#pam:"):
                filetype = line.replace("#pam:", '')
                break
        if not filetype:
            raise InvalidFileType
        for command in commands[filetype]:
            popen(" ".join(command))

class InvalidFileType(BaseException): ...

if __name__ == "__main__":

    print(argv[1])
    try:
        main()
        exit()
    except SystemExit:
        exit()
    except BaseException as e:
        print_exc()
        input()