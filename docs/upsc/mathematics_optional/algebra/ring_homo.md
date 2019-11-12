---
id: ring_homo
title: Ring Homomorphisms
sidebar_label: Ring Homomorphisms
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


A ring homomorphism $\phi$ from a ring $R$ to a ring $S$ is a mapping from
$R$ to $S$ that preserves the two ring operations; that is, for all $a, b$ in $R$,

$\phi(a + b) = \phi(a) + \phi(b)$ and $\phi(ab) = \phi(a)\phi(b)$.

A ring homomorphism that is both one-to-one and onto is called a
ring isomorphism.

---

**Examples:**

* The correspondence $\phi: x \rightarrow 5x$ from $Z_4$ to $Z_{10}$ 
  is a ring homomorphism. Although showing that $\phi(x + y) = \phi(x) + \phi(y)$ appears to be accomplished by the simple statement that $5(x + y) = 5x + 5y$, we must bear in mind that the addition on the left is done modulo 4, whereas the addition on the right and the multiplication on both sides are done modulo 10. An analogous difficulty arises in showing that $\phi$ preserves multiplication. So, to verify that $\phi$ preserves both operations, we write $x + y = 4q_1 + r_1$ and $xy = 4q_2 + r_2$. Then $\phi(x + y) = \phi(r_1) = 5r_1 = 5(x + y - 4q_1)$ $= 5x + 5y - 20q_1 = 5x + 5y = \phi(x) + \phi(y)$ in $Z_{10}$ . Similarly, using the fact that $5 \cdot 5 = 5$ in $Z_{10}$ , we have $\phi(xy) = \phi(r_2) = 5r_2 = 5(xy - 4q_2)$ $= 5xy - 20q_2 = (5 \cdot 5)xy = 5x5y = \phi(x)\phi(y)$ in $Z_{10}$.

* We determine all ring homomorphisms from $Z_{12}$ to $Z_{30}$. By Example in Chapter 10, the only group homomorphisms from $Z_{12}$ to $Z_{30}$ are $x \rightarrow ax$, where $a =$ 0, 15, 10, 20, 5, or 25. But, since $1 \cdot 1 = 1$ in $Z_{12}$, we must have $a \cdot a = a$ in $Z_{30}$. This requirement rules out 20 and 5 as possibilities for $a$. Finally, simple calculations show that each of the remaining four choices does yield a ring homomorphism.

* An integer $n$ with decimal representation $a_ka_{k-1} \cdots a_0$ is divisible by 9 if and only if $a_k + a_{k-1} + \cdots + a_0$ is divisible by 9. To verify this, observe that $n = a_k10^k + a_{k-1}10^{k-1} + \cdots + a_0$. Then, letting $\alpha$ denote the natural homomorphism from $Z$ to $Z_9$ ($z \rightarrow z \bmod 9$) [in particular, $\alpha(10) = 1$], we note that $n$ is divisible by $9$ if and only if $0 = \alpha(n) = \alpha(a_k)(\alpha(10))^k + \alpha(a_{k-1})(\alpha(10))^{k-1} + \cdots + \alpha(a_0)$ $= \alpha(a_k) + \alpha(a_{k-1}) + \cdots + \alpha(a_0) = \alpha(a_k + a_{k - 1} + \cdots + a_0)$. But $\alpha(a_k + a_{k - 1} + \cdots + a_0) = 0$ is equivalent to $a_k + a_{k - 1} + \cdots + a_0$ being divisible by 9.

* Let $m$ be a fixed positive integer. For any integer $a$, let $\overline{a}$ denote $a \bmod m$. It is easy to see that the mapping $\phi: Z[x] \rightarrow Z_m[x]$ given by $\phi(a_nx^n + a_{n-1}x^{n-1} + \cdots + a_0$) $= \overline{a_n}x^n + \overline{a_{n-1}}x^{n-1} + \cdots + \overline{a_0}$ is a ring homomorphism.

## Theorem 14.1

Let $\phi$ be a ring homomorphism from a ring $R$ to a ring $S$. Let $A$ be a
subring of $R$ and let $B$ be an ideal of $S$. (All below mentioned are super easy to prove)

