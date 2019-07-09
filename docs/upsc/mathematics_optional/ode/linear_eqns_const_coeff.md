---
id: linear_eqns_const_coeff
title: Linear Equations With Const. Coeff.
sidebar_label: Linear Equations With Const. Coeff.
---

---

**Definition:**
Linear DE of order $n$ of the form: $d^ny/dx^n + a_1d^{n - 1}y/dx^{n - 1} + \cdots + a_{n - 1}dy/dx + a_ny = Q(x)$ _(or)_ $X$

This eqn can be written as $f(D)y = Q \dots (1)$ where

$f(D) = D^n + a_1D^{n - 1} + \dots + a_{n - 1}D + a_n$

Note that these coefficients can be complex (imaginary).

---

## Homogeneous Eqn

If $Q = 0$ we get Homogeneous Eqn with constant coeff.

## Solving Linear Eqn

Solving this linear eqn is divided into two parts,

1. First we find the general solution of the corresponding Homogeneous eqn which is called as Complementary Function (CF) (_Note:_ It must contain as many arbitrary constants as the order of the eqn)
2. Next find a particular soln of original eqn which does not contain any arbitrary constant. This is called the Particular Integral (PI).
3. GS = CF + PI.

## Auxiliary Eqn

$f(m) = 0$ is called auxiliary eqn of (1). Clearly it will must have $n$ roots (which can be complex).

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

Here $A$ and $B$ can be complex. This is simplified form, putting soln in form of Case 1 is as well valid.

**Derivation:**

$y = c_1e^{(\alpha + i\beta)x} + c_2e^{(\alpha - i\beta)x} + c_3e^{m_3x} + \dots$

$= e^{\alpha x}(c_1e^{i\beta x} + c_2e^{-i\beta x}) + \dots$

