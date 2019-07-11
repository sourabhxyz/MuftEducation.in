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

$\frac{d^2v}{dx^2} + (P + \frac{2}{u}\frac{du}{dx})\frac{dv}{dx} = \frac{R(x)}{u}$

**Examples:**

- $xy'' - (2x - 1)y' + (x - 1)y = 0$

  $\rightarrow y'' - (2 - 1/x)y' + (1 - 1/x)y = 0$

  $\rightarrow u = e^x$

  $\rightarrow \frac{d^2v}{dx^2} + (-2 + 1/x + 2e^{-x}e^{x})\frac{dv}{dx} = 0$

  $\rightarrow \frac{dt}{dx} + t/x = 0$

  $\rightarrow log(t) = -log(x) + c$

  $\rightarrow tx = c_1$

  $\rightarrow v = c_1log(x) + c_2$

:::warning Warning
Here from "part of soln" means that $u(x)$ is a soln of the corresponding homogeneous eqn. Thus if in general we are given $y = u(x)v(x)$ where $u(x)$ is given, we **cannot** apply this method unless corresponding homogeneous eqn turns out to be zero when substituting $y = u(x)$ in it.
:::

## Changing the dependent variable and removal of the first order derivative

i.e. Reduce $y'' + P(x)y' + Q(x)y = R(x)$ to the form $\frac{d^2v}{dx^2} + Iv = S$ which is called as the **normal form** of the given eqn.

### Method for solving

1. Write the given eqn in the standard form $y'' + P(x)y' + Q(x)y = R(x)$
2. To remove the first order derivative we choose $u = e^{\frac{-1}{2}\int Pdx}$
3. Assume the GS is $y = uv$, where $v$ is given by the normal form $\frac{d^2v}{dx^2} + Iv = S$ where $I = Q - \frac{1}{4}P^2 - \frac{1}{2}\frac{dP}{dx}$ and $S = \frac{R}{u}$

**Examples:**

- $y'' -4xy' + (4x^2 - 1)y = -3e^{x^2}sin(2x)$

  $\Rightarrow u = e^{x^2}$

  $\Rightarrow I = 4x^2 - 1 -\frac{1}{4}16x^2 - \frac{1}{2}(-4) = 1$

  $\Rightarrow S = -3sin(2x)$

  $\Rightarrow \frac{d^2v}{dx^2} + v = -3sin(2x)$

  $\Rightarrow PI = -3sin(2x)/(D^2 + 1) = sin(2x)$

  $\Rightarrow CF = c_1cos(x) + c_2sin(x)$

  $\Rightarrow y = e^{x^2}(CF + PI)$

- Make use of the transformation $y(x) = v(x)sec(x)$ to obtain the soln of $y'' -2tanxy' + 5y = 0$, where $y(0) = 0, y'(0) = \sqrt{6}$

  Here not that $e^{\frac{-1}{2}\int -2tanxdx} = e^{-log(cosx)} = secx$ which is our given $u$. This we can apply our method.
