# File metainstance.py

class MetaOne(type):
    def __new_(meta, classname, supers, classdict):
        print('In MetaOne.new: ', classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self, a):
        return 'toast' + '  ' + a

class Super(metaclass = MetaOne):
    def spam(self):
        return 'spam'
    
class Sub(Super):
    def eggs(self):
        return 'eggs'
