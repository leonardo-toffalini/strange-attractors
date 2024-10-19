from manim import *
from scipy.integrate import solve_ivp
from functools import partial
import numpy as np

# TODO: Make the curves parametric and reutnr a dense output with the doe solver
#       so that the rate at which the curve moves is constant

"""
Lorenz attractor defining differential equation
x' = sigma * (y - x)
y' = x * (rho - z) - y
z' = x * y - beta * z
"""

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

        diff_eq = MathTex(
            r"x'(t) =& \sigma (y(t) - x(t)) \\ y'(t) =& x(t)(\rho - z(t)) - y(t) \\ z'(t) =& x(t) y(t) - \beta z(t)"
        ).scale(0.5).to_corner(UL)
        self.add_fixed_in_frame_mobjects(diff_eq)

        params = MathTex(
            r"\sigma &= 10 \\ \rho &= 28 \\ \beta &= \frac{8}{3}"
        ).scale(0.5).to_corner(UR)
        self.add_fixed_in_frame_mobjects(params)

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


class LorenzAttractorDiffParams(ThreeDScene):
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

        params1 = MathTex(
            r"\sigma &= 10 \\ \rho &= 28 \\ \beta &= \frac{8}{3}",
        ).set_color([GREEN, BLUE]).scale(0.5).to_corner(UL)
        self.add_fixed_in_frame_mobjects(params1)

        params2 = MathTex(
            r"\sigma &= 13 \\ \rho &= 10 \\ \beta &= \frac{8}{3}"
        ).set_color([YELLOW, RED]).scale(0.5).to_corner(UR)
        self.add_fixed_in_frame_mobjects(params2)

        self.begin_ambient_camera_rotation(rate=0.1)

        evolution_time = 30
        epsilon = 1e-5
        n_points = 5
        states = [
            [10 + n * epsilon, 10 + n * epsilon, 10 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([GREEN, BLUE], len(states))
        colors2 = color_gradient([YELLOW, RED], len(states))

        curves = VGroup()
        for state, color, color2 in zip(states, colors, colors2):
            sol = ode_solution_points(lorenz_system, state, evolution_time)
            lorenz_system_partial = partial(lorenz_system, sigma=13, rho=10, beta=8/3)
            sol2 = ode_solution_points(lorenz_system_partial, state, evolution_time)
            points = list(zip(sol[0], sol[1], sol[2]))
            points2 = list(zip(sol2[0], sol2[1], sol2[2]))
            curve = VMobject().set_points_smoothly(axes.c2p(points))
            curve2 = VMobject().set_points_smoothly(axes.c2p(points2))
            curve.set_stroke(color)
            curve2.set_stroke(color2)
            curves.add(curve)
            curves.add(curve2)


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


class LorenzAttractorBifurcation(ThreeDScene):
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
        self.begin_ambient_camera_rotation(rate=0.1)
        self.add(axes)


        evolution_time = 30
        state = [10, 10, 10]
        num_points = 8
        params = [(10, 6 + 3*i, 8/3) for i in range(num_points)]
        colors = color_gradient([GREEN, BLUE], len(params))

        curves = VGroup()
        for color, param in zip(colors, params):
            sigma, rho, beta = param
            lorenz_system_partial = partial(lorenz_system, sigma=sigma, rho=rho, beta=beta)
            sol = ode_solution_points(lorenz_system_partial, state, evolution_time)
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


class LorenzAttractorParamEvolution(ThreeDScene):
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

        step_size = 0.4
        num_params = 50

        params = MathTex(
            fr"\sigma &= 10 \\ \rho &= 6 + {step_size} \cdot i \quad i = 0, 1, \ldots, {num_params - 1} \\ \beta &= \frac{{8}}{{3}}"
        ).scale(0.5).to_corner(UL)
        self.add_fixed_in_frame_mobjects(params)

        self.begin_ambient_camera_rotation(rate=0.1)

        evolution_time = 52
        state = [10, 10, 10]
        params = [(10, 6 + step_size*i, 8/3) for i in range(num_params)]
        colors = color_gradient([GREEN, BLUE], len(params))

        curves = VGroup()
        for color, param in zip(colors, params):
            sigma, rho, beta = param
            lorenz_system_partial = partial(lorenz_system, sigma=sigma, rho=rho, beta=beta)
            sol = ode_solution_points(lorenz_system_partial, state, evolution_time)
            points = list(zip(sol[0], sol[1], sol[2]))
            curve = VMobject().set_points_smoothly(axes.c2p(points))
            curve.set_stroke(color)
            curves.add(curve)


        curves.set_stroke(width=2, opacity=0.8)
        dt = evolution_time / len(curves)


        self.play(FadeIn(curves[0]))
        for start, target in zip(curves[:-1], curves[1:]):
            self.play(FadeTransform(start, target, run_time=dt))


        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.wait(1)
        self.play(distance_to_origin.animate.set_value(0.8), run_time=2)
        self.wait(5)



