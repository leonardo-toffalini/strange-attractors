from manim import *

class Opening(Scene):
    def construct(self):
        title = Title("Original modell")
        self.play(Write(title))
        diff_eq = MathTex(
            r"x'(t) =& \sigma (y(t) - x(t)) \\ y'(t) =& x(t)(\rho - z(t)) - y(t) \\ z'(t) =& x(t) y(t) - \beta z(t)"
        ).scale(1).move_to(ORIGIN)
        self.play(Write(diff_eq))
        self.wait(5)
        self.play(diff_eq.animate.to_edge(LEFT, buff=1))
        self.wait(1)

        original_params = MathTex(
            r"\sigma &= 10 \\ \rho &= 28 \\ \beta &= \frac{8}{3}"
        ).to_edge(RIGHT, buff=1)
        self.play(Write(original_params))
        self.wait(5)

class EqPoints(Scene):
    def construct(self):
        new_params = MathTex(
            r"\sigma &= \alpha \\ \rho &= \beta \\ \beta &= \gamma"
        )

        diff_eq = MathTex(
            r"x' &= \alpha y - \alpha x \\ y' &= x(\beta - z) - y \\ z' &= xy - \gamma z"
        )
        diff_eq_zero = MathTex(
            r"x' &= \alpha y - \alpha x = 0 \\ y' &= x(\beta - z) - y = 0 \\ z' &= xy - \gamma z = 0"
        )
        diff_eq_zero_clean = MathTex(
            r"y - x &= 0 \\ x(\beta - z) - y &= 0 \\ xy - \gamma z &= 0"
        )

        self.play(Write(new_params))
        self.wait(1)
        self.play(Unwrite(new_params))
        self.wait(1)
        self.play(Write(diff_eq))
        self.wait(2)
        self.play(Transform(diff_eq, diff_eq_zero))
        self.wait(2)
        self.play(Transform(diff_eq_zero, diff_eq_zero_clean))
        self.wait(2)

class Solutions(Scene):
    def construct(self):
        sols = MathTex(
            r"""
                P_{1} &= \left(0, 0, 0\right) \\
                P_{2} &= \left(\sqrt{ \gamma(\beta - 1) },\; \sqrt{ \gamma(\beta - 1) },\; \beta - 1\right) \\
                P_{3} &= \left(-\sqrt{ \gamma(\beta - 1) },\; -\sqrt{ \gamma(\beta - 1) },\; \beta - 1\right)
            """
        )
        self.play(Write(sols))
        self.wait(2)

class Stability(Scene):
    def construct(self):
        eq = MathTex(
            r"""
                f(x, y, z) = \begin{bmatrix} \alpha y - \alpha x \\
                x(\beta - z) - y \\
                xy - \gamma z\end{bmatrix}
            """
        )
        eq_deriv = MathTex(
            r"""
                f'(x, y, z) = \begin{bmatrix} -\alpha & \alpha & 0 \\
                \beta - z & -1 & -x \\
                y & x & -\gamma\end{bmatrix}
            """
        )
        det = MathTex(
            r"""
                \det(f'(x, y, z) - \lambda I) = \det \left(
                \begin{bmatrix}
                -\alpha - \lambda & \alpha & 0 \\
                \beta - z & -1 - \lambda & -x \\
                y & x & -\gamma - \lambda
                \end{bmatrix}
                \right)
            """
        )
        det_eq = MathTex(
            r"""-(\gamma + \lambda)(-\alpha \beta + \alpha \lambda + \alpha z + \alpha + \lambda ^{2} + \lambda) + x(-\alpha x - \alpha y - \lambda x)"""
        )

        self.play(Write(eq))
        self.wait(2)
        self.play(Unwrite(eq))
        self.wait(0.5)
        self.play(Write(eq_deriv))
        self.wait(2)
        self.play(Unwrite(eq_deriv))
        self.wait(0.5)
        self.play(Write(det))
        self.wait(2)
        self.play(Unwrite(det))
        self.wait(0.5)
        self.play(Write(det_eq))
        self.wait(2)

class SpecialCase(Scene):
    def construct(self):
        title = Title(
            r"\text{Ha } (x, y, z) = (0, 0, 0)"
        )
        quadratic = MathTex(
            r"""
                -\alpha \beta + \alpha \lambda + \alpha + \lambda ^{2} + \lambda &= 0 \\
                \lambda ^{2} + (1 + \alpha)\lambda + \alpha(1 - \beta) &= 0
            """
        )
        sol = MathTex(
            r"""
                \lambda_{1, 2} &= \frac{-(1 + \alpha) \pm \sqrt{ (1 + \alpha)^{2} - 4 \alpha(1 - \beta) }}{2} \\
                \lambda_{3} &= -\gamma
            """
        )

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(quadratic))
        self.wait(2)
        self.play(Unwrite(quadratic))
        self.wait(0.5)
        self.play(Write(sol))
        self.wait(2)

class GeneralCase(Scene):
    def construct(self):
        title = Title(
            "Általános eset"
        )
        eq = MathTex(
            r"""
            \mu ^{3} + (1 + \alpha + \gamma) \mu ^{2} + (\alpha + \beta)\gamma \mu + 2\alpha \gamma(1 - \beta) = 0
            """
        )
        simplified_cubic = MathTex(
            r"x^3 + px + q = 0"
        )
        pq = MathTex(
            r"""
            p &= \frac{3(\alpha + \beta)\gamma - (2\alpha \gamma(1 - \beta))^{2}}{3} \\
            q &= \frac{2(1 + \alpha + \gamma)^{3} - 9(1 + \alpha + \gamma)(\alpha + \beta)\gamma + 27 \cdot 2\alpha \gamma(1 - \beta)}{27}
            """
        )
        cardano = MathTex(
            r"""
            \xi = \sqrt[3]{ \frac{q}{2} + \sqrt{ \frac{q^{2}}{4} + \frac{p^{3}}{27} } } + \sqrt[3]{ \frac{q}{2} - \sqrt{ \frac{q^{2}}{4} + \frac{p^{3}}{27} } }
            """
        )
        sol = MathTex(
            r"""
            \beta < \frac{\alpha(\alpha + \gamma + 3)}{\alpha - \gamma - 1}
            """
        )

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(eq))
        self.wait(2)
        self.play(Unwrite(eq))
        self.wait(0.5)
        self.play(Write(simplified_cubic))
        self.wait(2)
        self.play(Unwrite(simplified_cubic))
        self.wait(0.5)
        self.play(Write(pq))
        self.wait(2)
        self.play(Unwrite(pq))
        self.wait(0.5)
        self.play(Write(cardano))
        self.wait(2)
        self.play(Unwrite(cardano))
        self.wait(0.5)
        self.play(Write(sol))
        self.wait(2)

