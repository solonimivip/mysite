#!usr/bin/python3

#列表
list1 = ['goole','baidu','alibaba','taobao']
print(list1[1])
print(list1[1:3]) #截取从1-3位字符
list1[1] = 2001 #重新赋值
print(list1[1])
print(len(list1))#查看列表长度
list1.reverse()#反向列出字符串
print(list1)
list1.append('jingdong')#字符后面追加字符串
print(list1)
#元组转列表
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print(list1)
del list1[2] #删除第三个元素
print(list1)
print('==========元组============')
#元组
tup1 = ()#创建空元组
tup1 = (50,)#元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)

tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup;
print("删除后的元组 tup : ")
#列表转元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)

print('=============字典===============')
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
del dict['Name'] # 删除键 'Name'
