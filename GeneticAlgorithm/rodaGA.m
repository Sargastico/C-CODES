clc, clear;

pkg load ga;

fitfcn = @fcusto;
consfcn = @frest;
nvar = 2;
# LB = [-1 -1];
# UB = [1 0.75];
LB = [0 0];
UB = [1 13];

options = gaoptimset('PopulationSize',100,'Generations',200);

[soln, fval] = ga(fitfcn, nvar, [], [], [], [], LB, UB, consfcn, options)
