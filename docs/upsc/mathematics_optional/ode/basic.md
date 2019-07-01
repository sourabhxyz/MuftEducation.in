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
3. $\frac{\partial^2z}{\partial x^2} + 2\frac{\partial^2z}{\partial x \partial y} + \frac{\partial^2z}{\partial y^2}$

### Types of Differential Equations

- Ordinary DE: An eqn involving the derivatives of a dependent variable wrt a single independent variable as in example 1 and 2 above.
- Partial DE: An equation involving the derivatives of a dependent variable wrt more than one independent variable as in example 3 above.

---

**Definition:** An ODE is said to be of order $n$ if the $n$th derivative of the unknown function $y$ is the highest derivative of $y$ in the equation. So example 1 and 2 above are of order 3, 1 resp.

---

So an ODE of order $n$ involving 2 variables is of the form: $f(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^ny}{dx^n}) = 0$

<!-- From now on, unless otherwise mentioned, for this chapter of "ODE", "ODE" will be further abbreviated as "DE" -->

---

**Definition:** The degree (i.e. power) of the highest order derivative involved in a DE, when the DE satisfies the following:

- All derivatives have been made free from radicals (i.e. roots or fractional powers)
- There is no involvement of the derivatives in any fraction.
- There shouldn’t be involvement of highest order derivative as a transcendental function, trigonometric or exponential, etc. The coefficient of any term containing the highest order derivative should just be a function of $x$, $y$, or some lower order derivative.

So, example 1 above is of degree 101 whereas example 2 doesn't satisfy our conditions.
