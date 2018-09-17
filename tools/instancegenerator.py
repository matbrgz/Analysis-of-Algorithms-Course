from random import shuffle


class InstanceGenerator:
	def __init__(self):
		self.instancesize = instancesize

	def generator(self):
		# TODO: Improve randomness of the data variance
		if order == 'ASC':
			return range(10)

		if order == 'DESC':
			return reversed(range(10))

		if order == 'RAND':
			return shuffle(range(10))