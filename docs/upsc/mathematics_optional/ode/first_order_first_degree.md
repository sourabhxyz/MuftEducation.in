---
id: first_order_first_degree
title: Soln of DE of the first order and first degree
sidebar_label: Soln of DE of the first order and first degree
---

---

**Definition:** A DE of first order and first degree is an eqn of the form $\frac{dy}{dx} = \frac{f(x, y)}{g(x, y)}$ or $Mdx + Ndy = 0$ where $M$ and $N$ are functions of $x$ and $y$.

---

There are four methods to solve these eqn's:-

## Variables separable

If in an eqn it is possible to get all the functions of $x$ and $dx$ to one side and all the functions of $y$ and $dy$ to another side then the variables are said to be separable.

### Working rule

1. Consider the eqn $\frac{dy}{dx} = XY$
2. Modify to get $\frac{dy}{Y} = Xdx$ _(Now the variables have been seperated)_
3. Integrate both sides and don't forget to add arbitrary constant (only to one side as adding to both sides will ultimately lead to only one arbitrary constant), soln without this arbitrary const is wrong as it is not the general soln.

**Example:** $\frac{dy}{dx} = e^{x + y} + x^2e^y = e^{y}(e^x + x^2) \Rightarrow dye^{-y} = dx(e^x + x^2)$ solve and get $e^{-y} + e^{x} + x^3/3 + c = 0$

### Second Form

Equations reducible to the form in which variables can be separated.

Equations of the form $\frac{dy}{dx} = f(ax + by + c)$ can be reduced to the form in which the variables are separated.

Put $ax + by + c = z \Rightarrow a + b\frac{dy}{dx} = \frac{dz}{dx} \Rightarrow \frac{dy}{dx} = \frac{1}{b} (\frac{dz}{dx} - a) \Rightarrow \frac{1}{b} (\frac{dz}{dx} - a) = f(z)$

**Example:** $\frac{dy}{dx} = cos(x + y) + sin(x + y)$

**Sol:** $x + y = z \Rightarrow 1 + y^{'} = z^{'}$

$\Rightarrow z^{'} - 1 = cos(z) + sin(z) \Rightarrow z^{'} = 2cos^2(z/2) + 2sin(z/2)cos(z/2) = 2cos(z/2)(sin(z/2) + cos(z/2))$

$\Rightarrow \frac{dz  sec^2(z/2)}{2(tan(z/2) + 1)} = dx$ integrate and get $log(1 + tan((x + y)/2)) = x + c$

### Third Form

Differential eqns of the form

$\frac{dy}{dx} = \frac{(ax + by) + c}{m(ax + by) + c_1}$ or $\frac{dy}{dx} = \frac{m(ax + by) + c}{ax + by + c_1}$ just put $ax + by = z$ and solve like second form.

## Homogenous DE

### Homogenous function

A function $f(x, y)$ is said to be a homogenous function of degree $'n'$ in $x \text{ and } y$ if $f(kx, ky) = k^n f(x, y)$

**Examples:**

- $f(x, y) = \frac{\sqrt[3]{x} + \sqrt[3]{y}}{x + y}$ $\Rightarrow f(kx, ky) = k^{1/3 - 1}\frac{\sqrt[3]{x} + \sqrt[3]{y}}{x + y}$ $\Rightarrow f(x, y) \text{ is homogenous of degree } -2/3$
- $f(x, y) = \frac{\sqrt{x} + \sqrt{y}}{\sqrt{x} - \sqrt{y}}$ is homogenous of degree 0.

:::tip Note
If $f(x, y)$ is homogenous with degree 0 then $f(x, y)$ is a function of $y/x \text{ or } x/y$
:::

### Homogenous DE

A DE is said to be homogenous if it can be written in the form $\frac{dy}{dx} = \frac{f(x, y)}{g(x, y)}$ where $f \text{ and } g$ are homogenous functions of some degree in $x \text{ \& } y$

### Working Rule

1. Put $y = vx \Rightarrow \frac{dy}{dx} = v + x\frac{dv}{dx}$
2. Use this to separate variables

**Examples:**

- $\frac{dy}{dx} = \frac{y}{x} + e^{\frac{y}{x}}$ just put $y = vx$ and solve.

### Non Homogenous DE or Eqns Reducible To Homo. Form

Consider DE's of the form $$\frac{dy}{dx} = \frac{ax + by + c}{a_1x + b_1y + c_1}$$

#### Case 1

$\frac{a}{a_1} \neq \frac{b}{b_1} \text{ i.e. } ab_1 \neq ba_1$

**Working rule:**

Put $x = X + h, y = Y + k \text{ where } h \text{ and } k \text{ are constants }$

$\Rightarrow dx = dX \text{ \& } dy = dY \Rightarrow \frac{dy}{dx} = \frac{dY}{dX} = \frac{a(X + h) + b(Y + k) + c}{a_1(X + h) + b_1(Y + k) + c_1}$

