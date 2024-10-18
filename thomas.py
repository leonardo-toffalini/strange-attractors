from manim import *
from scipy.integrate import solve_ivp
import numpy as np


# TODO make animation that show one to three curves per b value
# and animates how the curves change as b changes


def thomas_system(t, state, b=0.208186):
    x, y, z = state
    dxdt = np.sin(y) - b * x
    dydt = np.sin(z) - b * y
    dzdt = np.sin(x) - b * z
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, 2*time),
        y0=state0,
    )
    return solution.y


class ThomasAttractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-5, 5, 1),
            x_length=16,
            y_length=16,
            depth=8,
        )
        axes.center()
        self.set_camera_orientation(phi=100 * DEGREES, theta=-45 * DEGREES, zoom=0.5)
        self.begin_ambient_camera_rotation(rate=0.1)
        # self.add(axes)


        epsilon = 1e-2
        evolution_time = 30
        n_points = 10
        states = [
            [0.1 + n * epsilon, 0 + n * epsilon, 0 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([RED, BLUE], len(states))

        curves = VGroup()
        for state, color in zip(states, colors):
            sol = ode_solution_points(thomas_system, state, evolution_time)
            points = list(zip(sol[0], sol[1], sol[2]))
            curve = VMobject().set_points_smoothly(axes.c2p(points))
            curve.set_stroke(color, width=1, opacity=0.25)
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
        self.play(distance_to_origin.animate.set_value(0.3), run_time=2)
        self.wait(5)


