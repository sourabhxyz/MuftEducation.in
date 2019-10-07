---
id: cyclic_groups
title: Cyclic Groups
sidebar_label: Cyclic Groups
---

**Example** The set $Z\_n = \\{0, 1, . . . , n - 1\\}$ for $n \geq 1$ is a cyclic group under addition modulo $n$. As it is in the case for group $Z$, 1 and -1 = n - 1 are generators.

**Example** $Z\_8 = <1> = <3> = <5> = <7>$.

**Theorem 4.1:** Let $G$ be a group, and let $a$ belong to $G$. If $a$ has infinite order, then $a^i = a^j$ if and only if $i = j$. If $a$ has finite order, say, $n$, then $\langle a\rangle = \\{e, a, a^2, . . . , a^{n-1}\\}$ and $a^i = a^j$ if and only if $n$ divides $i - j$. (Easy to prove)

**Corollary** For any group element $a$, $|a| = |< a >|$.

**Corollary** $a^k = e$ Implies That $|a|$ Divides $k$.

What is important about Theorem 4.1 in the finite case is that it says that multiplication in $< a >$ is essentially done by addition modulo $n$. That is, if $(i+j) \bmod n = k$, then $a^ia^j = a^k$.

Thus, no matter what group $G$ is, or how the element $a$ is chosen, multiplication in $< a >$ works the same as addition in $Z\_n$ whenever $|a| = n$. Similarly, if $a$ has infinite order, then multiplication in $< a >$ works the same as addition in $Z$, since $a^ia^j = a^{i+j}$ and no modular arithmetic is done.
For these reasons, the cyclic groups $Z\_n$ and $Z$ serve as prototypes for all cyclic groups, and algebraists say that there is essentially only one cyclic group of each order.

**Theorem 4.2:** Let $a$ be an element of order $n$ in a group and let $k$ be a positive integer. Then $< a^k > = < a^{gcd(n, k)} >$ and $|a^k| = n/gcd(n, k)$.

**Proof:** To simplify the notation, let $d = gcd(n, k)$ and let $k = dr$. Since $a^k = (a^d)^r$, we have by closure that $< a^k > \subseteq < a^d >$ _which is infact true for any divisor of k_. By Theorem 0.2 (the gcd theorem), there are integers $s$ and $t$ such that $d = ns + kt$. So, $a^d = a^{ns+kt} = a^{ns}a^{kt} = (a^n)^s(a^k)^t = e(a^k)^t = (a^k)^t \in < a^k >$. This proves $< a^d > \subseteq < a^k >$. So, we have verified that $< a^k > = < a^{gcd(n,k)} >$. We prove the second part of the theorem by showing first that $|a^d| = n/d$ for any divisor $d$ of $n$. Clearly, $(a^d)^{n/d} = a^n = e$, so that $|a^d| \leq n/d$. On the other hand, if $i$ is a positive integer less than $n/d$, then $(a^d)^i \neq e$ by definition of $|a|$.
$\blacksquare$

**Corollory 1:** In a finite cyclic group, the order of an element divides the order of the group.

**Corollory 2:** Let $|a| = n$. Then $< a^i > = < a^j >$ if and only if $gcd(n, i) = gcd(n, j)$, and $|a^i| = |a^j|$ if and only if $gcd(n, i) = gcd(n, j)$.

**Corollory 3:**  Let $|a| = n$. Then $< a > = < a^j >$ if and only if $gcd(n, j) = 1$, and $|a| = |< a^j >|$ if and only if $gcd(n, j) = 1$.

**Corollory 4:** An integer $k$ in $Z\_n$ is a generator of $Z\_n$ if and only if $gcd(n, k) = 1$.

The value of Corollary 3 is that once one generator of a cyclic group has been found, all generators of the cyclic group can easily be determined.

Let us use it to find all generators of the cyclic group $U(50)$. First, note that direct computations show that $|U(50)| = 20$ and that 3 is one of its generators. Thus, in view of Corollary 3, the complete list of generators for U(50) is
$3 \bmod 50 = 3, 3^3 \bmod 50 = 27, 3^7 \bmod 50 = 37, 3^9 \bmod 50 = 33$,
$3^{11} \bmod 50 = 47, 3^{13} \bmod 50 = 23, 3^{17} \bmod 50 = 13, 3^{19} \bmod 50 = 17$

We should keep in mind that Theorem 4.2 and its corollaries apply only to elements of finite order. Also, $U(n)$ need *not* be cyclic in general for example $U(8)$.

## Classification of Subgroups of Cyclic Groups

---

### Theorem 4.3

Every subgroup of a cyclic group is cyclic. Moreover, if $|< a >| = n$, then the order of any subgroup of $< a >$ is a divisor of $n$; and, for each positive divisor $k$ of $n$, the group $< a >$ has exactly one subgroup of order $k$—namely, $< a^{n/k} >$.

**Proof:** Let $G=\langle a\rangle$ and suppose that $H$ is a subgroup of $G .$ We must show that $H$ is cyclic. If it consists of the identity alone, then clearly $H$ is
cyclic. So we may assume that $H \neq\{e\} .$ We now claim that $H$ contains an element of the form $a^{t},$ where $t$ is positive. since $G=\langle a\rangle,$ every
element of $H$ has the form $a^{t} ;$ and when $a^{t}$ belongs to $H$ with $t<0,$ then
$a^{-t}$ belongs to $H$ also and $-t$ is positive. Thus, our claim is verified. Now
let $m$ be the least positive integer such that $a^{m} \in H .$ By closure, $\left\langle a^{m}\right\rangle \subseteq H .$
We next claim that $H=\left \langle a^{m}\right \rangle .$ To prove this claim, it suffices to let $b$ be an arbitrary member of $H$ and show that $b$ is in $\left\langle a^{m}\right\rangle .$ since $b \in G=\langle a\rangle,$ we
have $ b=a^{k}$ for some $k .$ Now, apply the division algorithm to $k$ and $m$ to
obtain integers $q$ and $r$ such that $k=m q+r$ where $0 \leq r<m .$ Then $a^{k}=$
$a^{m q+r}=a^{m q} a^{r},$ so that $a^{r}=a^{-m q} a^{k} .$ since $a^{k}=b \in H$ and $a^{-m q}=$
$\left(a^{m}\right)^{-q}$ is in $H$ also, $a^{r} \in H .$ But, $m$ is the least positive integer such that
$a^{m} \in H,$ and $0 \leq r<m,$ so $r$ must be $0 .$ The theorem that every sub-
group of a cyclic group is cyclic. 

