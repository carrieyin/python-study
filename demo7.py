# by y_dd
# 时间 2021/04/11
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, '*', i, '=', i*j, end='\t')
    print()
a=0
while a < 3:
    print(a)
    a+=1
    if a==2:
        break;
else:
    print('for执行结束')