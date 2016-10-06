%% This script applies a random policy on a constant game
clc;
close; 
clear all;
tabdata = load('data\univLatencies.mat');
tabdata = tabdata.univ_latencies;
%% Get the constant game
%game = gameConstant();
game = gameGaussian(10, 10000);
%game = gameAdversarial();
%game = gameLookupTable(tabdata,1);
%% Get a set of policies to try out
policies = {policyUCB()};%{policyConstant(), policyRandom(), policyGWM(), policyEXP3(), policyUCB()};
policy_names = {'policyUCB'};%{'policyConstant', 'policyRandom', 'policyGWM', 'policyEXP3', 'policyUCB'};

%% Run the policies on the game
figure;
hold on;
for k = 1:length(policies)
    policy = policies{k};
    game.resetGame();
    [reward, action, regret] = game.play(policy);
    %plot(action);
    %axis([1,game.totalRounds,0,game.nbActions+1]);
    fprintf('Policy: %s Reward: %.2f\n', class(policy), sum(reward));
    plot(regret);
end
legend(policy_names);