class Animal(object):
    # Every animal has an age, but a name may not be necessary
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self, name):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Dog(Animal):
    def speak(self):
        print("Woof!")

    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)

        self.set_name(name)
        self.friends = []

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def show_friends(self):
        for friend in self.friends:
            print(friend)

    def speak(self):
        print("Hello, my name is " + self.name + "!")

    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output 
    
cat = Cat(3)
dog = Dog(4)
me = Human("Chase", 27)


cat.set_name("Stripes")
dog.set_name("Bubbles")

me.add_friend("Ryan")
me.add_friend("Mason")
me.add_friend("Jabe")

print(cat)
cat.speak()

print(dog)
dog.speak()

print(me)
me.speak()