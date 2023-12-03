import os
import sys

from common import util

print("Util Version: ", util.version())
for var, value in os.environ.items():
    print(f"{var} = '{value}")
    
