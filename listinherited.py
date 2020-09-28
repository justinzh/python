#!python
# File listinherited.py (2.x + 3.x)

class ListInherited:
    """
    Using dir() to collect both instance attrs and names inherited from 
    its classes; Python 3.x shows more names than 2.x because of the
    implied object superclass in the new-style class model; getattr()
    fetches in herited names not in self.__dict__; use __str__, not 
    __repr__, or else this loops when printing bound methods!
    """
    
    def __attrnames(self, indent=' '*4):
        result = 'Under%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2]=='__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr)) 
        return result % ','.join(unders)
    
    def __str__(self):
        return '<Instance of %s, address %s:\n%s.' % (
                    self.__class__.__name__,
                    id(self),
                    self.__attrnames()
        )

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)