$$ = \frac{aX + bY + (ah + bk + c)}{{a_1X + b_1Y + (a_1h + b_1k + c_1)}}$$

Choosing $h$ and $k$ such that $ah + bk + c = a_1h + b_1k + c_1 = 0 \Rightarrow \frac{dY}{dX} = \frac{aX + bY}{a_1X + b_1Y}$ which is homogenous.

#### Case 2

$\frac{a}{a_1} = \frac{b}{b_1}$ then it reduces to a third form of variable separable.

## Exact Equations

---

**Definition:** The DE $M(x, y)dx + N(x, y)dy = 0$ is called an exact DE if $Mdx + Ndy = 0$ is an exact derivative of $x$ and $y$, i.e. $Mdx + Ndy = du = \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy$ where u is a function of $x$ and $y$, from $du = 0$ we get by integrating $u(x, y) = c$.

---

**Working Rule:**

- The DE $Mdx + Ndy = 0$ is an exact DE **iff** $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \text{ from } (u_{xy} = u_{yx})$ (Note that this will only hold true if $u$ is continuous and its first order derivatives are as well continuous)
  This equality condition is not only necessary but also sufficient (proof omitted)
- To obtain GS either do
  1.  $u = \int Mdx + k(y)$ and then using $u_y = N$ get an eqn in $\frac{dk}{dy}$ to solve for $k$.
  2.  $u = \int Ndy + l(x)$ and solve like above.

:::warning Warning
As evident from this theory, we cannot solve by just doing $Mdx = -Ndy$ then integrating each side wrt $x, y$ resp. Also eqn may not even be exact! (wanted to mention this point in variable separation section)
:::

:::caution Caution
The GS is **not** given by $\int Mdx \text{ (treat y as const)} + \int (\text{ terms in N not containing x})dy = c$

This might work in some cases only.
:::

### Integrating Factor

Sometimes $Mdx + Ndy = 0$ is not exact but can be made so by multiplying throughout by a suitable non zero $\mu(x, y)$. This multiplier is called the integrating factor.

:::tip Note
A DE can have more than one integrating factor like $1/x^2, 1/y^2, 1/xy, 1/(x^2 + y^2), 1/(x^2 - y^2)$ are all integrating factors of $ydx - xdy = 0$
:::

:::note Remember
If we have situation like this $l(x)dx + m(y)dy + d(N(x, y)) = 0$ then we can simply do $L(x) + M(y) + N(x, y) = c$
:::

**Examples:**

- $\frac{dy}{dx} + \frac{ax + hy + g}{hx + by + f} = 0$

  Sol: $\frac{\partial M}{\partial y} = h = \frac{\partial N}{\partial x}$, Answer: $ax^2/2 + hyx + gx + by^2/2 + fy = c$

