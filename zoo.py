class Animal:
    def reply(self):
        self.speak()
class Mammal(Animal):
    pass
class Cat(Mammal):
    def speak(self):
        print('Meow')
class Dog(Mammal):
    def speak(self):
        print('Ruol')
class Primate(Mammal):
    def speak(self):
        print('I am Mammal')
class Hacker(Primate):    
    def speak(self):
        print('I am Primate')
    #def speak(self):
    #    print('Hellow')

if __name__ == '__main__':
    spot = Cat()
    spot.reply()

    data = Hacker()
    data.reply()
