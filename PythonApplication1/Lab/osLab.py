import os
def pre_dir(dir):
    L=os.path.split(dir)
    return L[0]

test='path/gg/yy'
print(pre_dir(test))
