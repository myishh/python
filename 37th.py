f = open('36th.py', 'r')
str = f.read(3)
print('read data is : ', str)

position = f.tell()
print('current location is : ', position)

str = f.read(3)
print('read data is : ', str)

position = f.tell()
print('current location is : ', position)

f.close()

print('-'*30)
f = open("36th.py", "r")
str = f.read(30)
print ("读取的数据是 : ", str)

# 查找当前位置
position = f.tell()
print ("当前文件位置 : ", position)

# 重新设置位置
f.seek(5,0)

# 查找当前位置
position = f.tell()
print ("当前文件位置 : ", position)

f.close()
