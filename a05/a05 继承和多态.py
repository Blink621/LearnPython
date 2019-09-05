# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
        
def run_twice(animal):
    animal.run()
    animal.run()  


dog = Dog()
dog.run()

cat = Cat()
cat.run()  
run_twice(Tortoise())
