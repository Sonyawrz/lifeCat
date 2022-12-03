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
    print('Time to study')
    if self.progress < 2:
      self.gladness += 3
    self.progress += 4
    self.gladness -= 2
  def to_sleep(self):
    print('Time to sleep')
    self.gladness += 3
  def to_chill(self):
    print('Rest time')
    self.gladness += 5
    self.progress -= 2
  def is_alive(self):
    if self.progress < -5:
      print('You are bad')
      self.alive = False
    elif self.gladness <= 0:
      print('Dead inside')
      self.alive = False
    elif self.progress > 50:
      print('Amazing! You are so smart')
      self.alive = False
  def statics(self):
    print('Gladness: ', self.gladness, 'Progress ',self.progress)
  def live(self, day):
    day = "Day " + str(day) + " of " + self.breed + " life"
    