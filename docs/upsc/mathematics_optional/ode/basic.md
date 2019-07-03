---
id: basic
title: Basic
sidebar_label: Basic
---

## Differential Equations

---

**Definition:** An equation involving derivatives of a dependent variable wrt one or more independent variables

---

**Examples:**

1. $\frac{d^3y}{dx^3}^{101} + P(x)\frac{dy}{dx}^{202} = Q(y)$
2. $sin(\frac{dy}{dx}) = x^{10}$
3. $\frac{\partial^2z}{\partial x^2} + 2\frac{\partial^2z}{\partial x \partial y} + \frac{\partial^2z}{\partial y^2}^3$

### Types of Differential Equations

- Ordinary DE: An eqn involving the derivatives of a dependent variable wrt a single independent variable as in example 1 and 2 above.
- Partial DE: An equation involving the derivatives of a dependent variable wrt more than one independent variable as in example 3 above.

---

**Definition:** The order of the highest order derivative involved in a DE is called the order of the DE. So example 1, 2 and 3 above are of order 3, 1 and 2 resp.

---

So an ODE of order $n$ involving 2 variables is of the form: $f(1, x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^ny}{dx^n}) = 0$

<!-- From now on, unless otherwise mentioned, for this chapter of "ODE", "ODE" will be further abbreviated as "DE" -->

---

**Definition:** The degree (i.e. power) of the highest order derivative involved in a DE, when the DE satisfies the following:

- All derivatives have been made free from radicals (i.e. roots or fractional powers)
- There is no involvement of the derivatives in any fraction.
- There shouldn’t be involvement of highest order derivative as a transcendental function, trigonometric or exponential, etc. The coefficient of any term containing the highest order derivative should just be a function of $x$, $y$, or some lower order derivative.

---

So, example 1 above is of degree 101 whereas example 2 doesn't satisfy our conditions and example 3 has degree 3.

**Examples:**