$= e^{\alpha x}(c_1(cos(\beta x) + isin(\beta x)) + c_2(cos(\beta x) + -sin(\beta x)) + \dots$

$= e^{\alpha x}(Acos(\beta x) + Bsin(\beta x)) + \dots$

Where $A = c_1 + c_2$ and $B = i(c_1 - c_2)$

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

## Find PI

### Inverse Operator

$\frac{1}{f(D)}X$ is that function of $x$, not containing arbitrary constants which when operated upon by $f(D)$ gives $X$

i.e. $f(D)(\frac{1}{f(D)}X) = X$

Thus $\frac{1}{f(D)}X$ is a PI.

_Note:_ Say $X = c_1g_1(x) + c_2g_2(x)$ where $c_1, c_2$ are constants. Then $PI = c_1\frac{g_1(x)}{f(D)} + c_2\frac{g_2(x)}{f(D)}$ and each of these can be solved independently of the other as if other doesn't exist.

---

$\frac{1}{D}X = \int Xdx$

Proof: Let $\frac{1}{D}X = y$

$\Rightarrow Dy = X \Rightarrow dy/dx = X$

$\Rightarrow y = \int Xdx$ no constant being added because $y$ doesn't contain any constant.

**Corollary:** $\frac{1}{D^2}X = \int [\int Xdx]dx$

---

$\frac{1}{D - a}X = e^{ax}\int Xe^{-ax}dx$

Proof: Let $\frac{1}{D - a}X = y$

$\Rightarrow (D - a)y = X$

$\Rightarrow dy/dx - ay = X$

$\Rightarrow y = e^{ax}\int Xe^{-ax}dx$

### Case 1

To find PI when $Q = e^{ax}$ and $f(a) \neq 0$

Since $D^ke^{ax} = a^ke^{ax}$ therefore PI is $y = e^{ax}/f(a)$

:::note If $f(a) = 0$
Since $a$ is the root of AE, therefore $(D - a)$ is a factor of $f(D)$. Suppose $f(D) = (D - a)\phi(D)$, where $\phi(a) \neq 0$. Then

$\frac{1}{f(D)}e^{ax} = \frac{1}{D - a}\frac{1}{\phi(D)}e^{ax} = \frac{1}{\phi(a)}\frac{1}{D - a}e^{ax}$

$= \frac{1}{\phi(a)}e^{ax}\int e^{ax}e^{-ax}dx$

$= xe^{ax}/phi(a) = xe^{ax}/f'(a)$

$\because f'(D) = (D - a)\phi '(D) + 1 \cdot \phi(D)$

$\therefore f'(a) = \phi(a)$

If $f'(a) = 0$ then applying this procedure again we get $\frac{1}{f(D)}e^{ax} = x^2e^{ax}/f''(a)$

Instead of taking $f''(a)$ one can take $2\phi(a)$ as:-

$f(D) = (D - a)^2\phi(D)$

$\Rightarrow f'(D) = 2(D - a)\phi(D) + (D - a)^2\phi '(D)$

$\Rightarrow f''(a) = 2\phi (a)$

Similarly $f^{(k)}(a) = k!\phi(a)$
:::

**Examples:**

- $(D + 2)(D - 1)^2y = e^{-2x} + 2sinh x$

  $ = e^{-2x} + e^x - e^{-x}$

  $\Rightarrow y = xe^{-2x}/f'(-2) + x^2e^{x}/f''(1) -e^{-x}/f(-1)$

  $= xe^{-2x}/9 + x^2e^{x}/6 - e^{-x}/4$

### Case 2

$X = sin(ax + b) \text{ or } cos(ax + b)$

$\Rightarrow (D^2)^r sin(ax + b) = (-a^2)^r sin(ax + b)$

$\therefore f(D^2)sin(ax + b) = f(-a^2)sin(ax + b)$

Operating on both sides by $\frac{1}{f(D^2)}$ and dividing both sides by $f(-a^2)$ we get

$\frac{1}{f(D^2)}sin(ax + b) = \frac{1}{f(-a^2)}sin(ax + b)$ provided $f(-a^2) \neq 0$

If $f(-a^2) = 0$ [Note that if $f(a) = 0$ then it doesn't mean $f(-a^2) = 0$ thus be careful when checking this] then we proceed further.

$\frac{1}{D^2}sin(ax + b) =$ I.P. of $\frac{1}{D^2}e^{i(ax + b)}$

= IP of $\frac{x}{f'(D^2)}e^{i(ax + b)}$

= $x\frac{1}{f'(-a^2)}sin(ax + b)$

If $f'(-a^2) = 0$, $\frac{1}{D^2}sin(ax + b) = x^2\frac{1}{f''(-a^2)}sin(ax + b)$ provided $f''(-a^2) \neq 0$ and so on.

Similarly,

- $\frac{1}{f(D^2)}cos(ax + b) = \frac{1}{f(-a^2)}cos(ax + b)$ provided $f(-a^2) \neq 0$

- If $f(-a^2) = 0$ then, $\frac{1}{f(D^2)}cos(ax + b) = x\frac{1}{f'(-a^2)}cos(ax + b)$ provided $f'(-a^2) \neq 0$

- If $f'(-a^2) = 0$ then, $\frac{1}{f(D^2)}cos(ax + b) = x^2\frac{1}{f''(-a^2)}cos(ax + b)$ provided $f''(-a^2) \neq 0$

**Examples:**

- $(D^3 + 1)y = cos(2x - 1)$

  PI = $\frac{1}{D^3 + 1}cos(2x - 1)$

  $= \frac{1}{-4D + 1}cos(2x - 1)$

  $= \frac{1 + 4D}{(1 - 4D)(1 + 4D)}cos(2x - 1)$

  $(1 + 4D)\frac{1}{1 - 16(-4)}cos(2x - 1)$

  $= \frac{1}{65}[cos(2x - 1) + 4Dcos(2x - 1)]$

  $= \frac{1}{65}[cos(2x - 1) + -8sin(2x - 1)]$

- $\frac{d^3y}{dx^3} + 4\frac{dy}{dx} = sin(2x)$

  PI = $\frac{1}{D(D^2 + 4)}sin(2x)$

  $= x\frac{1}{3D^2 + 4}sin(2x)$

  _Note:_ We couldn't have just did $D(2D)$... as derivative should be applied to whole.

  $= x\frac{1}{3(-4) + 4}sin(2x)$

  $= -\frac{x}{8}sin(2x)$

### Case 3

$X = x^m$

PI = $\frac{1}{f(D)}x^m = [f(D)]^{-1}x^m$

Expand $[f(D)]^{-1}$ in ascending powers of D as far as the term in $D^m$ and operate on $x^m$ term by term. Since $(m + 1)th$ and higher derivatives of $x^m$ are zero, we need not consider terms beyond $D^m$

**Examples:**

- $\frac{d^2y}{dx^2} + \frac{dy}{dx} = x^2 + 2x + 4$

  PI = $\frac{1}{D(D + 1)}(x^2 + 2x + 4)$

  $= \frac{1}{D}(1 - D + D^2 + \dots)(x^2 + 2x + 4)$

  $= \frac{1}{D}(x^2 + 2x + 4 - (2x + 2) + 2)$

  $= \int (x^2 + 4)dx = x^3/3 + 4x$

- $\frac{1}{(D - 2)^2}x^2 = \frac{1}{4}(1 - D/2)^{-2}x^2$

  $= \frac{1}{4}(1 + D + \frac{(-2)(-3)}{2!}(-D/2)^2 + \dots)x^2$

  $= \frac{1}{4}(x^2 + 2x + 3/2)$

- $\frac{1}{D^2 - 2D + 2}(x)$

  $= \frac{1}{(D - (1 + i))(D - (1 - i))}$

  $= \frac{1}{2(1 - (D/(1 + i))(1 - (D/(1 - i))))}x$

  $= \frac{1}{2(1 - D/(1 + i))}(1 + D/(1 - i))x$

  $= \frac{1}{2}(x + 1/(1 + i))(1 + D/(1 - i))$

  $= \frac{1}{2}(x + 1/(1 - i) + 1/(1 + i))$

  $= (x + 1)/2$

  **Aliter**

  $= \frac{1}{2}(1 - (D - D^2/2))^{-1}x$

  $= \frac{1}{2}(1 + D - D^2/2)x$

:::caution Caution
In $\frac{x}{(D + 1)^2 - 4} = -\frac{1}{4}\frac{x}{1 - (\frac{D + 1}{2})^2}$

Is not equal to $-\frac{1}{4}(1 + (\frac{D + 1}{2})^2)x$

Solve it the way done in aliter above, i.e. in $(1 + x)^n$, $x$ should only contain $D's$ (not sure why $D's$ would be valid).
:::

### Case 4

$X = e^{ax}V(x)$

It can be proven

$\frac{1}{f(D)}(e^{ax}V) = e^{ax}\frac{1}{f(D + a)}V$

**Examples:**

- $(D^2 - 2D + 4)y = e^xcosx$

  PI = $e^x\frac{cosx}{f(D + 1)}$

  $= e^x\frac{cosx}{D^2 + 3}$

  $= e^x\frac{cosx}{2}$

### Case 5

When $X$ is any other function of $x$.

PI = $\frac{1}{f(D)}X$

If $f(D) = (D - m_1)(D - m_2)\dots (D - m_n)$

$\Rightarrow 1/f(D) = \frac{A_1}{D - m_1} + \frac{A_2}{D - m_2} + \dots + \frac{A_n}{D - m_n}$

$\therefore PI = A_1\frac{1}{D - m_1}X + A_2\frac{1}{D - m_2}X + \dots + A_2\frac{1}{D - m_n}X$

$= A_1e^{m_1x}\int Xe^{-m_1x}dx + A_2e^{m_2x}\int Xe^{-m_2x}dx + \dots + A_ne^{m_nx}\int Xe^{-m_nx}dx$

**Examples:**

- $(D^2 + D + 1)y = (1 - e^x)^2 = 1 + e^{2x} - 2e^{x}$

  $\Rightarrow y = CF + e^{0x}/(0 + 0 + 1) + e^{2x}/(4 + 2 + 1) - 2e^{x}/{3}$

  $y = CF + 1 + e^{2x}/7 - 2e^x/3$

- $(D^4 + 2D^2 + 1)y = x^2cos(x)$

  $AE = (m^2 + 1)^2$

  $\Rightarrow m = \pm i, \pm i$

  $\Rightarrow CF = (c_1 + c_2x)cosx + (c_3 + c_4x)sinx$

  $PI = Re[e^{ix}\frac{x^2}{((D + i)^2 + 1)^2}]$

  $= Re[e^{ix}(-\frac{1}{4D^2}(1 - iD/2)^{-2}x^2)]$ (_Since_ $\frac{1}{i} = -i$)

  $= Re[-\frac{e^{ix}}{4}\frac{1}{D^2}(1 + 2iD/2 + 3(iD/2)^2)x^2]$

  $= Re[-\frac{e^{ix}}{4}\frac{1}{D^2}(x^2 + 2ix - 3/2)]$

  $= Re[-\frac{e^{ix}}{4}\frac{1}{D}(x^3/3 + ix^2 - 3x/2)]$

  $= Re[-\frac{e^{ix}}{4}(x^4/12 + ix^3/3 - 3x^2/4)]$

  $= \frac{-1}{48}Re[(cosx + isinx)(x^4 + 4ix^3 - 9x^2)]$

  $= \frac{-1}{48}[(x^4 - 9x^2)cosx - 4x^3sinx]$

* $(D^2 - 4D + 4)y = 8x^2e^{2x}sin(2x)$

  $y = CF + IM[8e^{2x(1 + i)}\frac{x^2}{(D + 2i)^2}$]

  Now after a bit long calculation, you will arrive at answer. The better way is to always factorize $f(D)$ first so that we can see some structure. For example, in this case $f(D) = (D - 2)^2$, thus, $y = CF + 8e^{2x}\frac{x^2sin(2x)}{D^2}$ which is comparatively easy to compute.

* $(D^2 + a^2)y = sec(ax)$

  $\rightarrow D = \pm ai$

  $CF = c_1cosax + c_2sinax$

  $PI = \frac{1}{D^2 + a^2}secax = \frac{1}{2ia}[\frac{1}{D - ia} - \frac{1}{D + ia}]secax$

  Now $\frac{1}{D - ia}secax = e^{iax}\int secaxe^{-iax}dx$

  $= e^{iax}\int \frac{cosax - isinax}{cosax}dx = e^{iax}\int (1 - itanax)dx$

  $= e^{iax}(x + \frac{i}{a}log(cosax))$

  Changing $i$ to $-i$ we get

  $\frac{1}{D + ia}secax = e^{-iax}(x - \frac{i}{a}log(cosax))$

  $PI = \frac{1}{2ia}[e^{iax}(x + \frac{i}{a}log(cosax)) - e^{-iax}(x - \frac{i}{a}log(cosax))]$
