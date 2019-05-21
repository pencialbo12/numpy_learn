d ={'peter': 'handsome', 'shutong':'cute'}#key:value
print('peter' in d)#is in ?
print(d['peter'])#下标访问内容
d['1']='11'
print(d['1'])
print(d['shutong'])
del d['1']
print('1' in d)

f = {'person':2, 'dog':4, 'man':3}

for  animals in f:
    legs = f[animals]
    print('a %s has %d legs'%(animals, legs))
    print('a %s has %d legs',(animals, legs))
