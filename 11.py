def deco1(func):
    list1 = {}
    def _deco1(*args,**kwargs):
        if func not in list1:
            list1[func] = func(*args,**kwargs)
        return  list1[func]
    return _deco1()


@deco1
def myfunc():
    print("myfunc called.")

a = myfunc()