---
id: fact_poly
sidebar_label: Factorization of Polynomials
title: Factorization of Polynomials
---

Let $D$ be an integral domain. A polynomial $f(x)$ from $D[x]$ that is
neither the zero polynomial nor a unit in $D[x]$ is said to be irreducible
over $D$ if, whenever $f(x)$ is expressed as a product $f(x) = g(x)h(x)$, with
$g(x)$ and $h(x)$ from $D[x]$, then $g(x)$ or $h(x)$ is a unit in $D[x]$. A nonzero,
nonunit element of $D[x]$ that is not irreducible over $D$ is called
reducible over $D$.

Note that polynomial of degree $\geq$ 1 is never a unit due to the way multiplication is defined.

In the case that an integral domain is a field $F$, it is equivalent and more
convenient to define a nonconstant $f(x) \in F[x]$ to be irreducible if $f(x)$ cannot be expressed as a product of two polynomials of lower degree.

**Examples:**

*  The polynomial $f(x) = 2x^2 + 4$ is irreducible over $Q$ but reducible over $Z$, since $2x^2 + 4 = 2(x^2 + 2)$ and neither $2$ nor $x^2 + 2$ is a unit in $Z[x]$.
* The polynomial $f(x) = 2x^2 + 4$ is irreducible over $R$ but reducible over $C$.
*  The polynomial $x^2 - 2$ is irreducible over $Q$ but reducible over $R$.
*  The polynomial $x^2 + 1$ is irreducible over $Z_3$ but reducible over $Z_5$ as $(x^2 + 1) = (x + 3)(x + 2)$. Also note that zero of $x^2 + 1$ in $Z_5$ is 2.

In general, it is a difficult problem to decide whether or not a particular polynomial is reducible over an integral domain, but there are special cases when it is easy. 

**Theorem 16.1**: Let $F$ be a field. If $f(x) \in F[x]$ and $\operatorname{deg} f(x)$ is 2 or 3, then $f(x)$ is reducible over $F$ if and only if $f(x)$ has a zero in $F$.

**Proof:** Suppose that $f(x) = g(x)h(x)$, where both $g(x)$ and $h(x)$ belong to $F[x]$ and have degrees less than that of $f(x)$. Since $\operatorname{deg} f(x) = \operatorname{deg} g(x) + \operatorname{deg} h(x)$ and $\operatorname{deg} f(x)$ is 2 or 3, at least one of $g(x)$ and $h(x)$ has degree 1. Say $g(x) = ax + b$. Then, clearly, $-a^{-1}b$ is a zero of $g(x)$ and therefore a zero of $f(x)$ as well. Conversely, suppose that $f(a) = 0$, where $a \in F$. Then, by the Factor Theorem, we know that $x - a$ is a factor of $f(x)$ and, therefore, $f(x)$ is reducible over $F$. $\blacksquare$

So, in case of $Z_p$, we can easily check for reducibility of $f(x)$ by testing if $f(a) = 0$ for $a = 0, 1, . . . , p - 1$.

---

The content of a nonzero polynomial $a_nx^n + a_{n-1}x^{n-1} + \cdots + a_0$, where the $a's$ are integers, is the greatest common divisor of the integers $a_n, a_{n-1}, . . . , a_0$. A primitive polynomial is an element of $Z[x]$ with content 1.

---

**Gauss's Lemma**: The product of two primitive polynomials is primitive.

**Proof:** Let $f(x)$ and $g(x)$ be primitive polynomials, and suppose that
$f(x)g(x)$ is not primitive. Let $p$ be a prime divisor of the content of
$f(x)g(x)$, and let $\overline{f (x)}, \overline{g(x)}$, and $\overline{f(x)g(x)}$ be the polynomials obtained from $f(x)$, $g(x)$, and $f(x)g(x)$ by reducing the coefficients modulo $p$. Then, $\overline{f (x)}$ and $\overline{g(x)}$ belong to the integral domain $Z_p[x]$ and $\bar{f(x)}\bar{g(x)} = \overline{f(x)g(x)} = 0$, the zero element of $Z_p[x]$. Thus, $\overline{f(x)} = 0$ or $\overline{g(x)} = 0$. This means that either $p$ divides every co- efficient of $f(x)$ or $p$ divides every coefficient of $g(x)$. Hence, either $f(x)$ is not primitive or $g(x)$ is not primitive. This contradiction completes the proof.









