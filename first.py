print('hello')
fp = open('E:/temp/a.txt', 'a+')
print('python', file=fp)
fp.close()