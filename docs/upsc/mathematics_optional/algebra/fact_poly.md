---
id: fact_poly
sidebar_label: Factorization of Polynomials
title: Factorization of Polynomials
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
$f(x)g(x)$, and let $\overline{f (x)}, \overline{g(x)}$, and $\overline{f(x)g(x)}$ be the polynomials obtained from $f(x)$, $g(x)$, and $f(x)g(x)$ by reducing the coefficients modulo $p$. Then, $\overline{f (x)}$ and $\overline{g(x)}$ belong to the integral domain $Z_p[x]$ and $\bar{f(x)}\bar{g(x)} = \overline{f(x)g(x)} = 0$, the zero element of $Z_p[x]$. Thus, $\overline{f(x)} = 0$ or $\overline{g(x)} = 0$. This means that either $p$ divides every co- efficient of $f(x)$ or $p$ divides every coefficient of $g(x)$. Hence, either $f(x)$ is not primitive or $g(x)$ is not primitive. This contradiction completes the proof. $\blacksquare$

**Theorem 16.2:** Let $f(x) \in Z[x]$. If $f(x)$ is reducible over $Q$, then it is reducible over $Z$.

**Proof:** Suppose that $f(x) = g(x)h(x)$, where $g(x)$ and $h(x) \in Q[x]$. Clearly, we may assume that $f (x)$ is primitive because we can divide both $f(x)$ and $g(x)$ by the content of $f(x)$. Let $a$ be the least common multiple of the denominators of the coefficients of $g(x)$, and $b$ the least common multiple of the denominators of the coefficients of $h(x)$. Then $abf(x) = ag(x) \cdot bh(x)$, where $ag(x)$ and $bh(x) \in Z[x]$. Let $c_1$ be the content of $ag(x)$ and let $c_2$ be the content of $bh(x)$. Then $ag(x) = c_1g_1(x)$ and $bh(x) = c_2h_1(x)$, where both $g_1(x)$ and $h_1(x)$ are primitive, and $abf(x) = c_1c_2g_1(x)h_1(x)$. Since $f(x)$ is primitive, the content of $abf(x)$ is $ab$. Also, since the product of two primitive polynomials is primitive, it follows that the content of $c_1c_2g_1(x)h_1(x)$ is $c_1c_2$. Thus, $ab = c_1c_2$ and $f(x) = g_1(x)h_1(x)$, where $g_1(x)$ and $h_1(x) \in Z[x]$ and $\operatorname{deg} g_1(x) = \operatorname{deg} g(x)$ and $\operatorname{deg} h_1(x) = \operatorname{deg} h(x)$. $\blacksquare$

**Example:** 

* For the polynomial $f (x) = 6x^2 + x - 2 = (3x - 3/2)(2x + 4/3) = g(x)h(x)$. In this case we have $a = 2, b = 3, c_1 = 3, c_2 = 2, g_1(x) = 2x - 1$, and $h_1(x) = 3x + 2$.

## Irreducibility Tests 

**Theorem 16.3:** Let $p$ be a prime and suppose that $f(x) \in Z[x]$ with $\operatorname{deg} f(x) \geq 1$. Let $\bar{f} (x)$ be the polynomial in $Z _p[x]$ obtained from $f(x)$ by reducing pall the coefficients of $f(x)$ modulo $p$. If $\bar{f} (x)$ is irreducible over $Z_p$ and $\operatorname{deg} \bar{f} (x) = \operatorname{deg} f(x)$, then $f(x)$ is irreducible over $Q$.

**Proof:** It follows from the proof of Theorem 16.2 that if $f(x)$ is reducible over $Q$, then $f(x) = g(x)h(x)$ with $g(x), h(x) \in Z[x]$, and both $g(x)$ and $h(x)$ have degree less than that of $f(x)$. Let $\bar{f} (x), \bar{g}(x)$, and $\bar{h}(x)$ be the polynomials obtained from $f(x), g(x)$, and $h(x)$ by reducing all the coefficients modulo $p$. Since $\operatorname{deg} f(x) = \operatorname{deg} \bar{f} (x)$, we have $\operatorname{deg} \bar{g}(x) \leq \operatorname{deg} g(x) < \operatorname{deg} \bar{f} (x)$ and $\operatorname{deg} \bar{h}(x) \leq \operatorname{deg} h(x) < \operatorname{deg} \bar{f} (x)$. But, $\bar{f} (x) = \bar{g}(x)\bar{h}(x)$, and this contradicts our assumption that $\bar{f} (x)$ is irreducible over $Z_p$. $\blacksquare$













