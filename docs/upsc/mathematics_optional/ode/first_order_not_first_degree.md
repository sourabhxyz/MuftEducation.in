---
id: first_order_not_first_degree
title: Soln of DE of the first order but not of first degree
sidebar_label: Soln of DE of the first order but not of first degree
---

Is of the form (for degree = $n$) $P^n + A_1P^{n - 1} + A_2P^{n - 2} + \dots + A_{n - 1}P + A_ny = 0$
where $A_i$ are functions of $x$ and $P = \frac{dy}{dx}$

## Solvable for p

Such equations can be resolved into linear factors of first degree.

i.e., it reduces to $(P - f_1(x, y))(P - f_2(x, y))\dots (P - f_n(x, y) = 0$

i.e., $P = f_i(x, y)$, these equations on integration gives $F_i(x, y, c_i) \rightarrow y = F_1(x, y, c_1) \dots F_n(x, y, c_n)$

But our DE is of first order and thus should have only one arbitrary constant, therefore let $c_i = c$

**Examples:**

- $(P - xy) (P - x^2) (P - y^2) = 0$

  $(log(y) - x^2/2 - c)(y - x^3/3 - c)(-1/y - x - c) = 0$

## Solvable for x

i.e., it can be put in the form $x = f(y, P) \tag{1} \label{1}$

Differentiating wrt $y$ we get $1/P = F(y, P, \frac{dP}{dy}) \tag{2} \label{2}$

Let the soln of $\eqref{2}$ be $\phi(y, P, c) = 0 \label{3} \tag{3}$

Eliminating $P$ between $\eqref{1} \text{ and } \eqref{3}$ gives the soln for the given eqn.

If it is not possible to eliminate $P$ then the values of $x$ and $y$ in terms of $P$ i.e. $x = f_1(P, c) \text{ \& } y = f_2(P, c)$ together constitute the soln.

**Examples:**

- $xP^3 = a + bP$

  $\rightarrow x = a/P^3 + b/P^2$

  $\rightarrow 1/P = (-3a/P^4 -2b/P^3)\frac{dP}{dy}$

  $\rightarrow dy = (-3a/P^3 -2b/P^2)dP$

  $\rightarrow y = 3a/2P^2 + 2b/P + c$

  Here it is not possible to eliminate $P$ from 1 and 3. GS therefore is $x = a/P^3 + b/P^2, y = 3a/2P^2 + 2b/P + c$

- $P^3 - 4xyP + 8y^2 = 0$

  $\rightarrow x = P^2/4y + 2y/P$

  $\rightarrow 1/P = 2P/4y \frac{dP}{dy} - P^2/4y^2 + 2/P - 2y/P^2 \frac{dP}{dy}$

  $\rightarrow (\frac{P}{2y} - \frac{2y}{P^2})(\frac{dP}{dy} - \frac{P}{2y}) = 0$

  Omitting the first factor which leads to a singular soln, we get

  $\frac{dP}{dy} - \frac{P}{2y} = 0$

  $\rightarrow p = y^{1/2}c$

  Eliminating $p$ from 1 and 3 we get

  $x = \frac{y}{4yc^2} + \frac{2y}{y^{1/2}c}$

  $\rightarrow x = \frac{1}{4c^2} + \frac{2y^{1/2}}{c}$

:::tip Note
The factor which does not involve a derivative of P wrt $x \text{ or }y$ will be omitted as it will always lead to a singular soln
:::

## Solvable for y

i.e. of the form $y = f(x, P)$

differentiating both sides wrt x, we get $p = F(x, P, \frac{dP}{dx})$

proceed similar to [Solvable for x](#Solvable-for-x).

**Example:**

- $y = 3x + logP$

  $P = 3 + \frac{1}{P}\frac{dP}{dx}$

  $\frac{1}{3}[\frac{1}{P - 3} - \frac{1}{P}]dP = dx$

  $\frac{P - 3}{P} = Ae^{3x}$

  $P = \frac{3}{1 - Ae^{3x}}$

  Eliminate $P$ between 1 and 3 to get

  $y = 3x + log(\frac{3}{1 - Ae^{3x}})$

## Clairaut's Eqn

Is of the form $y = xP + f(P)$. It is solved as in [Solvable for y](#Solvable-for-y)

Differentiating wrt $x$ we get, $P = P + x\frac{dP}{dx} + f'(P)\frac{dP}{dx}$

$\rightarrow (x - f'(P))\frac{dP}{dx} = 0$

$\rightarrow \frac{dP}{dx} = 0$ ($x + f'(P)$ is discarded)

$\rightarrow P = c$

Therefore the GS is $y = xc + f(c)$

**Examples:**

- $P = log(Px - y)$

  $\rightarrow y = xc + e^c$

- $sin(y - Px) = P$

  $y = Pc + sin^{-1}(c)$

### Equations reducible to Clairaut's form

#### Form 1

$y^2 = pxy + f(\frac{py}{x}$

Intuition tells that we must do $f(\frac{py}{x}) = f(P)$

Let $X = x^2, Y = y^2 \rightarrow dX = 2xdx, dY = 2ydy$

$\rightarrow dY/dX = P = \frac{y}{x}p \rightarrow p = \frac{x}{y}P$

$\rightarrow Y = XP + f(P)$

$\rightarrow y^2 = x^2c + f(c)$

**Examples:**

- $x^2(y - px) = yp^2$

  $\rightarrow x^2y^2 - x^3py = y^2p^2$

  $\rightarrow y^2 = pxy + (\frac{py}{x})^2$
