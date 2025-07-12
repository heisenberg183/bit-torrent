# Library Code

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        if name!='Base' and not 'bar' in body:
            raise TypeError("Bad User Class")
        return super().__new__(cls, name, bases, body)

class Base(metaclass = BaseMeta):
    def foo(self):
        return self.bar()
    
    def __init_subclass__(cls, *a, **kw):
        print('init sublclass', a, kw)
        return super().__init_subclass__(*a, **kw)