To prove the next portion of the theorem, suppose that $|\langle a\rangle|=n$ and
$H$ is any subgroup of $\langle a\rangle .$ We have already shown that $H=\left\langle a^{m}\right\rangle,$ where
$m$ is the least positive integer such that $a^{m} \in H .$ Using $e=b=a^{n}$ as in
the preceding paragraph, we have $n=m q .$

Finally, let $k$ be any positive divisor of $n .$ We will show that $\left\langle a^{n / k}\right\rangle$ is
the one and only subgroup of $\langle a\rangle$ of order $ k .$ From Theorem $4.2,$ we see
that $\left\langle a^{n / k}\right\rangle$ has order $n / \operatorname{gcd}(n, n / k)=n /(n / k)=k .$ Now let $H$ be any
subgroup of $\langle a\rangle$ of order $ k .$ We have already shown above that $H=\left\langle a^{m}\right\rangle$ ,
where $m$ is a divisor of $n .$ Then $m=\operatorname{gcd}(n, m)$ and $k=\left|a^{m}\right|=| a^{\operatorname{gcd}(n, m)}|=$ $n / \operatorname{gcd}(n, m)=n / m .$ Thus, $m=n / k$ and $H=\left\langle a^{n / k}\right\rangle$.

---

Taking the group in Theorem 4.3 to be $Z_n$ and $a$ to be 1, we obtain
the following important special case.

**Corollary:** For each positive divisor $k$ of $n,$ the set $\langle n / k\rangle$ is the unique subgroup
of $ Z_{n}$ of order $k$ ; moreover, these are the only subgroups of $Z_{n}$ .

**Corollary:** Only subgroups of $\mathbb{Z}$ are $m\mathbb{Z}$ (i.e. multiples of $m$). (Can be proved in a similar way)

**Examples:**

- To find the generators of the subgroup of order 9 in $Z_{36},$ we observe that $36 / 9=4$ is one generator. To find the others, we
  have from Corollary 3 of Theorem 4.2 that they are all elements of $Z_{36}$
  of the form 4$j$ , where $\operatorname{gcd}(9, j)=1 .$ Thus,

  $$
  \langle 4 \cdot 1\rangle=\langle 4 \cdot 2\rangle=\langle 4 \cdot 4\rangle=\langle 4 \cdot 5\rangle=\langle 4 \cdot 7\rangle=\langle 4 \cdot 8\rangle
  $$

Let $\phi(1)=1,$ and for any integer $n>1,$ let $\phi(n)$ denote the number of positive integers less than $n$ and relatively prime to $n$


---

**Theorem 4.4:** If $d$ is a positive divisor of $n,$ the number of elements of order $d$ in a cyclic group of order $n$ is $\phi(d)$. (Easy to see by above example)

---

Notice that for a finite cyclic group of order $n,$ the number of elements
of order $d$ for any divisor $d$ of $n$ depends only on $d .$ Thus, $Z_{8}, Z_{640},$ and
$Z_{8000}$ each have $\phi(8)=4$ elements of order $8 .$


---

**Corollary:** In a finite group, the number of elements of order d is a multiple
of $\phi(d)$

**Proof:** If a finite group has no elements of order $d,$ the statement is true, since $\phi(d)$ divides $0 .$ Now suppose that $a \in G$ and $|a|=d .$ By
Theorem $4.4,$ we know that $\langle a\rangle$ has $\phi(d)$ elements of order $d .$ If all
elements of order $d$ in $G$ are in $\langle a\rangle,$ we are done. So, suppose that there
is an element $b$ in $G$ of order $d$ that is not in $\langle a\rangle .$ Then, $\langle b\rangle$ also has $\phi(d)$
elements of order $d .$ This means that we have found 2$\phi(d)$ elements of order $d$ in $G$ provided that $\langle a\rangle$ and $\langle b\rangle$ have no elements of order $d$ in
common. If there is an element $c$ of order $d$ that belongs to both $\langle a\rangle$ and
$\langle b\rangle,$ then we have $\langle a\rangle=\langle c\rangle=\langle b\rangle,$ so that $b \in\langle a\rangle,$ which is a contradiction. Continuing in this fashion, we see that the number of elements of order $d$ in a finite group is a multiple of $\phi(d)$.

---


---

### Converse of Theorem 4.3 is true

I.e., if a group $G$ of finite order $n$ has a unique subgroup for every order $d | n$ then $G$ is cyclic.

**Proof:** Let $G = \\{a_1, a_2, \dots, a_n\\}$, define $H = G$. Then taking any element in $H$, we compute $|\langle a_i \rangle| (= k \text{ say})$, then, since we have unique subgroup of order $k$, we have $\phi(k)$ such elements in total in $G$, we will remove such elements from $H$ and continue like this until $H$ becomes empty. Now since order of a subgroup always divides order of the group and the fact that $\sum_{d | n}\phi(d) = n$, we **must** exaust all the divisors of $n$ and thus we will have an element of order $n$.   

---