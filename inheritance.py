class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Child classes must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof" " Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"

class cheetah(Animal):
    def speak(self):
        return "Growl"


dog = Dog("Bosco", "Black")
print(dog.name,dog.speak(),dog.color)
# print(dog.speak())
# print(dog.color)

cat = Cat("Tom", "Blue")
print(cat.name,cat.speak(),cat.color)
# print(cat.speak())
# print(cat.color)

cheetah=cheetah("flash","Brown")
print(cheetah.name,cheetah.speak(),cheetah.color)
# print()

