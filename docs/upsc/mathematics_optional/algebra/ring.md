---
id: ring
title: Introduction to Rings 
sidebar_label: Introduction to Rings
---

---

A ring $R$ is a set with two binary operations, addition (denoted by $a + b$) and multiplication (denoted by $ab$), such that for all $a, b, c$ in $R$:

1. $a + b = b + a$. 
2. $(a + b) + c = a + (b + c)$.
3. There is an additive identity $0$. That is, there is an element $0$ in $R$ such that $a + 0 = a$ for all $a$ in $R$.
4. There is an element $-a$ in $R$ such that $a + (-a) = 0$.
5. $a(bc) = (ab)c$.
6. $a(b + c) = ab + ac \text{ and } (b + c) a = ba + ca$.

---

So, a ring is an Abelian group under addition, also having an associative multiplication that is left and right distributive over addition.
Note that multiplication need not be commutative. When it is, we say
that the ring is commutative. Also, a ring need not have an identity under multiplication. A unity (or identity) in a ring is a nonzero element
that is an identity under multiplication. A nonzero element of a commutative ring with unity need not have a multiplicative inverse. When it
does, we say that it is a unit of the ring. Thus, $a$ is a unit if $a^{-1}$ exists.

The following terminology and notation are convenient. If $a$ and $b$ belong to a commutative ring $R$ and $a$ is nonzero, we say that $a$ divides $b$ (or that $a$ is a factor of $b$) and write $a | b$, if there exists an element $c$ in $R$ such that $b = ac$. If a does not divide $b$, we write $a \not | b$.

Recall that if $a$ is an element from a group under the operation of
addition and $n$ is a positive integer, $na$ means $a + a + \cdots + a$, where
there are $n$ summands. When dealing with rings, this notation can cause
confusion, since we also use juxtaposition for the ring multiplication. When there is the potential for confusion, we will use $n \cdot a$ to mean $a + a + \cdots + a$ ($n$ summands).

We use $b - c$ to denote $b + (-c)$.

If $a, b$, and $c$ belong to a ring, $a \neq 0$ and $ab = ac$, we cannot
conclude that $b = c$. Similarly, if $a^2 = a$, we cannot conclude that $a = 0 \text{ or } 1$


## Subrings

A subset $S$ of a ring $R$ is a subring of $R$ if $S$ is itself a ring with the operations of $R$.

---

**Theorem 11.3:** A nonempty subset $S$ of a ring $R$ is a subring if $S$ is closed under subtraction and multiplication—that is, if $a - b$ and $ab$ are in $S$ whenever $a$ and $b$ are in $S$. (easy...)

---

**Examples:** 

* $\\{0\\}$ and $R$ are subrings of any ring $R$. $\\{0\\}$ is called the trivial subring of $R$.
* $\\{0, 2, 4\\}$ is a subring of the ring $Z_6$, the integers modulo 6. Note that although 1 is the unity in $Z_6$, 4 is the unity in $\\{0, 2, 4\\}$. 
* The set of Gaussian integers $Z[i] = \\{a + bi \mid a, b \in Z\\}$ is a subring of the complex numbers C.
* For each positive integer $n$, the set $nZ = \\{0, \pm n, \pm 2n, \pm 3n, . . .\\}$ is a subring of the integers $Z$.






**Example:** Let $R_1, R_2, . . . , R_n$ be rings. We can use these to construct a new ring as follows. Let
$R_1 \oplus R_2 \oplus \cdots \oplus R_n = \\{(a_1, a_2, . . . , a_n) \mid a_i \in R_i\\}$ and perform componentwise addition and multiplication; that is, define $(a_1, a_2, . . . , a_n) + (b_1, b_2 , . . . , b_n) = (a_1 + b_1, a_2 + b_2, . . . , a_n + b_n)$ 
and
$(a_1, a_2, . . . , a_n)(b_1, b_2, . . . , b_n) = (a_1b_1, a_2b_2, . . . , a_nb_n)$.
This ring is called the direct sum of $R_1, R_2, . . . , R_n$.

## Properties of Rings

---

**Theorem 11.1:** Let $a$, $b$, and $c$ belong to a ring $R$. Then
1. $a0 = 0a = 0$. (easy)
2. $a(-b) = (-a)b = -(ab)$. (easy)
3. $(-a)(-b) = ab.$ (easy, simply from above)
4. $a(b - c) = ab - ac$ and $(b - c)a = ba - ca$. (easy...)
Furthermore, if $R$ has a unity element 1, then
5. $(-1)a = -a$. (from above)
6. $(-1)(-1) = 1$. (from above...)

---

---

**Theorem 11.2:** If a ring has a unity, it is unique. If a ring element has a multiplicative inverse, it is unique. (proof as before)

---





