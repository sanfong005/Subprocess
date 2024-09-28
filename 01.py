a = float(input())
print(a/11.)

import subprocess
subprocess.run(['python','fin.py'])

import subprocess
subprocess.run(['python','fin.py'],input='2',text=True)


a = int(input())
b = int(input())
print('%d/%d = %s'%(a,b,a/b))

subprocess.run(['python','fin.py'],input='2\n3',text=True)

---------------
fin.py
---------------
a = int(input())
b = int(input())
print('%d×%d = %s'%(a,b,a*b))

po = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,text=True)
po.stdin.write('11\n')
po.stdin.flush()
po.stdin.write('12\n')
po.stdin.flush()
po.wait()

with subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,text=True) as po:
    po.stdin.write('11\n')
    po.stdin.flush()
    po.stdin.write('12\n')
    po.stdin.flush()
   
   
Get values from .stdout & .stderr
------------------------------------
a = int(input())
print('2^%d = %s'%(a,2**a))

po = subprocess.Popen(['python','sanpo.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
po.stdin.write('13\n')
po.stdin.flush()
print(po.stdout.read())         # 2^13 = 8192

po = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,stdout=open('xxx.txt','w'),text=True)
po.stdin.write('15\n')
po.stdin.flush()


po1 = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
po1.stdin.write('7\n')
po1.stdin.flush()

po2 = subprocess.Popen(['python','fin.py'],stdin=po1.stdout,stdout=subprocess.PIPE,text=True)
print(po2.stdout.read())         # 28



Multiple .Popen
---------------------------
fin.py
--------
import time
a = int(input())
time.sleep(a)
print('Elapse %s second'%a)




import subprocess,time

po3 = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,text=True)
po3.stdin.write('3\n')
po3.stdin.flush()

po2 = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,text=True)
po2.stdin.write('2\n')
po2.stdin.flush()

po1 = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,text=True)
po1.stdin.write('1\n')
po1.stdin.flush()

time.sleep(4) #





tt = [2,6,5,1]
for t in tt:
    po = subprocess.Popen(['python','fin.py'],stdin=subprocess.PIPE,text=True)
    po.stdin.write('%d\n'%t)
    po.stdin.flush()

time.sleep(max(tt)+1)