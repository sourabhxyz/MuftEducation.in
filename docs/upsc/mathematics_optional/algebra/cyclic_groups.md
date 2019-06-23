---
id: cyclic_groups
title: Cyclic Groups
sidebar_label: Cyclic Groups
---

**Example** The set $Z\_n = \\{0, 1, . . . , n - 1\\}$ for $n \geq 1$ is a cyclic group under addition modulo $n$. Again (was in case for group $Z$), 1 and -1 = n - 1 are generators.

**Example** $Z\_8 = <1> = <3> = <5> = <7>$.

**Theorem 4.1:** Let $G$ be a group, and let $a$ belong to $G$. If $a$ has infinite order, then $a\_i = a\_j$ if and only if $i = j$. If $a$ has finite order, say, $n$, then $< a > = \\{e, a, a^2, . . . , a^{n-1}\\}$ and $a\_i = a\_j$ if and only if $n$ divides $i - j$. (Easy to prove)

**Corollary** For any group element $a$, $|a| = |< a >|$.

**Corollary** $a^k = e$ Implies That $|a|$ Divides $k$.

What is important about Theorem 1 in the finite case is that it says that multiplication in $< a >$ is essentially done by addition modulo $n$. That is, if $(i+j) \bmod n = k$, then $a^ia^j = a^k$.

Thus, no matter what group $G$ is, or how the element $a$ is chosen, multiplication in $< a >$ works the same as addition in $Z\_n$ whenever $|a| = n$. Similarly, if $a$ has infinite order, then multiplication in $< a >$ works the same as addition in $Z$, since $a^ia^j = a^{i+j}$ and no modular arithmetic is done.
For these reasons, the cyclic groups $Z\_n$ and $Z$ serve as prototypes for all cyclic groups, and algebraists say that there is essentially only one cyclic group of each order.

**Theorem 4.2:** let $a$ be an element of order $n$ in a group and let $k$ be a positive integer. Then $< a^k > = < a^{gcd(n, k)} >$ and $|a^k| = n/gcd(n, k)$.

**Proof:** To simplify the notation, let $d = gcd(n, k)$ and let $k = dr$. Since $a^k = (a^d)^r$, we have by closure that $< a^k > \subseteq < a^d >$ _which is infact true for any divisor of k_. By Theorem 0.2 (the gcd theorem), there are integers $s$ and $t$ such that $d = ns + kt$. So, $a^d = a^{ns+kt} = a^{ns}a^{kt} = (a^n)^s(a^k)^t = e(a^k)^t = (a^k)^t \in < a^k >$. This proves $< a^d > \subseteq < a^k >$. So, we have verified that $< a^k > = < a^{gcd(n,k)} >$. We prove the second part of the theorem by showing first that $|a^d| = n/d$ for any divisor $d$ of $n$. Clearly, $(a^d)^{n/d} = a^n = e$, so that $|a^d| \leq n/d$. On the other hand, if $i$ is a positive integer less than $n/d$, then $(a^d)^i \neq e$ by definition of $|a|$.
$\blacksquare$

**Corollory 1:** In a finite cyclic group, the order of an element divides the order of the group.

**Corollory 2:** Let $|a| = n$. Then $< a^i > = < a^j >$ if and only if $gcd(n, i) = gcd(n, j)$, and $|a^i| = |a^j|$ if and only if $gcd(n, i) = gcd(n, j)$.

**Corollory 3:** An integer $k$ in $Z\_n$ is a generator of $Z\_n$ if and only if $gcd(n, k) = 1$.

**Corollory 4:**
