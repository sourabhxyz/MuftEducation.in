---
id: poly_ring
title: Polynomial Rings
sidebar_label: Polynomial Rings
---


Let $R$ be a commutative ring. The set of formal symbols $R[x] = \\{a_nx_n + a_{n-1}x_{n-1} + \cdots + a_1x_1 + a0 \mid a_i \in R, n$ is a nonnegative integer $\\}$ is called the ring of polynomials over $R$ in the indeterminate $x$. Two elements $a_nx_n + a_{n-1}x_{n-1} + \cdots + a_1x_1 + a_0$ and $b_mx_m + b_{m-1}x_{m-1} + \dots + b_1x_1 + b_0$ of $R[x]$ are considered equal if and only if $a_i = b_i$ for all nonnegative integers $i$. (Define $a_i = 0$ when $i > n$ and $b_i = 0$ when $i > m$.)

one must be careful not to confuse a polynomial with the function determined by a polynomial. For example, in $Z_3[x]$, the polynomials $f (x) = x$ and $g(x) = x^3$ determine the same function from $Z_3$ to $Z_3$, since $f(a) = g(a)$ for all $a$ in $Z_3$. But $f(x)$ and $g(x)$ are different elements of $Z_3[x]$. 

To make $R[x]$ into a ring, we define addition and multiplication in
the usual way.

## Theorem 15.1 

If $D$ is an integral domain, then $D [x]$ is an integral domain.

**Proof:** 

Since we already know that $D[x]$ is a ring, all we need to show is that $D[x]$ is commutative with a unity and has no zero-divisors. Clearly, $D[x]$ is commutative whenever $D$ is. If 1 is the unity element of $D$, it is obvious that $f(x) = 1$ is the unity element of $D[x]$. Finally, suppose that $f (x) = a_nx_n + a_{n-1}x_{n-1} + \cdots + a_0$ and $g(x) = b_mx_m + b_{m-1}x_{m-1} + \cdots + b_0$, where $a_n \neq 0$ and $b_m \neq 0$. Then, by definition, $f(x)g(x)$ has leading coefficient $a_nb_m$ and, since D is an integral domain, $a_nb_m \neq 0$.

## Theorem 15.2

Let $F$ be a field and let $f(x), g(x) \in F[x]$ with $g(x) \neq 0$. Then
there exist unique polynomials $q(x)$ and $r(x)$ in $F[x]$ such that $f(x) = g(x)q(x) + r(x)$ and either $r(x) = 0$ or $deg r(x) < deg g(x)$.

**Proof:** We begin by showing the existence of $q(x)$ and $r(x)$. If $f(x) = 0$ or $deg f(x) < deg g(x)$, we simply set $q(x) = 0$ and $r(x) = f(x)$. So, we may assume that $n = deg f(x) \geq deg g(x) = m$ and let $f(x) = a_nx_n + \cdots + a_0$ and $g(x) = b_mx_m + \cdots + b_0$. The idea behind this proof is to begin just as if you were going to "long divide" $g(x)$ into $f(x)$, then use the Second Principle of Mathematical Induction on $\operatorname{deg} f(x)$ to finish up. Thus, resorting to long division, we let $f_1(x) = f(x) - a_nb_m^{-1}x^{n-m}g(x)$. Then, $f_1(x) = 0$ or $deg f_1(x) < deg f(x)$; so, by our induction hypothesis, there exist $q_1(x)$ and $r_1(x)$ in $F[x]$ such that $f_1(x) = g(x)q_1(x) + r_1(x)$, where $r_1(x) = 0$ or $deg r_1(x) < deg g(x)$. [Technically, we should get the induction started by proving the case in which $deg f(x) = 0$, but this is trivial.] Thus, $f(x) = a_nb_m^{-1}x^{n-m}g(x) + f_1(x) = a_nb_m^{-1}x^{n-m}g(x) + q_1(x)g(x) + r_1(x)$ = $[a_nb_m^{-1}x^{n-m} + q_1(x)]g(x) + r_1(x)$. So, the polynomials $q(x) = a_nb_m^{-1}x^{n-m} + q_1(x)$ and $r(x) = r_1(x)$ have the desired properties. Proving uniqueness is easy. $\blacksquare$

When the ring of coefficients of a polynomial ring is a field, we can use the long
division process to determine the quotient and remainder.





