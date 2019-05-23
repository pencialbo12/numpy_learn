def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return  'negtive'
    else:
        return 'zero'
for x in [-1, 0, 1]:
    print(sign(x))

def hello(name, loud  = False):
    if  loud:
        print('hello, %s!' %name.upper())
    else:
        print('hello, %s'%name)
hello('shutong')
hello('peter', loud=True)
