# class Animal:
#     alive = True
#
#     def eat(self):
#         print("This animal is eating.")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
#
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running.")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming.")
#
#
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying.")
#
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# rabbit.run()
# fish.swim()
# hawk.fly()


# # Multi-level Inheritance
# class Organism:
#     alive = True
#
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating.")
#
#
# class Cat(Animal):
#
#     def cry(self):
#         print("This cat is crying.")
#
#
# cat = Cat()
#
# print(cat.alive)
# cat.cry()
# cat.eat()

class Prey:
    def flee(self):
        print("This animal flees.")


class Predator:
    def hunt(self):
        print("This animal is hunting.")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
