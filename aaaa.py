def singleton(cls, *args, **kwargs):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

@singleton
class Test(object):
    a = 1

test =  Test()
test1 = Test()
a = id(test)
b = id(test1)
print(a)

print(id(test) == id(test1))