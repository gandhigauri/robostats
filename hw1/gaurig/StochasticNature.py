'''class for stochastically generating nature true labels'''
import random

class StochasticNature(object):
	"""docstring for StochasticNature"""
	def __init__(self):
		self.true_label = random.choice([-1,1]) #random true label from nature

#if __name__ == '__main__':
#	sn = StochasticNature()
#	print sn.true_label	