''' Remote Shell Server '''
import os

from common import util

def abcXyz():
    return 10

if __name__ == '__main__':
    print("Util Version: ", util.version())
    for var, value in os.environ.items():
        print(f"{var} = '{value}")
