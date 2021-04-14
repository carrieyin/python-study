# by y_dd
# 时间 2021/04/11
r=range(10)
print(r)
print(list(r))
r=range(1, 9)
print(list(r))
r = range(1,9,2)
print(list(r), type(r))
print(3 in r)
print(4 not in r)

for i in range(0, 9):
    print(i)

for _ in range(0, 3):
    print("我在这里")

#for else
for item in range(0, 2):
    a=input("请输入")
    if a=='123':
        break
    else:
        print('输入了错误:', a)
else:
    print('for正常执行结束')