- $c = \frac{(\sqrt{x} + (\frac{dy}{dx})^2)^{3/2}}{\frac{d^2y}{dx^2}}$ --> Order = degree = 2
- $(y^{'''})^{4/3} + sin(\frac{dy}{dx}) + xy = x$ --> Order = 3, degree = 4
- $(y^{'''})^{1/2} - 2(y^{'})^{1/4} + xy = 0$ --> Take $(y^{'})^{1/4}$ to one side and take to the 4th power on both sides and then lhs would have remaining radicals like $4a^3b + 4ab^3 = 4ab(a^2 + b^2)$ (can be seen by doing $(a + b)^4 = (a^2 + b^2 + 2ab)(a^2 + b^2 + 2ab)$) which can now be removed by squaring both sides. --> Order = 3, degree = 4
- $(y^{'''})^{4/3} + (y^{'})^{1/5} + 4 = 0$ Since $GCD(3, 5) = 1$ that implies, order = 3, degree = 60 (simply take $1/5$ power term to one side then raise to the 5th power then take $1/3$ term common on one side and raise to the third power)
- $(y^{'''})^{3/2} + (y^{'''})^{2/3} = 0$ Order = 3 but don't say degree = 9 yet as both the terms are of same order and in the end we will have $l^9 = l^4 \Rightarrow l^5 = 0$ so degree equals 5 (?) (although it is still a subjective answer and in my opinion answer should be 9).

---

**Definition:** A DE is said to be **linear** if:-

1. The dependent variable and all its derivatives occur in the first degree only.
2. No product of dependent variable or derivatives occur.

So, in general a linear differential equation involving two variables and of $n$th order is of the form:-

$y^{n} + P_1(x) * y^{n - 1} + \dots + P_n(x) * y = Q(x)$

---

**Examples:**

- $\frac{dy}{dx} = x + sin(x)$
- $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial x \partial y}$

---

**Definition:** A DE is said to be **non linear** if it is not linear.

---

**Examples:**

- $y = \sqrt{x}\frac{dy}{dx} + \frac{k}{\frac{dy}{dx}}$
- $\frac{dx}{dt}^3 + \frac{d^2x}{dt} = e^t$

---

**Definition: (Soln to a DE)** Any relation between the dependent and independent variables which when substitute in the DE reduces it to an identity is called a **soln** or **integral** or **primitive** of the DE.

---

**Definition: (General Soln)** The soln of a DE in which the number of arbitrary constants is equal to the order of the DE.

**Example:** $y = ce^{2x}$ is a GS of the DE $y^{'} = 2y$

---

**Definition: (Particular Soln)** A solution obtained by giving particular values to the arbitrary constants in the general soln. So if we let $c = 1$ in the above example, we get a particular soln.

---

**Definition: (Singular Soln)** An eqn $\Psi(x, y) = 0$ is called **singular soln** of the DE $F(x, y, \frac{dy}{dx}, \dots, \frac{d^ny}{dx^n}) = 0$ if:-

1. $\Psi(x, y) = 0$ is a soln of the given DE.
2. $\Psi(x, y) = 0$ doesn't contain arbitrary constants.
3. $\Psi(x, y) = 0$ is not obtained by giving particular values to arbitrary constants in the general soln.

Note: The complete soln to a DE of the $n$th order contains exatcly $n$ arbitrary constants.

---

**Definition: (Family of plane curves)** For each given set of real numbers $c_1, c_2, \dots, c_n$ the equation $\phi(x, y, c_1, \dots, c_n) = 0$ represents a curve in x-y plane.

For different sets of real values of $c_1, \dots, c_n$ the eqn $\phi(x, y, c_1, \dots, c_n) = 0$ represents infinitely many curves. The set of all these curves is called $n$ parameter family of curves and $c_1, \dots, c_n$ are called parameters of the family.

**Example:** The set of circles defined by $(x - c_1)^2 + (y - c_2)^2 = c_3$ is three parameter family where $c_3 \geq 0$

---

## Formation of DE

### Working Rule

To form the DE from a given eqn in $x$ and $y$, containing arbitrary constants:

1. Write down the given eq., differentiate wrt x successively till the count reaches the number of arbitrary constants.
2. Eliminate the arbitrary constants from the eqn's obtained in above step.

**Example:** $y = ae^x + be^{-x} + c \cos{x} + d\sin{x}$ which arbitrary constants are $(a, b, c, d)$

**Soln** is $y^{(4)} = y$

## Soln of DE of the first order and first degree

---

**Definition:** A DE of first order and first degree is an eqn of the form $\frac{dy}{dx} = \frac{f(x, y)}{g(x, y)}$ or $Mdx + Ndy = 0$ where $M$ and $N$ are functions of $x$ and $y$.

---

There are four methods to solve these eqn's:-

### Variables separable

If in an eqn it is possible to get all the functions of $x$ and $dx$ to one side and all the functions of $y$ and $dy$ to another side then the variables are said to be separable.

#### Working rule

1. Consider the eqn $\frac{dy}{dx} = XY$
2. Modify to get $\frac{dy}{Y} = Xdx$ _(Now the variables have been seperated)_
3. Integrate both sides and don't forget to add arbitrary constant (only to one side), soln without this arbitrary const is wrong as it is not the general soln.

**Example:** $\frac{dy}{dx} = e^{x + y} + x^2e^y = e^{y}(e^x + x^2) \Rightarrow dye^{-y} = dx(e^x + x^2)$ solve and get $e^{-y} + e^{x} + x^3/3 + c = 0$

#### Second Form

Equations reducible to the form in which variables can be separated.

Equations of the form $\frac{dy}{dx} = f(ax + by + c)$ can be reduced to the form in which the variables are separated.

Put $ax + by + c = z \Rightarrow a + b\frac{dy}{dx} = \frac{dz}{dx} \Rightarrow \frac{dy}{dx} = \frac{1}{b} (\frac{dz}{dx} - a) \Rightarrow \frac{1}{b} (\frac{dz}{dx} - a) = f(z)$

**Example:** $\frac{dy}{dx} = cos(x + y) + sin(x + y)$

**Sol:** $x + y = z \Rightarrow 1 + y^{'} = z^{'}$

$\Rightarrow z^{'} - 1 = cos(z) + sin(z) \Rightarrow z^{'} = 2cos^2(z/2) + 2sin(z/2)cos(z/2) = 2cos(z/2)(sin(z/2) + cos(z/2))$

$\Rightarrow \frac{dz  sec^2(z/2)}{2(tan(z/2) + 1)} = dx$ integrate and get $log(1 + tan((x + y)/2)) = x + c$

#### Third Form

Differential eqns of the form

$\frac{dy}{dx} = \frac{(ax + by) + c}{m(ax + by) + c_1}$ or $\frac{dy}{dx} = \frac{m(ax + by) + c}{ax + by + c_1}$ just put $ax + by = z$ and solve like second form.

### Homogenous DE

#### Homogenous function

A function $f(x, y)$ is said to be a homogenous function of degree $'n'$ in $x \text{ and } y$ if $f(kx, ky) = k^n f(x, y)$

**Examples:**

- $f(x, y) = \frac{\sqrt[3]{x} + \sqrt[3]{y}}{x + y}$ $\Rightarrow f(kx, ky) = k^{1/3 - 1}\frac{\sqrt[3]{x} + \sqrt[3]{y}}{x + y}$ $\Rightarrow f(x, y) \text{ is homogenous of degree } -2/3$
- $f(x, y) = \frac{\sqrt{x} + \sqrt{y}}{\sqrt{x} - \sqrt{y}}$ is homogenous of degree 0.

:::tip Note
If $f(x, y)$ is homogenous with degree 0 then $f(x, y)$ is a function of $y/x \text{ or } x/y$
:::

#### Homogenous DE

A DE is said to be homogenous if it can be written in the form $\frac{dy}{dx} = \frac{f(x, y)}{g(x, y)}$ where $f \text{ and } g$ are homogenous functions of some degree in $x \text{ \& } y$

#### Working Rule

1. Put $y = vx \Rightarrow \frac{dy}{dx} = v + x\frac{dv}{dx}$
2. Use this to separate variables

**Examples:**

- $\frac{dy}{dx} = \frac{y}{x} + e^{\frac{y}{x}}$ just put $y = vx$ and solve.

#### Non Homogenous DE or Eqns Reducible To Homo. Form

Consider DE's of the form $\frac{dy}{dx} = \frac{ax + by + c}{a_1x + b_1y + c_1}$

##### Case 1

$\frac{a}{a_1} \neq \frac{b}{b_1} \text{ i.e. } ab_1 \neq ba_1$

**Working rule:**

Put $x = X + h, y = Y + k \text{ where } h \text{ and } k \text{ are constants }$

$\Rightarrow dx = dX \text{ \& } dy = dY \Rightarrow \frac{dy}{dx} = \frac{dY}{dX} = \frac{a(X + h) + b(Y + k) + c}{a_1(X + h) + b_1(Y + k) + c_1}$

$ = \frac{aX + bY + (ah + bk + c)}{{a_1X + b_1Y + (a_1h + b_1k + c_1)}}$

Choosing $h$ and $k$ such that $ah + bk + c = a_1h + b_1k + c_1 = 0 \Rightarrow \frac{dY}{dX} = \frac{aX + bY}{a_1X + b_1Y}$ which is homogenous.

##### Case 2

$\frac{a}{a_1} = \frac{b}{b_1}$ then it reduces to a third form of variable separable.

### Exact Equations

---

**Definition:** The DE $M(x, y)dx + N(x, y)dy = 0$ is called an exact DE if $Mdx + Ndy = 0$ is an exact derivative of $x$ and $y$, i.e. $Mdx + Ndy = du = \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy$ where u is a function of $x$ and $y$

---

**Working Rule:**

- The DE $Mdx + Ndy = 0$ is an exact DE if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \text{ from } (u_{xy} = u_{yx})$
- The GS is $\int Mdx \text{ (treat y as const)} + \int (\text{ terms in N not containing x})dy = c$

**Examples:**

1. $\frac{dy}{dx} + \frac{ax + hy + g}{hx + by + f} = 0$

   Sol: $\frac{\partial M}{\partial y} = h = \frac{\partial N}{\partial x}$, Answer: $ax^2/2 + hyx + gx ( = \int Mdx) + by^2/2 + fy ( = \int Ndy ) = c$

2. $(e^y + 1)cosxdx + e^ysinxdy = 0$, Answer: $(e^y + 1)sinx ( = \int Mdx) + 0 = c$

#### Integrating Factor

Sometimes $Mdx + Ndy = 0$ is not exact but can be made so by multiplying throughout by a suitable non zero $\mu(x, y)$. This multiplier is called the integrating factor.

### Linear Equations
