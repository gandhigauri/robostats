classdef gameGaussian < Game
    %GAMEGAUSSIAN This is a concrete class defining a game where rewards a
    %   are drawn from a gaussian distribution.
    
    methods
        
        function self = gameGaussian(nbActions, totalRounds) 
            % Input
            self.nbActions = nbActions;%   nbActions - number of actions
            self.totalRounds = totalRounds;%   totalRounds - number of rounds of the game
            self.N = 0;
            self.tabR = zeros(self.nbActions, self.totalRounds);
            self.tabR(:) = -1;
            for n = 1 : self.nbActions
                mu = rand;
                sigma = rand;
                for t = 1 : self.totalRounds
                    while (self.tabR(n,t) > 1) || (self.tabR(n,t) < 0)
                        self.tabR(n,t) = normrnd(mu, sigma);
                    end
%                     if self.tabR(n,t) > 1
%                         self.tabR(n,t) = 1;
%                     else if self.tabR(n,t) < 0
%                             self.tabR(n,t) = 0;
                        %end
                    %end
                end
            end 
        end
        
    end    
end

