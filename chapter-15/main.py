# No exercises

class Counter:
	x = 0
	name = "default-counter"

	def __init__(self, name):
		self.name = name

	def increment(self):
		self.x += 1

class AdvancedCounter(Counter):
	def decrement(self):
		self.x -= 1

counter = AdvancedCounter("new-counter")
counter.increment()
print(counter.x)
counter.decrement()
print(counter.x)