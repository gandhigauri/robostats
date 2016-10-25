classdef policyEXP3 < Policy
    %POLICYEXP3 This is a concrete class implementing EXP3.
    
    properties
        nbActions % number of bandit actions
        weights
        lastAction
        roundCounter
        p% Define member variables
    end
    
    methods

        function init(self, nbActions)
           self.nbActions = nbActions;
           self.weights = ones(1, self.nbActions);
           self.roundCounter = 0;% Initialize member variables
        end
        
        function action = decision(self)
           self.p = self.weights/sum(self.weights);
           [~, action] = max(mnrnd(1,self.p));
           self.lastAction = action; 
           self.roundCounter = self.roundCounter + 1; % Choose an action
        end
        
        function getReward(self, reward)
            % reward is the reward of the chosen action
            % update internal model
            lossScalar = 1 - reward; % This is loss of the chosen action
            lossVector = zeros(1,self.nbActions);
            lossVector(self.lastAction) = lossScalar;
            eta = sqrt(log(self.nbActions)/(self.roundCounter * self.nbActions));
            for n = 1:self.nbActions
                self.weights(n) = self.weights(n) * exp(-eta * lossVector(n)/self.p(n));
            end
        end        
    end
end