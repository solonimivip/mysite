#!usr/bin/python3

import os

url = 'bb.txt'

#判断文件是否存在
if os.path.exists(url):
    file = open(url,'a')
while True:
    content = input('请输入:')
    if content == 'q' or content == 'quit':
        os._exit(0)
    else:
        print(content)
        file.write(str(content)+'\n')
        file.flush()
file.close()
