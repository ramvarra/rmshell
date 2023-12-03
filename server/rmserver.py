import os
import sys

from common import util

print('Python Version: ', sys.version)
print("Util Version: ", util.version())
for var, value in os.environ.items():
    if 'python' in var.lower():
        print(f"{var} = '{value}")
    
