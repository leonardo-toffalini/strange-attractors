from manim import *
from scipy.integrate import solve_ivp
from functools import partial
import numpy as np
from itertools import product

"""
Lorenz83 defining differential equation
x' = -ax - y^2 - z^2 + af
y' = -y + xy - bxz + g
z' = -z + bxy + xz
"""

def lorenz_system(t, state, a=0.95, b=7.91, f=4.83, g=4.66):
    x, y, z = state
    dxdt = -a * x - y**2 - z**2 + a * f
    dydt = -y + x * y - b * x * z + g
    dzdt = -z + b * x * y + x * z
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, 0.5*time),
        y0=state0,
    )
    return solution.y

class LorenzAttractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(-0, 50, 5),
            x_length=16,
            y_length=16,
            depth=8,
        )
        axes.center()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=1)
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.1)

        epsilon = 1e-5
        evolution_time = 30
        n_points = 10
        states = [
            [2 + n * epsilon, 5 + n * epsilon, 10 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([RED, BLUE], len(states))

        curves = VGroup()
        for state, color in zip(states, colors):
            sol = ode_solution_points(lorenz_system, state, evolution_time)
            points = list(zip(sol[0], sol[1], sol[2]))
            curve = VMobject().set_points_smoothly(axes.c2p(points))
            curve.set_stroke(color)
            curves.add(curve)


        curves.set_stroke(width=2, opacity=0.8)


        self.play(
            *(
                Create(curve, rate_func=linear, run_time=evolution_time)
                for curve in curves
            ),
            run_time=evolution_time
        )
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.wait(1)
        self.play(distance_to_origin.animate.set_value(0.8), run_time=2)
        self.wait(5)
