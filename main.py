from random import *
class Student:
  def __init__(self, breed):
    self.breed = breed
    self.eat = 50
    self.progress = 10
    self.alive = True
  def say_hello(self):
    print('Meow')
  def to_study(self):
    print('Meow Meow!')
    if self.progress < 2:
      self.gladness += 3
    self.progress 
