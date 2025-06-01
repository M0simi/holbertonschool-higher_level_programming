#!/usr/bin/python3


class SwimMixing:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixing, FlyMixin):
    def roar(self):
        print("The dragon roars!")
