from manim import *
from scipy.integrate import solve_ivp
import numpy as np

def aizawa_system(t, state, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
    x, y, z = state
    dxdt = (z - b) * x - d * y
    dydt = d * x + (z - b) * y
    dzdt = c + a * z - (z**3 / 3) - (x**2 + y**2) * (1 + e*z) + f * z * (x**3)
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, 1*time),
        y0=state0,
        method="BDF"
    )
    return solution.y

class AizawaAttractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-2, 5, 1),
            x_length=16,
            y_length=16,
            depth=8,
        )
        axes.center()
        self.set_camera_orientation(phi=100 * DEGREES, theta=-45 * DEGREES, zoom=1)
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.begin_3dillusion_camera_rotation()
        # self.add(axes)


        epsilon = 1e-2
        evolution_time = 30
        n_points = 10
        states = [
            [-0.1 + n * epsilon, -0.1 + n * epsilon, 1 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([PURPLE, MAROON], len(states))

        curves = VGroup()
        for state, color in zip(states, colors):
            sol = ode_solution_points(aizawa_system, state, evolution_time)
            points = list(zip(sol[0], sol[1], sol[2]))
            curve = VMobject().set_points_smoothly(axes.c2p(points))
            curve.set_stroke(color)
            curves.add(curve)


        curves.set_stroke(width=1.5, opacity=0.8)


        self.play(
            *(
                Create(curve, rate_func=linear, run_time=evolution_time)
                for curve in curves
            ),
            run_time=evolution_time
        )
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.wait(1)
        self.play(distance_to_origin.animate.set_value(3), run_time=2)
        self.wait(5)
