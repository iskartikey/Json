def outer(func):
    def inner():
        return func().upper()
    return inner()
@outer
def yoda():
    return"make it happen"
a=yoda
print(a)

class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print (self.x + ' ' + foo)

prop=A
# print(prop)
