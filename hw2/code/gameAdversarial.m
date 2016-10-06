classdef gameAdversarial<Game
    %GAMEADVERSARIAL This is a concrete class defining a game where rewards
    %   are adversarially chosen.

    methods
        
        function self = gameAdversarial()
            self.nbActions = 2;
            self.totalRounds = 1000;
            self.tabR = zeros(self.nbActions, self.totalRounds);
            for i = 1:self.totalRounds
                if mod(i,4)==0
                    self.tabR(1,i) = 0.8;
                    self.tabR(2,i) = 0.3;
                else if mod(i,4)==3
                    self.tabR(1,i) = 0.1;
                    self.tabR(2,i) = 0.4;
                    else
                        self.tabR(1,i) = 0.6;
                        self.tabR(2,i) = 0.9;
                    end
                        
                end
            end
            self.N = 0;
        end
        
    end    
end

