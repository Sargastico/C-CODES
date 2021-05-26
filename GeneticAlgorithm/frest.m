function [cin, ceq] = frest(x)
  
  # y = -sin(4*pi*x(1)) + 2 * sin(2*pi*x(2)).^2 - 1.5
  
  r1 = x(1) * x(2) + x(1) - x(2) + 1.5;
  r2 = 10 - x(1)*x(2);
  
  #cin = [y];
  cin = [r1; r2];
  ceq = [];
  
  
endfunction