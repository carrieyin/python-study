#读写文件
print('aaa', 'bbb', 'ccc')
fp = open('E:/temp/a.txt', 'a+')
print('bb', file=fp)
fp.close()

#转义字符\n 换行
print('hello\nworld')

#\t 制表符 注意与C++不同，根据制表位不同输出空格不同
print('hello\tworld')
print('hellooo\tworld')

# \r回车 回车回到行首，替换了hello
print('hello\rworld')

#\b 退一个格
print('hello\bworld')

#原字符
print(r'hello\rworld')

#最后一个字符不能是\
#print(r'hello\rworld\')