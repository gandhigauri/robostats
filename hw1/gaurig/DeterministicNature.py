'''class for deterministically generating nature true labels'''

class DeterministicNature(object):
	"""docstring for DeterministicNature"""
	def __init__(self, num_trial, obs_flag, new_obs):
		self.trial = num_trial #round of prediction 
		self.true_label = 0 #true label from nature
		self.nature_obs = new_obs #weather observations
		if not (obs_flag):
			if (self.trial%4) in [0,1]:
				self.true_label = 1
			else:
				self.true_label = -1
		else:
			if (self.trial%4) is not 0:
				if new_obs is 'sunny':
					self.true_label = 1
				else:
					self.true_label = -1
			else:
				if new_obs is 'sunny':
					self.true_label = -1
				else:
					self.true_label = 1





#if __name__ == '__main__':
#	dn = DeterministicNature(10)
#	print dn.true_label