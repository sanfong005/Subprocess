import subprocess
subprocess.run('pwd')
subprocess.run('python3 -V',shell=True)
== alternative ==
subprocess.run(['python3','-V'])
subprocess.run('python3 -V'.split())

CompletedProcess Object
------------------
p = subprocess.run('python -V',shell=True)
print(p)                      # CompletedProcess(args=['python', '-V'], returncode=0)
print(p.args)                # ['python', '-V']
print(p.returncode)         # 0 [no error]

p = subprocess.run('python -j',shell=True)
print(p)     # CompletedProcess(args='python -j', returncode=2)

subprocess.run('python -j',shell=True,check=True)    # program will be stucked

Change folder
---------------------
subprocess.run('ls',cwd='/home')

import os
subprocess.run('ls',cwd=os.path.expanduser('~'))

subprocess.run(['echo HOME: $HOME'],shell=True)

subprocess.run(['echo HOME: $HOME'],shell=True,env={'HOME': 'birtHome')

subprocess.run('sleep 2',shell=True,timeout=1)

Ouputech
----------------------
p = subprocess.run(['python', '-V'],stdout=subprocess.PIPE)    # standard output (byte)
print(p)             # CompletedProcess(args=['python', '-V'], returncode=0, stdout=b'Python 3.8.1\n')
print(p.stdout)     # b'Python 3.8.1\n'

p = subprocess.run(['python', '-V'],stdout=subprocess.PIPE,encoding='utf-8') # extract only output
print(p.stdout)     # Python 3.8.1

    p = subprocess.run(['python', '-V'],stdout=subprocess.PIPE)    # < 3.6
    print(p.stdout.decode())
   
p = subprocess.run(['python', '-V'],stdout=subprocess.DEVNULL)
print(p)             # CompletedProcess(args=['python', '-V'], returncode=0)
print(p.stdout)     # None

p = subprocess.run(['python', '-j'],stderr=subprocess.PIPE)
print(p)         # CompletedProcess(args=['python', '-j'], returncode=2, stderr=b"Unknown option: -j\nusage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...\nTry `python -h' for more information.\n")
print(p.stderr) # b"Unknown option: -j\nusage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...\nTry `python -h' for more
print(p.stdout) # None

p = subprocess.run(['python', '-j'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print(p)         # CompletedProcess(args=['python', '-j'], returncode=2, stdout=b"Unknown option: -j\nusage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...\nTry `python -h' for more information.\n")
print(p.stderr) # None
print(p.stdout) # b"Unknown option: -j\nusage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...\nTry `python -h' for more information.\n"

    >= 3.7
p = subprocess.run(['python', '-V'],capture_output=True)
print(p.stdout)     # b'Python 3.8.1\n'

p = subprocess.run(['python', '-j'],capture_output=True)
print(p.stderr[0])     # b"Unknown option: -j\nusage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...\nTry `python -h' for more information.\n"


Output to A File
--------------------------
with open('pythonver.txt','w') as f:
    subprocess.run(['python', '-V'],stdout=f)
   
subprocess.run(['python', '-V'],stdout=open('pythonver.txt','w'))

subprocess.run(['python', '-j'],stderr=open('pythonerr.txt','w'))

subprocess.run(['python', '-j'],stdout=open('pythonerr.txt','w'),stderr=subprocess.STDOUT)



Input
---------------
subprocess.run('python',input=b'print(1./11)')

subprocess.run('python',input='print(1./11)',encoding='utf-8')

subprocess.run('python',input='print(1./11)',text=True)

subprocess.run('python',stdin=open('fin.py'))

subprocess.run('python',input=open('fin.py').read(),text=True)