- $\frac{xdy - ydx}{x^2 + y^2} = xdx \Rightarrow d(tan^{-1}(y/x) = xdx \Rightarrow tan^{-1}(y/x) = x^2/2 + c$

- $ydx -xdy + (1 + x^2)dx + x^2sinydy = 0 \Rightarrow \frac{ydx - xdy}{x^2} + (1/x^2 + 1)dx + sinydy = 0$

  Clubbing $dx$ and $dy$ terms together (was of no use though), we get $-y/x + -1/x + x + k(y) = u \Rightarrow -1/x + k^{'}y = -1/x + siny \Rightarrow k(y) = -cos(y) + c^*$

  Now using $u = c$ we get $-y/x -1/x + x -cosy = c^{'}$

- $xdy = (y + xcos^2(y/x))dx \Rightarrow \frac{xdy - ydx}{x^2} = \frac{cos^2(y/x)}{x}dx$

  $\Rightarrow \frac{sec^2(y/x)(xdy - ydx)}{x^2} = dx/x \Rightarrow tan(y/x) = log(x) + c$

- $(xy^2 + 2x^2y^3)dx + (x^2y - x^3y^2)dy = 0$

  $\Rightarrow ydx + xdy + 2xy^2dx - x^2ydy = 0$

  $\Rightarrow \frac{ydx + xdy}{x^2y^2} \text{ (this is now in exact form,}$

  $ \text{can be verified thus it should be kept in mind that }$
  $ x^2y^2 \text{ is an integrating factor of }ydx + xdy$)
  $+ 2dx/x \text{ (wasn't able to do anything rather than making it free from y) } - dy/y = 0$

  Now getting answer is easy, which is $-1/xy + 2log(x) - log(y) = c$

- $xdx + ydy + (x^2 + y^2)dy = 0$

  $\Rightarrow \frac{xdx + ydy}{x^2 + y^2} = -dy \Rightarrow log(x^2 + y^2)/2 + y = c$

- $x^2dy/dx + xy = \sqrt{1 - x^2y^2}$

  $\Rightarrow x\frac{xdy + ydx}{dx} = \sqrt{1 - (xy)^2}$

  $\Rightarrow \frac{d(xy)}{\sqrt{1 - (xy)^2}} = dx/x$

  $\Rightarrow sin^{-1}(xy) - log(x) = c$

### Methods for finding Integrating Factor

#### Method 1

If $Mdx + Ndy = 0$ is homogenous and $Mx + Ny \neq 0$ then $\frac{1}{Mx + Ny}$ is an IF.

**Example:** $x^2ydx - (x^3 + y^3)dy = 0$, IF is $\frac{1}{x^3y - x^3y - y^4} = -1/y^4 \neq 0$ although this same problem can be solved with the homogenous theory discussed before.

#### Method 2

If $Mdx + Ndy = 0$ is such that $M = yf_1(x, y)$ and $N = xf_2(x, y)$ and $Mx - Ny \neq 0$ then $\frac{1}{Mx - Ny}$ is an IF.

**Example:** $y(xysin(xy) + cos(xy))dx + x(xysin(xy) - cos(xy))dy = 0$. IF is $1/xy(xysin(xy) + cos(xy) - xysin(xy) + cos(xy)) = 1/2xycos(xy)$

#### Method 3

If $Mdx + Ndy = 0$ is such that $\frac{\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}}{N} = f(x).$ (as usual $f(x)$ can as well be a constant) then IF $= e^{\int f(x)dx}$

**Example:** $(y + y^3/3 + x^2/2)dx + (x + xy^2)dy/4 = 0$

$\Rightarrow f(x) = \frac{1 + y^2 - (1 + y^2)/4}{x(1 + y^2)/4} = 3/x$

$\Rightarrow IF = e^{3log(x)} = x^3$

#### Method 4

If $Mdx + Ndy = 0$ is such that $\frac{\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}}{M} = f(y).$ ($f(y)$ can as well be a constant) then IF $= e^{\int f(y)dy}$

#### Method 5

If $Mdx + Ndy = 0$ can be put in the form of $x^{\alpha_1} y^{\beta_1} (m_1ydx + n_1xdy) + x^{\alpha_2} y^{\beta_2}(m_2ydx + n_2xdy) = 0$ where $\alpha_1, \alpha_2, \beta_1, \beta_2, m_1, m_2, n_1, n_2$ are constants then the IF is $x^hy^k$ where $h$ and $k$ can be obtained by applying the condition that the given eqn must become exact after multiplying by $x^hy^k$.

## Linear Equations

Here linear equation will of the form $\frac{dy}{dx} + P(x)y = Q(x)$.

### Working Rule

1. Find IF = $e^{\int P(x)dx}$
2. GS is $y \cdot IF = \int (Q \cdot IF) dx + c$

**Examples:**

1. $x\frac{d^2y}{dx^2} + \frac{dy}{dx} + 1 = 0$ Put $\frac{dy}{dx} = t$ we get

   $\frac{dt}{dx} + \frac{t}{x} = \frac{-1}{x}$ Now solve as mentioned.

2. $(1 + y^2) = (tan^{-1}y - x)\frac{dy}{dx}$

   $\Rightarrow \frac{dx}{dy} + \frac{x}{1 + y^2} = \frac{tan^{-1}y}{1 + y^2}$ Now solve as mentioned.

### Equations Reducible to Linear Form

1. $f'(y)dy/dx + P(x)f(y) = Q(x)$

   Put $f(y) = v \Rightarrow f'(y)dy/dx = dv/dx$

   $\Rightarrow dv/dx + Pv = Q$

2. $f'(x)dx/dy + P(y)f(x) = Q(y)$ Proceed like above

3. **Bernoulli's Equation:**

   $dy/dx + P(x)y = Q(x)y^n$ _Note:_ $n \neq 0$ and $n \neq 1$

   _(or)_

   $dx/dy + P(y)x = Q(y)x^n$ with similar conditions

   **Working Rule:**

   $y^{-n}dy/dx + P(x)y^{1 - n} = Q(x)$

   put $y^{1 - n} = z$

   $\Rightarrow (1 - n)y^{-n}dy/dx = dz/dx$

   $\Rightarrow dz/dx + (1 - n)P(x)z = (1 - n)Q(x)$ Which is linear.

   **Examples:**

   - $dz/dx + zlog(z)/x = z(log(z))^2/x^2$

     Put $log(z) = t \Rightarrow z = e^t$

     $\Rightarrow e^tdt/dx + e^tt/x = e^tt^2/x^2 \Rightarrow dt/dx + t/x = t^2/x^2$

     Now solve. Ans: $1/(xlog(z)) = 1/(2x^2) + c$

   - $\frac{dy}{dx}(x^2y^3 + xy) = 1$

     $\Rightarrow dx/dy = x^2y^3 + xy$

     $\Rightarrow dx/dy - xy = x^2y^3$ Now solve.

   - $dy/dx + 1/x = e^y/x^2$

     $\Rightarrow e^{-y}dy/dx + e^{-y}/x = 1/x^2$ Put $e^{-y} = t$ and solve.

     Ans: $e^{-y}/x = 1/2x^2 + c$
