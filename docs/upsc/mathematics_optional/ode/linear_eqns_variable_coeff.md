---
id: linear_eqns_variable_coeff
title: Linear Equations Of Second Order With Variable Coeff.
sidebar_label: Linear Equations Of Second Order With Variable Coeff.
---

Is an eqn of the form

$\frac{d^2y}{dx^2} + P(x)\frac{dy}{dx} + Q(x)y = R(x)$

can be solved by following methods:

## Change of the dependent variable when a part of the CF is known

### Method for solving

Method for Finding one integral (soln) in CF by inspection
i.e. one soln $u(x)$ of $(D^2 + P(x)D + Q(x))y = 0$

| Condition Satisfied     | one soln of CF       |
| ----------------------- | -------------------- |
| $a^2 + aP + Q = 0$      | $u = e^{ax}$         |
| $1 + P + Q = 0$         | $u = e^x$            |
| $1 - P + Q = 0$         | $u = e^{-x}$         |
| $m(m - 1) + Pmx + Qx^2$ | $u = x^m (m \geq 2)$ |
| $P + Qx = 0$            | $u = x$              |
| $2 + 2Px + Qx^2$        | $u = x^2$            |

Now assume the GS of given eqn is of the form $y = uv$ where $u$ is obtained as above, now $v$ can be obtained by solving:

$\frac{d^2v}{dx^2} + (P + \frac{2}{u}\frac{u}{x})\frac{dv}{dx} = \frac{R(x)}{u}$
