#! drill for class decorator



class Person:
    def __init__(self, name):
        self._name = name

    class CAP:
        def __get__(self, instance, owner):
            first = instance._name.split(' ')[0]
            last = instance._name.split(' ')[1]
            print('decorator fetching ... %s, %s, %s' % (self, instance, owner))
            return 'first name:%s, last name:%s' % (str.upper(first), str.upper(last))
        def __set__(self, instance, value):
            instance._name = value

    name = CAP()
    
j = Person('abbigale zhang')
d = Person('justin zhang')
print(j.name, d.name)
print(j, d)