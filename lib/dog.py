#!/usr/bin/env python3

class Dog:
    def bark(self):#instance method definition
        print("Woof!")
    def sit(self):
        print("The dog is sitting.")
fido = Dog()
fido.bark()#bark is the method
fido.sit()

snoopy = Dog()
snoopy.bark()
