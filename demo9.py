# by y_dd
# 时间 2021/04/11
#list生成式
listc=[i for i in range(2, 9, 2)]
print(listc, type(listc))

lista=['a', 'b', 'c']
listb=[10, 20, 30]
#字典生成式
dic =  {i:j for i,j in zip(lista, listb)}
print(dic, type(dic))

#元组 属于不可变序列，不允许修改引用，但可以修改数据
#在多任务情况下，同时操作对象时不需要加锁
t=('hello', ['world', 'python'], 'test')
#先查看元组中t1的id
print(t[1], id(t[1]))
print(id('test'))
#以下操作需要改变引用会报错
#t[1]='test'
#这个操作不影响引用，可以操作，此时查看a[1]的引用并没有变更
t[1].append('i like python')
print(t[1], id(t[1]))



