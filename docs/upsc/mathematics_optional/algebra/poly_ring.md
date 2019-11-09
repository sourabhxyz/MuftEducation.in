---
id: poly_ring
title: Polynomial Rings
sidebar_label: Polynomial Rings
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


Let $R$ be a **commutative ring**. The set of formal symbols $R[x] = \\{a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x^1 + a_0 \mid a_i \in R, n$ is a nonnegative integer $\\}$ is called the ring of polynomials over $R$ in the indeterminate $x$. Two elements $a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x^1 + a_0$ and $b_mx^m + b_{m-1}x^{m-1} + \dots + b_1x^1 + b_0$ of $R[x]$ are considered equal if and only if $a_i = b_i$ for all nonnegative integers $i$. (Define $a_i = 0$ when $i > n$ and $b_i = 0$ when $i > m$.)

one must be careful not to confuse a polynomial with the function determined by a polynomial. For example, in $Z_3[x]$, the polynomials $f (x) = x$ and $g(x) = x^3$ determine the same function from $Z_3$ to $Z_3$, since $f(a) = g(a)$ for all $a$ in $Z_3$. But $f(x)$ and $g(x)$ are different elements of $Z_3[x]$. 

To make $R[x]$ into a ring, we define addition and multiplication in
the usual way.

Let
$f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x^1 + a_0$
and
$g(x) = b_mx^m + b_{m-1}x^{m-1} + \cdots + b_1x^1 + b_0$
belong to $R[x]$. Then $f(x) + g(x) = (a_s + b_s)x^s + (a_{s-1} + b_{s-1})x^{s-1} + \cdots + (a_1 + b_1)x + a_0 + b_0$, where $s$ is the maximum of $m$ and $n$. Also, $f(x)g(x) = c_{m+n}x^{m+n} + c_{m+n-1}x^{m+n-1} + \cdots 1 c_1x + c_0$, where $c_k = a_kb_0 + a_{k-1}b_1 + \cdots + a_1b_{k-1} + a_0b_k$ for $k = 0, . . . , m + n$.


## Theorem 15.1 

If $D$ is an integral domain, then $D [x]$ is an integral domain.

**Proof:** 

Since we already know that $D[x]$ is a ring, all we need to show is that $D[x]$ is commutative with a unity and has no zero-divisors. Clearly, $D[x]$ is commutative whenever $D$ is. If 1 is the unity element of $D$, it is obvious that $f(x) = 1$ is the unity element of $D[x]$. Finally, suppose that $f (x) = a_nx_n + a_{n-1}x_{n-1} + \cdots + a_0$ and $g(x) = b_mx_m + b_{m-1}x_{m-1} + \cdots + b_0$, where $a_n \neq 0$ and $b_m \neq 0$. Then, by definition, $f(x)g(x)$ has leading coefficient $a_nb_m$ and, since D is an integral domain, $a_nb_m \neq 0$.

## Theorem 15.2

Let $F$ be a field and let $f(x), g(x) \in F[x]$ with $g(x) \neq 0$. Then
there exist unique polynomials $q(x)$ and $r(x)$ in $F[x]$ such that $f(x) = g(x)q(x) + r(x)$ and either $r(x) = 0$ or $\operatorname{deg} r(x) < \operatorname{deg} g(x)$.

**Proof:** We begin by showing the existence of $q(x)$ and $r(x)$. If $f(x) = 0$ or $\operatorname{deg} f(x) < \operatorname{deg} g(x)$, we simply set $q(x) = 0$ and $r(x) = f(x)$. So, we may assume that $n = \operatorname{deg} f(x) \geq \operatorname{deg} g(x) = m$ and let $f(x) = a_nx_n + \cdots + a_0$ and $g(x) = b_mx_m + \cdots + b_0$. The idea behind this proof is to begin just as if you were going to "long divide" $g(x)$ into $f(x)$, then use the Second Principle of Mathematical Induction on $\operatorname{deg} f(x)$ to finish up. Thus, resorting to long division, we let $f_1(x) = f(x) - a_nb_m^{-1}x^{n-m}g(x)$. Then, $f_1(x) = 0$ or $\operatorname{deg} f_1(x) < \operatorname{deg} f(x)$; so, by our induction hypothesis, there exist $q_1(x)$ and $r_1(x)$ in $F[x]$ such that $f_1(x) = g(x)q_1(x) + r_1(x)$, where $r_1(x) = 0$ or $\operatorname{deg} r_1(x) < \operatorname{deg} g(x)$. [Technically, we should get the induction started by proving the case in which $\operatorname{deg} f(x) = 0$, but this is trivial.] Thus, $f(x) = a_nb_m^{-1}x^{n-m}g(x) + f_1(x) = a_nb_m^{-1}x^{n-m}g(x) + q_1(x)g(x) + r_1(x)$ = $[a_nb_m^{-1}x^{n-m} + q_1(x)]g(x) + r_1(x)$. So, the polynomials $q(x) = a_nb_m^{-1}x^{n-m} + q_1(x)$ and $r(x) = r_1(x)$ have the desired properties. Proving uniqueness is easy. $\blacksquare$

