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
- There is no involvement of the derivatives in any denominator of a fraction.
- There shouldn’t be involvement of highest order derivative as a transcendental function, trigonometric or exponential, etc. The coefficient of any term containing the highest order derivative should just be a function of $x$, $y$, or some lower order derivative.

---

So, example 1 above is of degree 101 whereas example 2 doesn't satisfy our conditions and example 3 has degree 3.

**Examples:**

- $c = \frac{(\sqrt{x} + (\frac{dy}{dx})^2)^{3/2}}{\frac{d^2y}{dx^2}}$ --> Order = degree = 2
- $(y^{'''})^{4/3} + sin(\frac{dy}{dx}) + xy = x$ --> Order = 3, degree = 4
- $(y^{'''})^{1/2} - 2(y^{'})^{1/4} + xy = 0$ --> Take $(y^{'})^{1/4}$ to one side and take to the 4th power on both sides and then lhs would have remaining radicals like $4a^3b + 4ab^3 = 4ab(a^2 + b^2)$ (can be seen by doing $(a + b)^4 = (a^2 + b^2 + 2ab)(a^2 + b^2 + 2ab)$) which can now be removed by squaring both sides. --> Order = 3, degree = 4
- $(y^{'''})^{4/3} + (y^{'})^{1/5} + 4 = 0$ ~~Since $GCD(3, 5) = 1$ that implies, order = 3, degree = 20 (simply take $1/5$ power term to one side then raise to the 5th power then take $1/3$ term common on one side and raise to the third power)~~ Tedious, yet to calculate.
- $(y^{'''})^{3/2} + (y^{'''})^{2/3} = 0$ Order = 3 but don't say degree = 9 yet as both the terms are of same order and in the end we will have $l^9 = l^4 \Rightarrow l^5 = 0$ so degree equals 5 (?) (although it is still a subjective answer and in my opinion answer should be 9).

---

**Definition:** A DE is said to be **linear** if:-

1. The dependent variable and all its derivatives occur in the first degree only.
2. No product of dependent variable or derivatives occur.

So, in general a linear differential equation involving two variables and of $n$th order is of the form:-

$y^{(n)} + P_1(x) * y^{(n - 1)} + \dots + P_n(x) * y = Q(x)$

Also if $Q(x) = 0$ then it is called as **Homogeneous Linear DE** o/w **Non Homogeneous Linear DE**.

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

**Definition: (Soln to a DE)** Any relation between the dependent and independent variables which when substituted in the DE reduces it to an identity is called a **soln** or **integral** or **primitive** of the DE.

---

**Definition: (General Soln)** The soln of a DE in which the number of arbitrary constants is equal to the order of the DE.

**Example:** $y = ce^{2x}$ is a GS of the DE $y^{'} = 2y$

---

**Definition: (Particular Soln)** A solution obtained by giving particular values to one or more of the $n$ arbitrary constants in the general soln. So if we let $c = 1$ in the above example, we get a particular soln.

---

**Definition: (Singular Soln)**

An eqn $\Psi(x, y) = 0$ is called **singular soln** of the DE $F(x, y, \frac{dy}{dx}, \dots, \frac{d^ny}{dx^n}) = 0$ if:-

1. $\Psi(x, y) = 0$ is a soln of the given DE.
2. $\Psi(x, y) = 0$ doesn't contain arbitrary constants.
3. $\Psi(x, y) = 0$ cannot be obtained by giving particular values to arbitrary constants in the general soln.

Example: $y = (x + c)^2$ is the general soln of $(dy/dx)^2 - 4y = 0$, notice that $y = 0$ is as well the soln of this eqn which cannot be obtained by any choice of $c$. Hence $y = 0$ is a singular soln.

Note: The complete soln to a DE of the $n$th order contains exactly $n$ arbitrary constants.

---

**Definition: (Family of plane curves)** For each given set of real numbers $c_1, c_2, \dots, c_n$ the equation $\phi(x, y, c_1, \dots, c_n) = 0$ represents a curve in x-y plane.

For different sets of real values of $c_1, \dots, c_n$ the eqn $\phi(x, y, c_1, \dots, c_n) = 0$ represents infinitely many curves. The set of all these curves is called $n$ parameter family of curves and $c_1, \dots, c_n$ are called parameters of the family.

**Example:** The set of circles defined by $(x - c_1)^2 + (y - c_2)^2 = c_3$ is three parameter family where $c_3 \geq 0$

---

## Formation of DE

### Working Rule

To form the DE from a given eqn in $x$ and $y$, containing $n$ arbitrary constants:

1. Write down the given eq., differentiate wrt x successively till the count reaches the number of arbitrary constants ($n$).
2. Eliminate the arbitrary constants from the ($n + 1$) eqn's obtained in above step.

**Example:** $y = ae^x + be^{-x} + c \cos{x} + d\sin{x}$ which arbitrary constants are $(a, b, c, d)$

**Soln** is $y^{(4)} = y$
