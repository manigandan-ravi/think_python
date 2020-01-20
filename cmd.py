import pipes
import os

cmd = 'ls -la'
fp = os.popen(cmd)

print(fp.read())