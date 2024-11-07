from manim import *

class Opening(Scene):
    def construct(self):
        title = Title("Eredeti modell")
        self.play(Write(title))
        diff_eq = MathTex(
            r"""
            x'(t) =& \sigma (y(t) - x(t)) \\
            y'(t) =& x(t)(\rho - z(t)) - y(t) \\
            z'(t) =& x(t) y(t) - \beta z(t)
            """,
            substrings_to_isolate=(r"\sigma", r"\rho", r"\beta")
        ).scale(1).move_to(ORIGIN)
        diff_eq.set_color_by_tex(r"\sigma", RED)
        diff_eq.set_color_by_tex(r"\rho", GREEN)
        diff_eq.set_color_by_tex(r"\beta", BLUE)
        self.play(Write(diff_eq))
        self.wait(5)
        self.play(diff_eq.animate.to_edge(LEFT, buff=1))
        self.wait(1)

        original_params = MathTex(
            r"\sigma &= 10 \\ \rho &= 28 \\ \beta &= \frac{8}{3}",
            substrings_to_isolate=(r"\sigma", r"\rho", r"\beta")
        ).to_edge(RIGHT, buff=1)
        original_params.set_color_by_tex(r"\sigma", RED)
        original_params.set_color_by_tex(r"\rho", GREEN)
        original_params.set_color_by_tex(r"\beta", BLUE)
        self.play(Write(original_params))
        self.wait(5)

class EqPoints1(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúlyi pontok kiszámolása}")
        new_params = MathTex(
            r"\sigma &= \alpha \\ \rho &= \beta \\ \beta &= \gamma"
        )

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(new_params))
        self.wait(1)

class EqPoints2(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúlyi pontok kiszámolása}")
        diff_eq = MathTex(
            r"x' &= \alpha y - \alpha x \\ y' &= x(\beta - z) - y \\ z' &= xy - \gamma z"
        )

        self.add(title)
        self.wait(0.5)
        self.play(Write(diff_eq))
        self.wait(2)

class EqPoints3(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúlyi pontok kiszámolása}")
        diff_eq_zero = MathTex(
            r"x' &= \alpha y - \alpha x = 0 \\ y' &= x(\beta - z) - y = 0 \\ z' &= xy - \gamma z = 0"
        )

        self.add(title)
        self.wait(0.5)
        self.play(Write(diff_eq_zero))
        self.wait(2)

class EqPoints4(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúlyi pontok kiszámolása}")
        diff_eq_zero_clean = MathTex(
            r"y - x &= 0 \\ x(\beta - z) - y &= 0 \\ xy - \gamma z &= 0"
        )

        self.add(title)
        self.wait(0.5)
        self.play(Write(diff_eq_zero_clean))
        self.wait(2)

class EqPointsSolutions(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúlyi pontok kiszámolása}")
        sols = MathTex(
            r"""
                P_{1} &= \left(0, 0, 0\right) \\
                P_{2} &= \left(\sqrt{ \gamma(\beta - 1) },\; \sqrt{ \gamma(\beta - 1) },\; \beta - 1\right) \\
                P_{3} &= \left(-\sqrt{ \gamma(\beta - 1) },\; -\sqrt{ \gamma(\beta - 1) },\; \beta - 1\right)
            """
        )
        self.add(title)
        self.play(Write(sols))
        self.wait(2)

class Stability1(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúly pontok stabilitása}")
        eq = MathTex(
            r"""
                f(x, y, z) = \begin{bmatrix} \alpha y - \alpha x \\
                x(\beta - z) - y \\
                xy - \gamma z\end{bmatrix}
            """
        )

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(eq))
        self.wait(2)

class Stability2(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúly pontok stabilitása}")
        eq_deriv = MathTex(
            r"""
                f'(x, y, z) = \begin{bmatrix} -\alpha & \alpha & 0 \\
                \beta - z & -1 & -x \\
                y & x & -\gamma\end{bmatrix}
            """
        )

        self.add(title)
        self.wait(0.5)
        self.play(Write(eq_deriv))
        self.wait(2)

class Stability3(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúly pontok stabilitása}")
        det = MathTex(
            r"""
                \det(f'(x, y, z) - \lambda I) = \det \left(
                \begin{bmatrix}
                -\alpha - \lambda & \alpha & 0 \\
                \beta - z & -1 - \lambda & -x \\
                y & x & - \gamma - \lambda
                \end{bmatrix}
                \right)
            """,
            substrings_to_isolate=(r"y", r"x")
        )
        # det.set_color_by_tex(r"\lambda", BLUE)

        self.add(title)
        self.wait(0.5)
        self.play(Write(det))
        self.wait(2)

