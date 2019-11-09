---
id: edp
title: External Direct Products
sidebar_label: External Direct Products
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

---

Let $G_{1}, G_{2}, \ldots, G_{n}$ be a finite collection of groups. The external direct
product of $G_{1}, G_{2}, \ldots, G_{n},$ written as $G_{1} \oplus G_{2} \oplus \cdots \oplus G_{n},$ is the set of
all $n$ -tuples for which the $i$ th component is an element of $G_{i}$ and the operation is componentwise.

---

In symbols,

$$
G_{1} \oplus G_{2} \oplus \cdots \oplus G_{n}=\left\\{\left(g_{1}, g_{2}, \ldots, g_{n}\right) | g_{i} \in G_{i}\right\\}
$$

where $\left(g_{1}, g_{2}, \ldots, g_{n}\right)\left(g_{1}^{\prime}, g_{2}^{\prime}, \ldots, g_{n}^{\prime}\right)$ is defined to be $\left(g_{1} g_{1}^{\prime},\right.$
$g_{2} g_{2}^{\prime}, \ldots, g_{n} g_{n}^{\prime} ) .$ It is understood that each product $g_{i} g_{i}^{\prime}$ is performed
with the operation of $G_{i} .$ Note that in the case that each $G_{i}$ is finite, we
have by properties of sets that $\left|G_{1} \oplus G_{2} \oplus \cdots \oplus G_{n}\right|=\left|G_{1}\right|\left|G_{2}\right| \cdots\left|G_{n}\right|$

It is easy to see that external direct product of
groups is itself a group. And external direct product of abelian groups is an abelion group.

If $A \approx_{\phi} C$, then $A \oplus B \approx C \oplus B$ (easy to see, define $\Phi(a, b) = (\phi(a), b)$)

And $G_1 \oplus G_2 \approx G_2 \oplus G_1$, define $\phi(g_1, g_2) = (g_2, g_1)$.

**Examples:**

- A group of order 4 is isomorphic to $Z_{4}$ or $Z_{2} \oplus Z_{2} .$ To verify this, let $G=$
  $\\{e, a, b, a b\\} .$ If $G$ is not cyclic, then it follows from Lagrange's Theorem
  that $|a|=|b|=|a b|=2 .$ Then the mapping $e \rightarrow(0,0), a \rightarrow(1,0)$, $b \rightarrow(0,1),$ and $a b \rightarrow(1,1)$ is an isomorphism from $G$ onto $Z_{2} \oplus Z_{2}$

---

**Theorem 8.1:** The order of an element in a direct product of a finite number of
finite groups is the least common multiple of the orders of the
components of the element. In symbols,

$\left|\left(g_{1}, g_{2}, \ldots, g_{n}\right)\right|=\operatorname{lcm}\left(\left|g_{1}\right|,\left|g_{2}\right|, \ldots,\left|g_{n}\right|\right)$

(Easy to prove)

---

**Examples:** 

- We determine the number of cyclic subgroups of order
  10 in $Z_{100} \oplus Z_{25}$. 
  We begin by counting the number of elements $(a, b)$ of
  order 10. Possible cases to get LCM 10; (10, 1), ~~(10, 2)~~, (10, 5), ~~(10, 10)~~, ~~(2, 10)~~, ~~(5, 10)~~, (2, 5), ~~(5, 2)~~. That implies answer is $\phi(10) \times 1 + \phi(10) \times \phi(5) + \phi(2) \times \phi(5)$ = $4 + 4 * 4 + 4 = 24$. Because each cyclic
  subgroup of order 10 has four elements of order 10 and no two of the
  cyclic subgroups can have an element of order 10 in common, there
  must be $24/4 = 6$ cyclic subgroups of order 10. 

-  For each divisor $r$ of $m$ and $s$ of $n$, the group $Z_m \oplus Z_n$ has a subgroup isomorphic to $Z_r \oplus Z_s$ (can be proved). To find a subgroup of, say, $Z_{30} \oplus Z_{12}$ isomorphic to $Z_6 \oplus Z_4$, we observe that $<5>$ is a subgroup of $Z_{30}$ of order 6 and $<3>$ is a subgroup of $Z_{12}$ of order 4, so $<5> \oplus <3>$ is the desired subgroup.

