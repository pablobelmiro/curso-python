import os
from datetime import datetime
dir = os.getcwd()

def createDir():
    os.mkdir('test-dir')
    print("dir created")

def remove():
    os.rmdir(os.path.join(dir, 'test-dir'))
    list = os.listdir(dir)
    print(list)
    for fd in list:
        if(fd == 'os.py'):
            continue
        else:
            print('removing {}'.format(fd))
            os.remove(os.path.join(dir, fd))

def createfiles():
    flags = os.O_RDWR | os.O_CREAT
    mode = 0o666
    i=0
    for i in range(10):
        fd = os.open(os.path.join(dir, 'test'+str(i)+'.txt'), flags, mode)
        print("file created {}".format(fd))
        os.close(fd)
        i += 1

print(os.getcwd())
print(os.path.getmtime(os.getcwd()))
print(datetime.utcfromtimestamp(os.path.getmtime(os.getcwd())))

print('==========> Creating dir...')
createDir()

print(os.listdir(os.getcwd()))

print('==========> Creating file...')
createfiles()
os.system('PAUSE')

print(os.listdir(os.getcwd()))

print('==========> removing all...')
remove()



