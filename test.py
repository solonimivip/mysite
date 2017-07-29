#!/usr/bin/python3

import sys
import os
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

#条件控制
i = 100
if i < 100:
    print(i)
elif i == 100:
    print(i+100)
else:
    print(i*100)
#循环
while i<110:
    print(i)
    i = i+1

for i in range(1,6):
   for j in range(1, i+1):
      print("*",end='')
   print('\r')


l1 = ['lala.log','xixi.log','haha']
for j in l1:
    if j.endswith('.log'):
        print(j)
    else:
        print('==')


for k in range(0,10):
    print(k)

str1 = 'www.baid.com'
s = enumerate(str1)
s.next
