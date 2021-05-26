function z = levy_function(x)

  z = (4*(x(1)^2)) - (2 * 1 * (x(1)^4)) + ((1/3)*(x(1)^6)) + (x(1) * x(2)) - (4*(x(2)^2)) - 1 + (x(2)^4)
  plot ( x(1) , x(2) , "g." )
 
endfunction

function z = levy_function_countour(x, y)

  z = (4*(x^2)) - (2 * 1 * (x^4)) + ((1/3)*(x^6)) + (x * y) - (4*(y^2)) - 1 + (y^4)

endfunction

function Pop_init = myinitga(popsize, param)

  disp("Initializing the Population with grand")

  [Dim,err]       = get_param(param,"dimension",2)
  [MinBounds,err] = get_param(param,"minbound",-2*ones(1,Dim))
  [MaxBounds,err] = get_param(param,"maxbound",2*ones(1,Dim))

  Pop_init = list()
  nr = size(MaxBounds,1)
  nc = size(MaxBounds,2)
  for i=1:popsize
    u = grand(nr,nc,"def")
    Pop_init(i) = (MaxBounds - MinBounds).*u + MinBounds
  end
endfunction

PopSize     = 100;
Proba_cross = 0.7;
Proba_mut   = 0.1;
NbGen       = 10;
NbCouples   = 110;
Log         = %T;

ga_params = init_param();

ga_params = add_param(ga_params,"minbound",[-2; -2]);
ga_params = add_param(ga_params,"maxbound",[2; 2]);
ga_params = add_param(ga_params,"dimension",2);
ga_params = add_param(ga_params,"init_func",myinitga);

t=linspace(-%pi,%pi,30);

contour(t,t,levy_function_countour,10)

[pop_opt, fobj_pop_opt, pop_init, fobj_pop_init] = ..
  optim_ga(levy_function, PopSize, NbGen, Proba_mut, Proba_cross, Log, ga_params);

