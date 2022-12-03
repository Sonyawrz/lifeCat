from random import *
class Student:
	def __init__(self, breed):
		self.breed = breed
		self.gladness = 50
		self.progress = 0
		self.alive = True
	def say_hello(self):
		print('Meow')
	def to_study(self):
		print('Time to study')
		if self.progress < 5:
			self.gladness -= 1
		self.progress += 4
		self.gladness -= 1
	def to_sleep(self):
		print('Time to sleep')
		self.gladness += 6
	def to_chill(self):
		print('Rest time')
		self.gladness += 7
		self.progress -= 2
	def is_alive(self):
		if self.progress < -10:
			print('You are bad')
			self.alive = False
		elif self.gladness <= 0:
			print('Dead inside')
			self.alive = False
		elif self.progress > 50:
			print('Amazing! You are so smart')
			self.alive = False
	def statics(self):
		print('Gladness: ', self.gladness, 'Progress: ',self.progress)
	def live(self, day):
		day = "Day " + str(day) + " of " + self.breed + " life"
		print(day)
		live_cube = randint(1,4)
		if live_cube == 1:
			self.to_study()
		elif live_cube == 2:
			self.to_sleep()
		elif live_cube == 3:
			self.to_chill()
		elif live_cube == 4:
			self.say_hello()
		self.statics()
		self.is_alive()

cat = Student('Sanya')
for day in range(365):
	if cat.alive == False:
		break
	cat.live(day)

# human = Student('Zolo')
# for day in range(365):
# 	if human.alive == False:
# 		break
# 	human.live(day)