1. For any $r \in R$ and any positive integer $n$, $\phi(nr) = n\phi(r)$ and
$\phi(r^n) = (\phi(r))^n$.
2. $\phi(A) = \\{\phi(a) \mid a \in A\\}$ is a subring of $S$.
3. If $A$ is an ideal and $\phi$ is onto $S$, then $\phi(A)$ is an ideal.
4. $\phi^{-1}(B) = \\{r \in R \mid \phi(r) \in B\\}$ is an ideal of $R$.
5. If $R$ is commutative, then $\phi(R)$ is commutative.
6. If $R$ has a unity 1, $S \neq \\{0\\}$, and $\phi$ is onto, then $\phi(1)$ is the unity of $S$.
7. $\phi$ is an isomorphism if and only if $\phi$ is onto and $\operatorname{Ker} \phi = \\{r \in R \mid \phi(r) = 0\\} = \\{0\\}$.
8. If $\phi$ is an isomorphism from $R$ onto $S$, then $\phi^{-1}$ is an isomorphism from $S$ onto $R$.

**Corollary**: Let $\phi$ be a ring homomorphism from a ring $R$ to a ring $S$. Then $\operatorname{Ker} \phi$ is an ideal of $R$.

## Theorem 14.2 (First Isomorphism theorem for Rings)

Let $\phi$ be a ring homomorphism from $R$ to $S$. Then the mapping from $R/\operatorname{Ker} \phi$ to $\phi(R)$, given by $r + \operatorname{Ker} \phi \rightarrow \phi(r)$, is an isomorphism. In
symbols, $R/\operatorname{Ker} \phi \approx \phi(R)$.

## Theorem 14.3

Every ideal of a ring $R$ is the kernel of a ring homomorphism of $R$.
In particular, an ideal $A$ is the kernel of the mapping $r \rightarrow r + A$ from $R$ to $R/A$.

**Examples:**

* Since the mapping $\phi$ from $Z[x]$ onto $Z$ given by $\phi(f(x)) = f(0)$ is a ring homomorphism with $\operatorname{Ker} \phi = \langle x\rangle$, we have, by Theorem 14.3, $Z[x]/\langle x\rangle \approx Z$. And because $Z$ is an integral domain but not a field, we know by Theorems 13.3 and 13.4 that the ideal $\langle x\rangle$ is prime but not maximal in $Z[x]$.

## Theorem 14.4

Let $R$ be a ring with unity 1. The mapping $\phi: Z \rightarrow R$ given by $n \rightarrow n \cdot 1$ is a ring homomorphism.

**Proof** We have $\phi(m + n) = (m + n) \cdot 1 = m \cdot 1 + n \cdot 1$. So, $\phi$ preserves addition. That $\phi$ also preserves multiplication follows from Example done before, which says that $(m \cdot a)(n \cdot b) = (mn) \cdot (ab)$ for all integers $m$ and $n$. Thus, $\phi(mn) = (mn) \cdot 1 = (mn) \cdot ((1)(1)) = (m \cdot 1)(n \cdot 1) = \phi(m)\phi(n)$. So, $\phi$ preserves multiplication as well.

**Corollary 1:** If $R$ is a ring with unity and the characteristic of $R$ is $n > 0$, then
$R$ contains a subring isomorphic to $Z_n$. If the characteristic of $R$ is 0,
then $R$ contains a subring isomorphic to $Z$.

**Proof:** Let 1 be the unity of $R$ and let $S = \\{k \cdot 1 \mid k \in Z\\}$. Theorem 14.4
shows that the mapping $\phi$ from $Z$ to $S$ given by $\phi(k) = k \cdot 1$ is a homomorphism, and by the First Isomorphism Theorem for rings, we have
$Z/\operatorname{Ker} \phi \approx S$. But, clearly, $\operatorname{Ker} \phi = \langle n\rangle$, where $n$ is the additive order of 1 and, by Theorem 12.3, $n$ is also the characteristic of $R$. So, when $R$ has characteristic $n$, $S \approx Z/\langle n\rangle \approx Z_n.$ When $R$ has characteristic 0, $S \approx Z/\langle 0\rangle \approx Z.$ 

