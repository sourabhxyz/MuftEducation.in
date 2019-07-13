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

  Here note that $e^{\frac{-1}{2}\int -2tanxdx} = e^{-log(cosx)} = secx$ which is our given $u$. Thus we can apply our method.

## Soln by changing independent variable

Let $z = f(x)$ then after a bit of work,

$\frac{d^2y}{dz^2} + P_1\frac{dy}{dz} + Q_1y = R_1$ where:

$P_1 = \frac{\frac{d^2z}{dx^2} + P\frac{dz}{dx}}{(\frac{dz}{dx})^2}$

$Q_1 = \frac{Q}{(\frac{dz}{dx})^2}$

$R_1 = \frac{R}{(\frac{dz}{dx})^2}$

### Case 1

Choose $z$ to make $P_1 = 0$ i.e., $\frac{d^2z}{dx^2} + P\frac{dz}{dx} = 0$

$\rightarrow z = \int e^{-\int Pdx}dx$

Now the eqn reduces to $\frac{d^2y}{dz^2} + Q_1y = R_1$

which can be easily solved if $Q_1$ turns out to be a constant or a constant multiplied by $\frac{1}{z^2}$

### Case 2

Choose $z$ such that $Q_1 = a^2$

$\rightarrow a\int dz = \int \sqrt{\pm Q}dx$

Take appropriate sign to make expression under radical positive.

Now the eqn reduces to $\frac{d^2y}{dz^2} + P_1\frac{dy}{dz} + a^2y = R_1$

which can be easily solved provided $P_1$ comes out to be a constant.

**Examples:**

- $x\frac{d^2y}{dx^2} - \frac{dy}{dx} - 4x^3y = 8x^3sin(x^2)$

  $\Rightarrow \frac{d^2y}{dx^2} - \frac{1}{x}\frac{dy}{dx} - 4x^2y = 8x^2sin(x^2)$

  $\Rightarrow z = \int e^{-\int Pdx}dx = x^2/2$

  $\Rightarrow Q_1 = -4, R_1 = 8sin(x^2) = 8sin(2z)$

  $\Rightarrow PI = \frac{8sin(2z)}{D^2 - 4} = -sin(2z) = -sin(x^2)$

  $\Rightarrow y = c_1e^{x^2} + c_2e^{-x^2} - sin(x^2)$

- Transform the DE $xy'' -y' + 4x^3y = x^5$ into $z$ as independent variable where $z = x^2$ and solve it.

  $\frac{dy}{dx} = \frac{dy}{dz}\frac{dz}{dx} = 2x\frac{dy}{dz}$

  $\frac{d^2y}{dx^2} = 2\frac{dy}{dz} + 2x\frac{d^2y}{dz^2}\frac{dz}{dx}$

  $= 2\frac{dy}{dz} + 4x^2\frac{d^2y}{dz^2}$

  Now using this, it will reduce in a good solvable form.

## Method of variation of parameters

1. Write the given equation in the standard form $y'' + Py' + Qy = R$.
2. Find the soln of corresponding homogeneous eqn. Let it be $y_c = c_1u(x) + c_2v(x)$ by using methods discussed before.
3. Let the PI of the given eqn be $y_p = A(x)u + B(x)v$ where $A = -\int \frac{vR}{W(u, v)}dx$ and $B = \int \frac{uR}{W(u, v)}dx$ are functions of $x$.
4. GS of the given eqn is $y = y_c + y_p$

**Examples:**

- $((x - 1)D^2 - xD + 1)y = (x - 1)^2$

  $\rightarrow (D^2 - \frac{x}{x - 1}D + \frac{1}{x - 1})y = x - 1$

  It can be seen by inspection that $y = e^x \text{ and } y = x$ are soln of corresponding homogeneous eqn. Therefore

  $\rightarrow y_c = c_1e^x + c_2x$

  And after some calculation

  $y_p = -(1 + x + x^2)$

  $GS = y_c + y_p$
