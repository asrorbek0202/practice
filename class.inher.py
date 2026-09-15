print("==== inheritance =====")
# parent > child
# pareent class o'zining child clasiga faqatgina public hamda protected propertylarini yani state va metodlarini pass qiloladi


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


dog.introduce()
cat.introduce()
fish.introduce()

print("========")
dog.make_voice()
fish.make_voice()

print("=======")
print(Animal.descriptioin)
print(Dog.descriptioin)

print(dog.voice, fish.voice)
print("dog.status", dog.status)
print("cat.status", cat.status)
