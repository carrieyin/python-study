# by y_dd
# 时间 2021/04/11

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print( "输出: ")
    print(arg1)
    for var in vartuple:
        print(var, end='\t')
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);


def printme(str):
    "打印任何传入的字符串"

    print(str);

    return;


# 调用printme函数

printme("My string");