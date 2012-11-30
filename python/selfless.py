class d:
    def __init__(self, arg):
        self.a = arg
    def p(self):
        a = self.a - 99
        print "my a= ", a
        print "instance a= ", self.a

x = d(1)
y = d(2)
x.p()
y.p()

class e:
    def __init__(self, arg):
        global a 
        a = arg
    def p(self):
        print "a= ", a
        #print "instance a=", self.a

e1 = e(1)
e2 = e(2)
e1.p()
e2.p()