classdef policyGWM < Policy
    %POLICYGWM This policy implementes GWM for the bandit setting.
    
    properties
        nbActions % number of bandit actions
        weights
        lastAction
        roundCounter
        p% Add more member variables as needed
    end
    
    methods
        
        function init(self, nbActions)
            % Initialize any member variables
            self.nbActions = nbActions;
            self.weights = ones(1, self.nbActions);
            self.roundCounter = 0;% Initialize other variables as needed

        end
        
        function action = decision(self)
            self.p = self.weights/sum(self.weights);
            [~, action] = max(mnrnd(1,self.p));
            self.lastAction = action; 
            self.roundCounter = self.roundCounter + 1;% Choose an action according to multinomial distribution
        end
        
        function getReward(self, reward)
            % Update the weights
            
            % First we create the loss vector for GWM
            lossScalar = 1 - reward; % This is loss of the chosen action
            lossVector = zeros(1,self.nbActions);
            lossVector(self.lastAction) = lossScalar;
            eta = sqrt(log10(self.nbActions)/self.roundCounter);
            for n = 1:self.nbActions
                self.weights(n) = self.weights(n) * exp(-eta * lossVector(n));
            end
            % Do more stuff here using loss Vector
        end        
    end
end