---

When the ring of coefficients of a polynomial ring is a field, we can use the long
division process to determine the quotient and remainder.

Let $D$ be an integral domain. If $f(x)$ and $g(x)$ $\in D[x]$, we say that $g(x)$ divides $f(x)$ in $D[x]$ [and write $g(x) | f(x)$] if there exists an $h(x) \in D[x]$ such that $f(x) = g(x)h(x)$. In this case, we also call $g(x)$ a factor of $f(x)$. An element $a$ is a zero (or a root) of a polynomial $f(x)$ if $f(a) = 0$.

When $F$ is a field, $a \in F$, and $f(x) \in F[x]$, we say that $a$ is a zero of multiplicity $k$ ($k \geq 1)$ if $(x - a)^k$ is a factor of $f(x)$ but $(x - a)^{k+1}$ is not a factor of $f(x)$.

**Corollary 1: (Remainder Theorem)** Let $F$ be a field, $a \in F$, and $f(x) \in F[x]$. Then $f(a)$ is the remainder in
the division of $f(x)$ by $x - a$.

**Corollary 2: (Factor Theorem)** Let $F$ be a field, $a \in F$, and $f(x) \in F[x]$. Then $a$ is a zero of $f(x)$ if
and only if $x - a$ is a factor of $f(x)$.

**Corollary 3:** A polynomial of degree $n$ over a field has at most $n$ zeros, counting
multiplicity.

**Proof:** We proceed by induction on $n$. Clearly, a polynomial of degree 0 over a field has no zeros. Now suppose that $f(x)$ is a polynomial of degree $n$ over a field and $a$ is a zero of $f(x)$ of multiplicity $k$. Then, $f(x) = (x - a)^kq(x)$ and $q(a) \neq 0$; and, since $n = \operatorname{deg} f(x) = \operatorname{deg} (x - a)^k q(x) = k + \operatorname{deg} q(x)$, we have $k \leq n$ (As o/w...). If $f(x)$ has no zeros other than $a$, we are done. On the other hand, if $b \neq a$ and $b$ is a zero of $f(x)$, then $0 = f(b) = (b - a)^kq(b)$, so that $b$ is also a zero of $q(x)$ with the same multiplicity as it has for $f(x)$. By the Second Principle of Mathematical Induction, we know that $q(x)$ has at most $\operatorname{deg} q(x) = n - k$ zeros, counting multiplicity. Thus, $f(x)$ has at most $k + n - k = n$ zeros, counting multiplicity.

---

A principal ideal domain is an integral domain $R$ in which every ideal
has the form $\langle a\rangle = \\{ra \mid r \in R\\}$ for some $a$ in $R$.

## Theorem 15.3

Let $F$ be a field. Then $F[x]$ is a principal ideal domain.

**Proof:** By Theorem 15.1, we know that $F[x]$ is an integral domain. Now, let $I$ be an ideal in $F[x]$. If $I = \\{0\\}$, then $I = \langle 0\rangle$. If $I \neq \\{0\\}$, then among all the elements of $I$, let $g(x)$ be one of minimum degree. We will show that $I = \langle g(x)\rangle$. Since $g(x) \in I$, we have $\langle g(x)\rangle \subseteq I$. Now let $f(x) \in I$. Then, by the division algorithm, we may write $f(x) = g(x)q(x) + r(x)$, where $r(x) = 0$ or $\operatorname{deg} r(x) < \operatorname{deg} g(x)$. Since $r(x) = f(x) - g(x)q(x) \in I$, the minimality of $\operatorname{deg} g(x)$ implies that the latter condition cannot hold. So, $r(x) = 0$ and, therefore, $f(x) \in \langle g(x)\rangle$. This shows that $I \subseteq \langle g(x)\rangle$.

**Examples:**

* Consider the homomorphism $\phi$ from $R[x]$ onto $C$ given by $\phi(x) \rightarrow \phi(i)$ (that is, evaluate a polynomial in $R[x]$ at $i$). Then $x^2 + 1 \in \operatorname{Ker} \phi$ and is clearly a polynomial of minimum degree in $\operatorname{Ker} \phi$. Thus, $\operatorname{Ker} \phi = \langle x^2 + 1\rangle$ and $R[x]/\langle x^2 + 1\rangle$ is isomorphic to $C$.










