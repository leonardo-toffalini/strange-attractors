# Strange attractors

### List of attractors visualized
#### Lorenz attractor
Defining differential equation:
```math
\begin{align}
x'(t) &= \sigma (y(t) - x(t)) \\
y'(t) &= x(t)(\rho - z(t)) - y(t) \\
z'(t) &= x(t) y(t) - \beta z(t) \\
\begin{align}
```

https://github.com/user-attachments/assets/0c213ce9-a2c9-4c8d-b9c5-7ead485578b2

#### Thomas attractor
Defining differential equation:
```math
\begin{align}
x'(t) &= \sin y - bx \\
y'(t) &= \sin z - by \\
z'(t) &= \sin x - bz
\end{align}
```

#### Aizawa attractor
Defining differential equation:
```math
\begin{align}
x'(t) &= (z-b)x - dy \\
y'(t) &= dx + (z-b)y \\
z'(t) &= c + az - \frac{z^3}{3} - (x^2 + y^2)(1 + ez) + fzx^3
\end{align}
```

https://github.com/user-attachments/assets/717b6d5a-1e3f-4e97-9055-9340adebebab

### Dependencies
The animation engine used to visualize the attractors is [Manim](https://www.manim.community/), to install it run the following command:
```
conda install manim
```


