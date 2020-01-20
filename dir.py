import os
import pickle
def walk(dir):
    for name in  os.listdir(dir):
      path = os.path.join(dir,name)

      if os.path.isfile(path):
          print (path)
      else:
          return walk(path)



cwd = os.getcwd()
walk(cwd)