import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x jsu')
    os.system('./jsu')
elif bit == '32bit':
    os.system('chmod +x jsu32')
    os.system('./jsu32')
else:
    print('device not supported')
