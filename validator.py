def personDecor(attr_name, attr_age):
    def pf(aClass):
        class person_name:
            value = []
            subject_class = None
            def __init__(self, *args):
                object.__setattr__(self, 'subject_class', aClass())
                object.__setattr__(self, 'value', [attr_name, attr_age])
 
                for ar in zip(('name', 'age'), args):
                    self.__setattr__(ar[0], ar[1])

            def __getattr__(self, item):
                return getattr(self.subject_class, item)       

            def __setattr__(self, item, value):
                print(item, value)
                if item in self.value:
                    if item=='name' and not self.isName(value):
                        print('"%s" attribute can only contain alphabeta where "%s" is used.' % (item, value))
                        print('the value is set to "None"')
                        value = None
                    if item=='age' and value < 0:
                        print('"%s" attribute can not less than 0 where "%s" is used.' % (item, value))
                        print('the value is set to "0"')
                        value = 0                   
                setattr(self.subject_class, item, value)

            def isName(self, name):
                if name == None or str.isalpha(name.replace(' ', '')) :
                    return True
                return False

        return person_name
    return pf

def argumentDecor(*args, **kargs):
    def onDecor(func):

        print('in decorating....')
        def onCall(*a, **d):
            print('on calling....')
            print('a: %s; args: %s' % (str(a), str(args)))
            for item in kargs:
                print('%s, %s, %s' % (item, kargs[item][0], kargs[item][1]))
                if item in d:
                    if d[item] < kargs[item][0] or d[item] > kargs[item][1]:
                        raise TypeError('argument "%s" = %s, it is out of range.' % (item, d[item]))

            
            for (av, (low, high)) in zip(a, args):
                print('%s, %s, %s' % (av, low, high))
                if av < low or av > high:
                        raise TypeError('argument value %s, it is out of range:(%s, %s).' % (av, low, high))

            return func(*a, **d)
        return onCall
    return onDecor

def simple(func):
    print('simple, decorating')
    return func

def simple1(func):
    print('simple1, decorating')
    def onCall(*args):
        result = func(*args)
        return 'end of oncall, result=%s' % result
    return onCall

if __name__ == '__main__':

    # class CTest:
    #     @argumentDecor((-100, 99))
    #     def func2decor(self, x, y):
    #         print('x and y')

    #     # func2decor = argumentDecor((-100, 99))(func2decor)

    # t = CTest()
    # t.func2decor(200,0)

#    @argumentDecor(a = (1,10), b=(-5, 0))
    @argumentDecor((1,10), (-5, 0))
    def test(a, b, c):
        print('a = %s, b=%s, c=%s' % (a, b, c))

    test(1,b=2,c=5)
    print('------------------------')


#     @personDecor('name', 'age')
#     class Person:
#         def __init__(self, name = 'Joe', age = 24):
#             self.name = name
#             self.age = age

#     p1 = Person('joe 1blow', -1)
#     p1.name = 'Joe Blow'
#     p1.age = 44
#     p2 = Person('Mary read', 23)
#     p2.age = -2
#     print(p1, p1.name, p1.age)
#     print(p2, p2.name, p2.age)

