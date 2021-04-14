# by y_dd
# 时间 2021/04/11

lst=['hello', 'world', 123]
lst1=list(['hello', 'world', 567])
lst2=lst[0: : 2]
print(lst, lst[0], lst[-3])
print(lst.index('world'))
print(lst1)

print(lst2)
lst3=[i for i in range(0, 8)]
print('lS3---', lst3)
s1 = {'c':200, 'a':230}
print(s1, type(s1))

s2 = dict(id='a', ph='c')
print(s2, type(s1))

#可以获取key集合，类型dict_keys
keys=s1.keys()
print(keys, type(keys))
print(list(keys), type(list(keys)))

values=s1.values()
print(values, type(values))
print(list(values), type(list(values)))

items=s1.items()
print(items, type(items))
print(list(items))

#遍历出的为key
for ite in s1:
    print(ite, s1.get(ite))

