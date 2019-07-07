---
id: linear_eqns_const_coeff
title: Linear Equations With Const. Coeff.
sidebar_label: Linear Equations With Const. Coeff.
---

---
**Definition:**
Linear DE of order $n$ of the form: $d^ny/dx^n + a_1d^{n - 1}y/dx^{n - 1} + \cdots + a_{n - 1}dy/dx + a_ny = Q(x)$

This eqn can be written as $f(D)y = Q \dots (1)$ where

$f(D) = D^n + a_1D^{n - 1} + \dots + a_{n - 1}D + a_n$ 

---

## Homogeneous Eqn

If $Q = 0$ we get Homogeneous Eqn with constant coeff.

## Solving Linear Eqn

Solving this linear eqn is divided into two parts, 

1. First we find the general solution of the corresponding Homogeneous eqn which is also called as Complementary Function (CF) (*Note:* It must contain as many arbitrary constants as the order of the eqn)
2. Next find a particular soln of original eqn which does not contain any arbitrary constant. This is called the Particular Integral (PI).
3. GS = CF + PI.

## Auxiliary Eqn

$f(m) = 0$ is called auxiliary eqn of (1). Clearly it will must have $n$ roots (can be complex).

## Find CF

Consider AE $f(m) = 0$

### Case 1

All roots are real and distinct.

Let $m_1, m_2, \dots, m_n$ be those $n$ roots.

Then $y = e^{m_1x}, y = e^{m_2x}, \dots, y = e^{m_nx}$ are independent solns of homogeneous eqn.

Hence the GS is $y = c_1e^{m_1x} + c_2e^{m_2x} + \dots + c_ne^{m_nx}$ where $c_1, c_2, \dots, c_n$ are our $n$ constants.

**Example:** $(D - m_1)y = 0$

$\Rightarrow m - m_1 = 0, i.e., m = m_1$

$\Rightarrow GS = ce^{m_1x}$

Which was evident as 

$dy/dx = m_1y \Rightarrow dy/y = m_1x$

$\Rightarrow log(y) = m_1x + c$

### Case 2

Same as Case 1 but now two roots are equal.

Let $m_1, m_1, m_3, \dots, m_n$ be those $n$ roots, then GS is

$y = (c_1 + c_2x)e^{m_1x} + c_3e^{m_3x} + \dots + c_ne^{m_nx}$

**Example:** $(D - m_1)^2y = 0$

$\Rightarrow GS = (c_1 + c_2x)e^{m_1x}$

### Case 3

Same as Case 2 but now three roots are equal.

GS is $y = (c_1 + c_2x + c_3x^2)e^{m_1x} + c_4e^{m_4x} + \dots + c_ne^{m_nx}$

Similar is the treatment for further equality of roots.

### Case 4

Same as Case 3 but all roots are equal, then GS is

$y = (c_1 + c_2x + c_3x^2 + \dots + c_nx^{n - 1})e^{m_1x}$

### Case 5

If in Case 1 we have $\alpha \pm i\beta$ as a pair of complex roots then GS is 

$y = e^{\alpha x}[Acos(\beta x) + Bsin(\beta x)]$ (Ignoring other terms for now) 

If the imaginary roots are repeated, say, $\alpha \pm i\beta$ occur twice then the soln would be 

$y = e^{\alpha x}[(A + Bx)cos(\beta x) + (C + Dx)sin(\beta x)]$

:::tip Note
1. Expression $e^{\alpha x}[Acos(\beta x) + Bsin(\beta x)]$ can as well be written as

   $Ae^{\alpha x}cos(\beta x + B)$

2. If AE has $\alpha \pm \sqrt{\beta}$ as a pair of roots, then GS is 

   $y = e^{\alpha x}[Acosh(\sqrt{\beta}x) + Bsinh(\sqrt{\beta}x)]$

   which may be written as $y = Ae^{\alpha x}cosh(\sqrt{\beta}x + B)$

   If these roots are repeated then the GS is 

   $y = e^{\alpha x}[(A + Bx)cosh(\sqrt{\beta} x) + (C + Dx)sinh(\sqrt{\beta} x)]$
   
:::