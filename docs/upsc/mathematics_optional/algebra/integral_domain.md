---
id: integral_domain
title: Integral Domains
sidebar_label: Integral Domains
documentclass: extarticle
classoption:
  - 8pt
  - a4paper
  - oneside
  - twocolumn
header-includes:
  - \usepackage{enumitem}
  - \setlist{nolistsep}
  - \usepackage[export]{adjustbox}
  - \usepackage[compact]{titlesec}
  - \titlespacing*{\section}{0pt}{0px plus 1px minus 0px}{-2px plus 0px minus 0px}
  - \titlespacing*{\subsection}{0pt}{0px plus 1px minus 0px}{0px plus 3px minus 3px}
  - \titlespacing*{\subsubsection}{0pt}{0px plus 1px minus 0px}{0px plus 3px minus 3px}
  - \usepackage[left=0.8cm, right=0.8cm, top=2cm, bottom=0.3cm, a4paper]{geometry}
  - \setlength{\columnseprule}{0.4pt}
subparagraph: yes
---

## Zero-Divisors

A zero-divisor is a nonzero element $a$ of a commutative ring $R$ such that there is a nonzero element $b \in R$ with $ab = 0$.

## Integral Domain

An integral domain is a commutative ring with unity and no zero-divisors.

**Examples:**

* The ring $Z_n$ of integers modulo $n$ is not an integral domain when $n$ is not prime.

* The ring of integers is an integral domain.

* $Z \oplus Z$ is not an integral domain.

## Theorem 12.1

Let $a, b$, and $c$ belong to an integral domain. If $a \neq 0$ and $ab = ac$, then $b = c$.

**Proof:** From $ab = ac$, we have $a(b - c) = 0$. Since $a \neq 0$, we must have $b - c = 0$. $\blacksquare$

Many authors prefer to define integral domains by the cancellation
property—that is, as commutative rings with unity in which the cancellation property holds. This definition is equivalent to ours.

## Fields

A field is a commutative ring with unity in which every nonzero
element is a unit.


To verify that every field is an integral domain, observe that if $a$ and
$b$ belong to a field with $a \neq 0$ and $ab = 0$, we can multiply both sides
of the last expression by $a^{-1}$ to obtain $b = 0$.

## Theorem 12.2

A finite integral domain is a field. (proof as in groups)

### Corollary 

$Z_n$ is a field if and only if $n$ is prime.

## Characteristic of a Ring

The characteristic of a ring $R$ is the least positive integer $n$ such that
$nx = 0$ (Remember that this is adding $x$, $n$ times) for all $x$ in $R$. If no such integer exists, we say that $R$ has characteristic 0. The characteristic of $R$ is denoted by $\operatorname{char} R$.


* Thus, the ring of integers has characteristic 0, and $Z_n$ has characternistic $n$.
* An infinite ring can have a nonzero characteristic. Indeed, the ring $Z_2[x]$ of all polynomials with coefficients in $Z_2$ has characteristic 2. (Addition and multiplication are done as for polynomials with ordinary integer coefficients except that the coefficients are reduced modulo 2.)

## Theorem 12.3

Let $R$ be a ring with unity 1. If 1 has infinite order under addition, then the characteristic of $R$ is 0. If 1 has order $n$ under addition, then the characteristic of $R$ is $n$. 

**Proof:** Suppose that 1 has additive order n (as other case is straight forward). Then $n \cdot 1 = 0$, and $n$ is the least positive integer with this property. So, for any $x$ in $R$, we have $n \cdot x = x + x + \cdots + x$ ($n$ summands) = $1x + 1x + \cdots + 1x$ ($n$ summands) = $(1 + 1 + \cdots + 1)x$ ($n$ summands)$ = (n \cdot 1)x = 0x = 0.$ Thus, $R$ has characteristic $n$.

**Corollary:** Characteristic of a subfield is same as that of field as unity of subfield is same as that of unity of field.

**Proof:** If $u$ is any element of $F$ satisfying $u^2 = u$, then either $u=0 \text{ or } u=1$.

If $K$ is a subring of $F$ having unity $e$, possibly different from $1 \in F$, then $e^2 = ee = e$ by definition of unity. So either $e=0 \text{ or } e=1$, because $e \in F$. The case $e = 0$ is disallowed if $K$ is a subfield, because in a field it is required that the unity is nonzero.

## Theorem 12.4

The characteristic of an integral domain is 0 or prime.

**Proof:** By Theorem 12.3, it suffices to show that if the additive order of 1 is finite, it must be prime. Suppose that 1 has order $n$ and that $n = st$, where $1 \leq s, t \leq n.$ Then, as we know, $0 = n \cdot 1 = (st) \cdot 1 = (s \cdot 1)(t \cdot 1).$ 

So, $s \cdot 1 = 0 \text{ or } t \cdot 1 = 0.$ Since $n$ is the least positive integer with the property that $n \cdot 1 = 0$, we must have $s = n$ or $t = n$. Thus, $n$ is prime. $\blacksquare$

Thus characteristic of a field is 0 or prime.




