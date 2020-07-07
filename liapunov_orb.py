import numpy as np
import matplotlib.pyplot as plt

# No fixed points therefore exhibits no chaotic motion x^5 +x
# Since D[x^5+x]: 5*x^4 + x
# or when x = f(x) this is a fixed point by definition
#               f(x) = x^5 + x = x =>
#                   x^5 = 0
#                   x = sqrt^5(0) = 0
#             Not interesting

#  For future work consider equations of motion in the hamiltonian space as containing
#  any fixed points, for ultra cold atom scattering experiments "Nodes" where as there is a fixed potential due to
#  interfering lasers of wavelengths comprobable to the size of the electrons
#  such that latice structures for electrons to "fall" into and are unable to escape
#  These such systems might have fixed points; in 3 dimensions the number of degrees of freedom are
#  numerous and must be considered as something like a fixed point in a potential electric field
#  governed by some equation f(x,y,z), for instance.
#  Then
def arb_func(x):
    return x ** 5 + x


def derv_func(x):
    return 5 * x ** 4 + 1


result = []
lambdas = []
maps = []
xmin = float(input("Enter x min: "))
xmax = float(input("Enter x max: "))
mult = (xmax - xmin) * 2000
rvalues = np.arange(xmin, xmax, 0.01)
inp = float(input("Enter initial point for equation x^5 + x: "))
if inp:
    for r in rvalues:
        x = inp
        result = []

        for t in range(100):
            x = arb_func(x)
            result.append(np.log(abs(derv_func(x))))
        lambdas.append(np.mean(result))

        for t in range(20):
            x = arb_func(x)
            maps.append(x)
    print("done")
    print(f"Maps length: {len(maps)}")

    xticks = np.linspace(xmin, xmax, mult)
    axes = plt.gca()
    axes.set_ylim([-10, 10])
    axes.set_xlim([xmin, xmax])
    plt.plot(rvalues, lambdas, "r", xticks, maps, "b.")
    plt.ylabel("values")

    plt.show()