---

**Theorem 8.2:** Let $G$ and $H$ be finite cyclic groups. Then $G \oplus H$ is cyclic if and only if $|G|$ and $|H|$ are relatively prime.

**Proof:** Let $|G|=m$ and $|H|=n,$ so that $|G \oplus H|=m n .$ To prove the first half of the theorem, we assume $G \oplus H$ is cyclic and show that
$m$ and $n$ are relatively prime. Suppose that gcd $(m, n)=d$ and $(g, h)$ is a
generator of $G \oplus H .$ since $(g, h)^{m n / d}=\left(\left(g^{m}\right)^{n / d},\left(h^{n}\right)^{m / d}\right)=(e, e),$ we
have $m n=|(g, h)| \leq m n / d .$ Thus, $d=1$ 

To prove the other half of the theorem, let $G=\langle g\rangle$ and $H=\langle h\rangle$ and suppose $\operatorname{gcd}(m, n)=1 .$ Then $,|(g, h)|=\operatorname{lcm}(m, n)=m n=|G \oplus H|,$ so that $(g, h)$ is a generator of $G \oplus H$.

**Corollary 1:** An external direct product $G_{1} \oplus G_{2} \oplus \cdots \oplus G_{n}$ of a finite number
of finite cyclic groups is cyclic if and only if $\left|G_{i}\right|$ and $\left|G_{j}\right|$ are relatively
prime when $i \neq j .$

**Corollary 2:** Let $m=n_{1} n_{2} \cdots n_{k} .$ Then $Z_{m}$ is isomorphic to $Z_{n_{1}} \oplus Z_{n_{2}} \oplus \cdots \oplus Z_{n_{k}}$
if and only if $n_{i}$ and $n_{j}$ are relatively prime when $i \neq j$ . 

---

By using the results above in an iterative fashion, one can express
the same group (up to isomorphism) in many different forms. For example, we have

$Z_{2} \oplus Z_{2} \oplus Z_{3} \oplus Z_{5} \approx Z_{2} \oplus Z_{6} \oplus Z_{5} \approx Z_{2} \oplus Z_{30}$

Similarly,

$\begin{aligned} Z_{2} \oplus Z_{2} \oplus Z_{3} \oplus Z_{5} & \approx Z_{2} \oplus Z_{6} \oplus Z_{5} \\\ & \approx Z_{2} \oplus Z_{3} \oplus Z_{2} \oplus Z_{5} \approx Z_{6} \oplus Z_{10} \end{aligned}$

Thus, $Z_{2} \oplus Z_{30} \approx Z_{6} \oplus Z_{10}$.

## The Group of Units Modulo $n$ as an External Direct Product

If $k$ is a divisor of $n$, let
$U_{k}(n)=\\{x \in U(n) | x \bmod k=1\\}$

It can be readily shown that $U_k(n)$ is indeed a subgroup of $U(n)$.

---

**Theorem 8.3:** Suppose $s$ and $t$ are relatively prime. Then, 

$U(s t) \approx U(s) \oplus U(t)$

Moreover, $U_{s}(s t)$ is isomorphic to $U(t)$ and $U_{t}(s t)$ is isomorphic to $U(s)$

**Proof:**  An isomorphism from $U(st)$ to $U(s) \oplus U(t)$ is $x \rightarrow (x \bmod s, x \bmod t)$ (one-one and onto follows from [Chinese Remainder Theorem](upsc/mathematics_optional/algebra/advance_groups.md), operation preserving is clear; an isomorphism from $U_s(st)$ to $U(t)$ is $x \rightarrow x \bmod t$; an isomorphism from $U_t (st)$ to $U(s)$ is $x \rightarrow x \bmod s$. We leave the verification that
these mappings are operation-preserving, one-to-one, and onto to the
reader.

**Corollary:** Let $m=n_{1} n_{2} \cdots n_{k},$ where $g c d\left(n_{i}, n_{j}\right)=1$ for $i \neq j .$ Then $U(m) \approx U\left(n_{1}\right) \oplus U\left(n_{2}\right) \oplus \cdots \oplus U\left(n_{k}\right)$.

---
