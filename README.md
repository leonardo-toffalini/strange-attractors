# Strange attractors

### List of attractors visualized
#### Lorenz attractor
Defining differential equation:
$$\begin{align}
x'(t) &= \sigma (y(t) - x(t)) \\
y'(t) &= x(t)(\rho - z(t)) - y(t) \\
z'(t) &= x(t) y(t) - \beta z(t) \\
\begin{align}$$

<video width="320" height="240" controls>
  <source src="videos/LorenzAttractor.mp4" type="video/mp4">
</video>

#### Thomas attractor
Defining differential equation:
$$\begin{align}
x'(t) = \sin y - bx \\
y'(t) = \sin z - by \\
z'(t) = \sin x - bz
\end{align}$$

#### Aizawa attractor
Defining differential equation:
$$\begin{align}
x'(t) = (z-b)x - dy \\
y'(t) = dx + (z-b)y \\
z'(t) = c + az - \frac{z^3}{3} - (x^2 + y^2)(1 + ez) + fzx^3
\end{align}$$

<video width="320" height="240" controls>
  <source src="videos/AizawaAttractor.mp4" type="video/mp4">
</video>

### Dependencies
The animation engine used to visualize the attractors is [Manim](https://www.manim.community/), to install it run the following command:
```
conda install manim
```


