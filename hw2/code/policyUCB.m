classdef policyUCB < Policy
    %POLICYUCB This is a concrete class implementing UCB.

        
    properties
        sumAction
        counterAction
        nbActions
        roundCounter
        lastAction% Member variables
    end
    
    methods
        function init(self, nbActions)
            self.nbActions = nbActions;
            self.sumAction = zeros(self.nbActions,1);
            self.counterAction = zeros(self.nbActions,1);
            self.roundCounter = 0;% Initialize
        end
        
        function action = decision(self)
            ucb = zeros(self.nbActions,1);
            self.roundCounter = self.roundCounter + 1;
            alpha = 1;
            if self.roundCounter <= self.nbActions
                action = self.roundCounter;
            else
                for n = 1:self.nbActions
                    ucb(n) = (self.sumAction(n)/self.counterAction(n)) + ...
                    sqrt(alpha * log(self.roundCounter)/(2 * self.counterAction(n)));
                end
                [~, action] = max(ucb);% Choose action
            end
%             figure(1);
%             plot(self.roundCounter, ucb(1),'ro');
%             hold on;
%             plot(self.roundCounter, ucb(2),'bo');
%             legend({'ucb_action1','ucb_action2'});
              self.lastAction = action;
%             drawnow;
        end
        
        function getReward(self, reward)
            self.sumAction(self.lastAction) = self.sumAction(self.lastAction) + reward;
            self.counterAction(self.lastAction) = self.counterAction(self.lastAction) + 1;% Update ucb
        end        
    end

end
