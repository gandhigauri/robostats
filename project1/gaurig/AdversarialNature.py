'''class for adversarially generating nature true labels'''

class AdversarialNature(object):
	"""docstring for AdversarialNature"""
	def __init__(self, weight_vector, prediction_vector):
		self.weights = weight_vector  #vector containing weights allocated to each expert at t time step
		self.predictions = prediction_vector #vector containing expert predictions at t time step
		max_wt_index = self.weights.index(max(self.weights)) #calculate index of expert with max weight
		self.true_label = -1 * self.predictions[max_wt_index] #return adversarial truth wrt to the outcome of the max weight expert

#if __name__ == '__main__':
#	an = AdversarialNature([7,9,9],[-1,1,-1])
#	print an.true_label	