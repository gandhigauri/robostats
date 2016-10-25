from StochasticNature import StochasticNature
from DeterministicNature import DeterministicNature
from AdversarialNature import AdversarialNature
import matplotlib.pyplot as plt
import random
import math

class wma(object):
	"""docstring for wma"""
	def __init__(self, num_trials, num_experts, eta, nature):
		self.num_trials = num_trials
		self.num_experts = num_experts
		self.eta = eta
		self.nature = nature
		self.WeightedMajorityAlgorithm(self.num_experts, self.eta, self.num_trials, self.nature)

	def WeightedMajorityAlgorithm(self, N, eta, T, nature):
		w = [1] * N  #initialize weight vector
		#loss vectors
		learner_loss = [0] * T
		expert_losses = [[0 for i in range(N)] for j in range(T)]
		sum_expert = [0] * N
		sum_learner = 0
		for t in range(T):
			eta = 1.0/math.sqrt(t+1)
			x = self.receive_obs(N, t) #receive expert advices
			#print "obs" + str(x) + "\n" 
			i = self.roullette_sampling(w, N)
			#print "i" + str(i) + "\n"
			y_est = x[i] #learner predicts outcome
			#print "y_est" + str(y_est) + "\n"
			y_true = self.receive_truth(nature, t, w, x)  #nature sends truth
			#print "y_true" + str(y_true) + "\n"
			for n in range(N):
				w[n] = w[n] * (1 - (eta * (y_true != x[n]))) #weight update for each expert 
				sum_expert[n] = sum_expert[n] + (1 * (x[n] != y_true)) #calculating expert losses 
				expert_losses[t][n] = sum_expert[n] 
			#print "wts" + str(w) + "\n"
			#print "expert_losses" + str(expert_losses) + "\n"
			#calculating learner losses
			sum_learner = sum_learner + (1 * (y_est != y_true)) 
			learner_loss[t] = sum_learner
		print "completed"
		self.plot_losses(learner_loss, expert_losses)
		self.plot_regret(learner_loss, expert_losses)
		plt.show()

	def roullette_sampling(self, w, N):
		sum_wts = sum(w)
		wt_probs = [0] * N
		for n in range(N):
			wt_probs[n] = (1.0 * w[n])/sum_wts 
		rand_num = random.uniform(0,1) #choose random number 
		sum_probs = 0
		for n in range(N):
			sum_probs = sum_probs + wt_probs[n]
			if (rand_num <= sum_probs):
				return n



	def receive_obs(self, N, t):
		obs_vector = [0] * N
		trial_num = t + 1
		obs_vector[0] = 1 #optimistic
		obs_vector[1] = -1 #pessimistic
		if (trial_num % 2) is 0:
			obs_vector[2] = 1
		else:
			obs_vector[2] = -1
		return obs_vector

	def receive_truth(self, nature, t, w, x):
		if nature is 'stochastic':
			self.stochastic = StochasticNature()
			return self.stochastic.true_label
		elif nature is 'deterministic':
			self.deterministic = DeterministicNature(t,0,0)
			return self.deterministic.true_label
		elif nature is 'adversarial':
			self.adversarial = AdversarialNature(w,x)
			return self.adversarial.true_label

	def plot_losses(self, learner_loss, expert_losses):
		plt.figure(1)
		plt.plot([expert[0] for expert in expert_losses],'r-',
			[expert[1] for expert in expert_losses],'b-',
			[expert[2] for expert in expert_losses],'g-',
			learner_loss,'y-')
		plt.xlabel('t')
		plt.ylabel('losses')
		plt.title(self.nature)
		print "plotted losses"

	def plot_regret(self, learner_loss, expert_losses):
		best_expert_loss = [min(loss) for loss in expert_losses] #loss of best expert at each time step
		#print best_expert_loss
		#print "\n"
		#print learner_loss
		regret = [0] * self.num_trials
		#sum_regret = 0
		for t in range(self.num_trials):
			regret[t] = (learner_loss[t] - best_expert_loss[t])
			#print learner_loss[t] - best_expert_loss[t]
			regret[t] = (1.0 * regret[t])/(t+1) #average regret for t time steps
		#print regret
		plt.figure(2)
		plt.plot(regret,'r-')
		plt.xlabel('t')
		plt.ylabel('regret')
		plt.title(self.nature)
		print "plotted regret"


if __name__ == '__main__':
	wma = wma(100,3,0.1,'deterministic')