**Corollary 2:** For any positive integer $m$, the mapping of $\phi: Z \rightarrow Z_m$ given by $x \rightarrow x \bmod m$ is a ring homomorphism.

**Proof:** This follows directly from the statement of Theorem 14.4,
since in the ring $Z_m$, the integer $x \bmod m$ is $x \cdot 1$.

**Corollary 3:** If $F$ is a field of characteristic $p$, then $F$ contains a subfield
isomorphic to $Z_p$ . If $F$ is a field of characteristic 0, then $F$ contains
subfield isomorphic to the rational numbers.

**Proof:** By Corollary 1, $F$ contains a subring isomorphic to $Z_p$ if $F$ has characteristic $p$, and $F$ has a subring $S$ isomorphic to $Z$ if $F$ has characteristic 0. In the latter case, let $T = \\{ab^{-1} \mid a, b \in S, b \neq 0\\}$. Then $T$ is isomorphic to the rationals (Let $\phi$ be the isomorphism from $S$ to $Z$, define $T(ab^{-1}) = \phi(a)/\phi(b)$). $\blacksquare$


Since the intersection of all subfields of a field is itself a subfield, every field has a smallest subfield (that is, a subfield that is contained in every subfield). This subfield is called the prime subfield of the field. It follows from Corollary 3 that the prime subfield of a field of characteristic p is isomorphic to $Z_p$, whereas the prime subfield of a field of characteristic 0 is isomorphic to $Q$. 

## Theorem 14.4

Let $D$ be an integral domain. Then there exists a field $F$ (called the
field of quotients of $D$) that contains a subring isomorphic to $D$.

**Proof:** Let $S = \\{(a, b) \mid a, b \in D, b \neq 0\\}$. We define an equivalence
relation on $S$ by $(a, b) \equiv (c, d )$ if $ad = bc$. Now, let $F$ be the set of equivalence classes of $S$ under
the relation $\equiv$ and denote the equivalence class that contains $(x, y)$ by
$x/y$. We define addition and multiplication on $F$ by
$a/b + c/d = (ad + bc)/(bd)$ and $a/b \cdot c/d = (ac)/(bd)$.
(Notice that here we need the fact that $D$ is an integral domain to ensure
that multiplication is closed; that is, $bd \neq 0$ whenever $b \neq 0$ and $d \neq 0$.)
Since there are many representations of any particular element of $F$ ( just as in the rationals, we have 1/2 = 3/6 = 4/8), we must show that these two operations are well-defined. To do this, suppose that $a/b = a'/b'$ and $c/d = c'/d'$, so that $ab' = a'b$ and $cd' = c'd$. It then follows that $(ad + bc)b'd' = adb'd' + bcb'd'$ $= (ab')dd' + (cd')bb' = (a'b)dd' + (c'd)bb'$ $= a'd'bd + b'c'bd = (a'd' + b'c')bd$. Thus, by definition, we have $(ad + bc)/(bd) = (a'd' + b'c')/(b'd')$, and, therefore, addition is well-defined. Similarly, multiplication is well-defined. That $F$ is a field is straightforward. Let 1 denote the unity of $D$. Then $0/1$ is the additive identity of $F$. The additive inverse of $a/b$ is $-a/b;$ the multiplicative inverse of a nonzero element $a/b$ is $b/a$. The remaining field properties can be checked easily. Finally, the mapping $\phi: D \rightarrow F$ given by $x \rightarrow x/1$ is a ring isomorphism from $D$ to $\phi(D)$ 

---

When $F$ is a field, the field of quotients of $F[x]$ is traditionally denoted by $F(x)$.

Let $p$ be a prime. Then $Z_p(x) = \\{f(x)/g(x) \mid f(x), g(x) \in Z_p[x], g(x) \neq 0\\}$ is an infinite field of characteristic $p$.


| D            | Field of fractions (F)                                                |
| ------------ | --------------------------------------------------------------------- |
| $\mathbb{Z}$ | $\mathbb{Q}$                                                          |
| K[X]         | K(X)                                                                  |
| F            | F (as that map will become  surjective as $\frac{a}{b} \sim ab^{-1}$) |


