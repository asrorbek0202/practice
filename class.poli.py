print("==== Polimorphism =====")
# parent > child
# pareent class o'zining child clasiga faqatgina public hamda protected propertylarini yani state va metodlarini pass qiloladi
# bitta parent classning metodi yoki state boshqa classlarda boshqacha amalga oshishi yani 1 ta ovoz degan metod hayvonlarga qarab tuslanadi shu polimorphism deyiladi
# poli ==> kop


class Animal:   # Parent
    descriptioin = "The class creates animals"

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}- {self.sound}")

    def protect(self):
        print("yes, i can protect you!")

    def make_voice(self):
        print(f"{self.name} says {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}- {self.sound}")

    def play(self):
        print("yes, i can play with you!")


class Fish(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says : {self.sound}- {self.sound}")

    def Swim(self):
        print("yes, i can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myow", True)
fish = Fish("Nemo", "ZzZzZz", False)


print("========")
dog.make_voice()
fish.make_voice()


print("-------")
# fish > Fish > Animal > oblect
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")

# Fish > Animal > oblect
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data", data1, data2)
