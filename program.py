# this program is a demo for what Ed Lorenz experienced
from scipy.integrate import solve_ivp
from time import sleep
import sys

x0, y0, z0 = map(lambda x: float(x), sys.argv[1:4])

def lorenz_system(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, 0.5*time),
        y0=state0,
    )
    return solution.y

sols = ode_solution_points(lorenz_system, (x0, y0, z0), 300)

x = "{0: >14}".format("x")
y = "{0: >14}".format("y")
z = "{0: >14}".format("z")
print(x, y, z)

j = 0
for  x, y, z in list(zip(sols[0], sols[1], sols[2])):
    j += 1
    sleep(0.25)
    x = "{0: >14}".format(f"{x:.4f}")
    y = "{0: >14}".format(f"{y:.4f}")
    z = "{0: >14}".format(f"{z:.4f}")
    j_str = "{0: >3}".format(f"{j}")
    print(j_str, x, y, z)
    if j > 50:
        break

