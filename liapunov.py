import numpy as np 
import matplotlib.pyplot as plt


result = []
lambdas = []
maps = []
xmin = 2
xmax = 4
mult = (xmax - xmin)*2000
rvalues = np.arange(xmin,xmax,0.01)

for r in rvalues:
    x = 0.1
    result = []
    
    for t in range(100):
        x = r*x*(1-x)
        result.append(np.log(abs(r-2*r*x)))
    lambdas.append(np.mean(result))
    
    for t in range(20):
        x = r*x*(1-x)
        maps.append(x)
print('done')
print(f'Maps length: {len(maps)}')

xticks = np.linspace(xmin,xmax,mult)
axes = plt.gca()
axes.set_ylim([-1,1])
axes.set_xlim([2.5,4])
plt.plot(rvalues,lambdas, 'r', xticks , maps, 'b.')
plt.ylabel('values')

plt.show()
    
# fig = plt.figure(figsize=(10,7))
# ax1 = fig.add_subplot(1,1,1)
# xticks = np.linspace(0,2,4000)
# zero = [0]*4000
# ax1.plot(xticks, zero, 'g-')
# # plot map
# ax1.plot(xticks, maps, 'r.',alpha = 0.3, label = 'Map')
# ax1.set_xlabel('r')
# # plot lyapunov
# ax1.plot(rvalues, lambdas, 'b-', linewidth = 3, label = 'Lyapunov exponent')

# ax1.grid('on')
# ax1.set_xlabel('r')
# ax1.legend(loc='best')
# ax1.set_title('Map of x(t+1) = x(t) + r - x(t)^2 versus Lyapunov exponent')


# def origin(x):
#     return (3*x*(1-x))
# def func(x):
#       return (3-6*x)

# def liapunov_calc(start_point):
#     xNext = start_point
#     print('Calculating exponent for function 3x(1-x')
#     sum = 0
#     for k in range(401,500):
#         xNext = origin(xNext)
#         sum += np.log(np.abs(func(xNext)))
#         print (xNext)
        
#     return print(((1/500) * sum))



