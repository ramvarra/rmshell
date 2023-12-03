''' Remote Shell Server '''
import os
import sys

from common import util

def abc_xyz():
    return 10

if __name__ == '__main__':
    print('PY VER: ', sys.version_info)
    print("Util Version: ", util.version())
    for var, value in os.environ.items():
        print(f"{var} = '{value}")
