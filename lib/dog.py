#!/usr/bin/env python3

class Dog:
    def __init__(self,name, breed= "Mutt"):
        self.name= name
        self.breed= breed
Rex= Dog("Rex", "German shephard")
print(Rex.breed)


# class Dog:
#     def __init__(self, name):
#         self.name= name
#         print(self.name)
#     def bark(self):
#         print("Woof!")
# fido = Dog("Fido")
# fido.name

# snoop = Dog("Snoop")
# snoop.name


# class Dog:
#     def __init__(self, name):
#         print(f"{name} is born")
#     def bark(self):
#         print("Woof!")
#     def showing_self(self):
#         print (self)
# fido= Dog("Fido")
# fido.showing_self()

# snoop = Dog("Snoop")
# snoop.showing_self()