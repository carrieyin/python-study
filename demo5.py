# by y_dd
# 时间 2021/04/10

print(15//-6)
print(15//6)
print(15.18//6)

x, y, z = 1, 2, 3
print(x,y,z)

print(x,y,z)
print(id(x), type(x), x)
print(x< y) #值True
print(x is y) #值False

a = 10
b = 10
print(a is b) #值True
print(a is not b)

print(a==1 and b==10)
print(a==1 or b==10)
f=True
print(not f)
print(4&8)

a=int(input('input a :'))
if a%2==0:
    print('a是偶数')
else:
    print("a是奇数")

if a>90:
    print('A')
elif a>80:
    print('B')

print('如果x > y输出x' if x > y else '输出y')