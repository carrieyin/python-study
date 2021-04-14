# by y_dd
# 时间 2021/04/10

#输出类型
name='abc'
print('name:id', id(name))
print('name:type', type(name))

#浮点计算
print(1.1+2.2)
from decimal import  Decimal
print(Decimal('1.1')+Decimal('2.2'))

#bool
b1=True
b2=False

print(b1+1)
print(b2+1)

#字符串类型
str1='hello world'
str2="hello world"
print(str1, type(str1))
str3="""hello 
world"""
print(str3)

#类型转换
name='hello'
age=3
# print('name'+ name + 'age' +age) 此处报错connect error
print('name:'+ name + ' age:' +str(age))

print("My name is %s and weight is %d kg!" % ('Zara', 21))