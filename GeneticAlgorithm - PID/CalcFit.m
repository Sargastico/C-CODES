function fit = CalcFit(Ind)
%Ind = [K T L] para o ind. em análise
t = 0:0.1:5;

%resposta sistema original:
J = 0.01; b = 0.1; K = 0.01;
R = 1; L = 0.5; s = tf('s');
Gs = K/((J*s+b)*(L*s+R)+K^2);

%resposta sistema aproximado
Kp = Ind(1); Ki = Ind(2); Kd = Ind(3);
Cs = pid(Kp, Ki, Kd);
sysMF1 = feedback(Gs*Cs, 1);
Y = step(sysMF1, t);
C = cell2mat(struct2cell(stepinfo(sysMF1)));
Ta = C(2);
Mp = C(5);
ess = Y(length(t)-1);

h1 = abs(Ta-2);
  
if(h1==0)

  h1 = 1e-22;
  
end

if(Mp < 5 && Mp > 0)

  h2 = 0;
  
else
  
  h2 = abs(5-Mp);
  
end

if abs (ess-1) < 0.01
 
  h3 = 0;
  
else
  
  h3 = abs (ess-1);
  
end

fit = (h1) + (h2) + (h3);
%%end
fit = sqrt(fit);