class Stability4(Scene):
    def construct(self):
        title = Title(r"\text{Egyensúly pontok stabilitása}")
        det_eq = MathTex(
            r"""-(\gamma + \lambda)(-\alpha \beta + \alpha \lambda + \alpha z + \alpha + \lambda ^{2} + \lambda) + x(-\alpha x - \alpha y - \lambda x)""",
            substrings_to_isolate=(r"\alpha", r"\lambda")
        )
        det_eq.set_color_by_tex(r"\lambda", BLUE)

        self.add(title)
        self.wait(0.5)
        self.play(Write(det_eq))
        self.wait(2)

class SpecialCase1(Scene):
    def construct(self):
        title = Title(
            r"\text{Ha } (x, y, z) = (0, 0, 0)"
        )
        det_eq = MathTex(
            r"""-(\gamma + \lambda)(-\alpha \beta + \alpha \lambda + \alpha z + \alpha + \lambda ^{2} + \lambda) + x(-\alpha x - \alpha y - \lambda x)""",
            substrings_to_isolate=(r"\alpha", r"\lambda")
        )
        det_eq_subs = MathTex(
            r"""-(\gamma + \lambda)(-\alpha \beta + \alpha \lambda + \alpha 0 + \alpha + \lambda ^{2} + \lambda) + 0(-\alpha 0 - \alpha 0 - \lambda 0)""",
            substrings_to_isolate=(r"\alpha", r"\lambda")
        )
        det_eq.set_color_by_tex(r"\lambda", BLUE)
        det_eq_subs.set_color_by_tex(r"\lambda", BLUE)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(det_eq))
        self.wait(1)
        self.play(Transform(det_eq, det_eq_subs))
        self.wait(2)

class SpecialCase2(Scene):
    def construct(self):
        title = Title(
            r"\text{Ha } (x, y, z) = (0, 0, 0)"
        )
        det_eq_subs = MathTex(
            r"""-(\gamma + \lambda)(-\alpha \beta + \alpha \lambda + \alpha 0 + \alpha + \lambda ^{2} + \lambda) + 0(-\alpha 0 - \alpha 0 - \lambda 0)""",
            substrings_to_isolate=(r"\alpha", r"\lambda")
        )
        quadratic = MathTex(
            r"""
                -\alpha \beta + \alpha \lambda + \alpha + \lambda ^{2} + \lambda &= 0
            """,
            substrings_to_isolate=(r"\alpha", r"\lambda")
        )
        det_eq_subs.set_color_by_tex(r"\lambda", BLUE)
        quadratic.set_color_by_tex(r"\lambda", BLUE)

        self.add(title)
        self.add(det_eq_subs)
        self.wait(0.5)
        self.play(Transform(det_eq_subs, quadratic))
        self.wait(2)

class SpecialCase3(Scene):
    def construct(self):
        title = Title(
            r"\text{Ha } (x, y, z) = (0, 0, 0)"
        )
        quadratic1 = MathTex(
            r"""
                -\alpha \beta + \alpha \lambda + \alpha + \lambda ^{2} + \lambda &= 0
            """,
            substrings_to_isolate=(r"\alpha", r"\lambda")
        )
        quadratic2 = MathTex(
            r"""
                \lambda ^{2} + (1 + \alpha)\lambda + \alpha(1 - \beta) &= 0
            """,
            substrings_to_isolate=(r"\lambda", r"\alpha")
        )
        quadratic1.set_color_by_tex(r"\lambda", BLUE)
        quadratic2.set_color_by_tex(r"\lambda", BLUE)

        self.add(title)
        self.add(quadratic1)
        self.wait(0.5)
        self.play(Transform(quadratic1, quadratic2))
        self.wait(2)

class SpecialCase4(Scene):
    def construct(self):
        title = Title(
            r"\text{Ha } (x, y, z) = (0, 0, 0)"
        )
        sol = MathTex(
            r"""
                \lambda_{1, 2} &= \frac{-(1 + \alpha) \pm \sqrt{ (1 + \alpha)^{2} - 4 \alpha(1 - \beta) }}{2} \\
                \lambda_{3} &= -\gamma
            """,
        )

        self.add(title)
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

