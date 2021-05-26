clc; clear all; close all;
pkg load control;

% %parametros do motor CC:
% J = 0.01;
% b = 0.1;
% K = 0.01;
% R = 1;
% L = 0.5;
% s = tf('s');
% 
% %modelo do motor - 2º ordem
% P_motor = K/((J*s+b)*(L*s+R)+K^2)

% %degrau em MA:
% t = 0:0.1:5;
% step(P_motor,t)

% %degrau em MF:
% figure;
% t = 0:0.1:5;
% sysMF = feedback(P_motor,1);
% step(sysMF,t)

%Parametros do GA:
NPop = 50;  %Numero de indivíduos
NGen = 3;   %Numero de genes em cada Ind.
NGer = 30;  %Numero de gerações
ftMut= 0.02; %Fator de mutação

%Definição do espaço de busca
XMin = [0 0 0];
XMax = [80 80 8]; % 1 1 0.001
stepMut = (XMax - XMin)*ftMut;

% 1 - Inicializacao da Populacao
Pop = zeros(NPop,NGen);
for i=1:NPop
  
    for j=1:NGen
      
        Pop(i,j) = rand * (XMax(j)-XMin(j)) + XMin(j);
        
    end
    
end

% 2 - Avalia População inicial
fitPop = zeros(NPop,1);

for i=1:NPop
  
    fitPop(i) = CalcFit(Pop(i,:));
    
end

% 3 - Processo Evolutivo
for g=1:NGer
  
   NSub = 0; %contador de individuos que foram substituidos.
   
   for i=1:NPop  
     
       %3.1 - Seleciona dois pais na Pop.
       p1 = randi(NPop,1);
       p2 = randi(NPop,1);              
       
       %3.2 - Cruza os dois pais e gera um novo Ind.
       ft1 = fitPop(p1)/(fitPop(p1)+fitPop(p2));
       ft2 = fitPop(p2)/(fitPop(p1)+fitPop(p2));
       nFilho = zeros(1,NGen); 
       
       for j=1:NGen
         
           nFilho(1,j) = ft2*Pop(p1,j)+ft1*Pop(p2,j);
           
       end
       
       %3.3 - Faz mutacao do novo filho:
       for j=1:NGen
         
           if(rand < 0.5)
           
               nFilho(1,j) = nFilho(1,j) + rand*stepMut(j);
               
           else
               
               nFilho(1,j) = nFilho(1,j) - rand*stepMut(j);
               
           end
           
       end
       
       %3.4 - Avalia o novo filho:
       fitFilho = CalcFit(nFilho(1,:));
       
       %3.5 - Tenta substituir o filho no lugar do pior pai:
       if fitPop(p1) < fitPop(p2)   %p1 é melhor que p2?
         
           if fitFilho < fitPop(p2) %o filho é melhor que p2?
             
               Pop(p2,:) = nFilho(1,:);
               fitPop(p2) = fitFilho;
               NSub = NSub+1;
               
           end
           
       else
           
           if fitFilho < fitPop(p1)  %o filho é melhor que p1?
             
               Pop(p1,:) = nFilho(1,:);
               fitPop(p1) = fitFilho;
               NSub = NSub+1;
               
           end
           
       end  
       
   end
   
   %4 - Acha o melhor Ind. da Pop.
   BestFit = 10000000000;
   idxBest = -1;
   
   for i=1:NPop
     
       if fitPop(i) < BestFit
         
           BestFit = fitPop(i);
           idxBest = i;
           
       end      
       
   end
   
   Best = Pop(idxBest,:);
   fprintf('Geracao = %4i --> bestFit = %4.5f -- NSub = %4i\n',g,BestFit,NSub);
   
end

fprintf('Melhor Modelo => Kp = %4.2f, Ki = %4.2f, Kd = %1.3f\n',Best(1),Best(2),Best(3));

%resposta sistema original:
J = 0.01; b = 0.1; K = 0.01;
R = 1; L = 0.5; s = tf('s');
Gs = K/((J*s+b)*(L*s+R)+K^2);
sysMF1 = feedback(Gs,1);
t = 0:0.1:5;
step(sysMF1,t);
hold on

%resposta sistema aproximado otimizado
Kp = Best(1); Ki = Best(2); Kd = Best(3);
Cs = pid (Kp,Ki,Kd);
sysMF2 = feedback(Gs*Cs,1);
step(sysMF2,t,'r');
legend('Sistema Original','Sistema Algoritmo');






