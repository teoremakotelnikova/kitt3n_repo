#3
import os, sys
print(os.getcwd())

print(sys.path)

if os.getcwd() in sys.path: print(f'Yes, {os.getcwd()} is found in PATH')
