class Greeter(object):
    def __init__(self, name):
        self.name = name
    def greet(self, loud = False):
        if  loud:
            print('hello, %s!'%self.name.upper())
        else:
            print('hello, %s!'%self.name)
g =  Greeter('peter')
g.greet()
g.greet(loud = True)
