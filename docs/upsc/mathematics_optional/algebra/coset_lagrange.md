---
id: coset_lagrange
title: Cosets and Lagrange's Theorem
sidebar_label: Cosets and Lagrange's Theorem
---

## Coset of $H$ in $G$

Let $G$ be a group and let $H$ be a nonempty subset of $G .$ For any $a \in G,$
the set $\\{a h | h \in H\\}$ is denoted by $a H .$ Analogisly, $H a=\\{h a | h \in H\\}$
and $a H a^{-1}=\left \\{a h a^{-1} | h \in H\right \\} .$ When $H$ is a subgroup of $G,$ the set $a H$ (in additie notation $a + H$) is called the left coset of $H$ in $G$ containing $a,$ whereas $H a$ is called the right
coset of $H$ in G containing a. In this case, the element $a$ is called the coset representative of $a H$ (or $H a ) .$ We use $|a H|$ to denote the number of elements in the set $a H,$ and $|H a|$ to denote the number of elements in $H a$.

### Properties of Cosets

Let $H$ be a subgroup of $G,$ and let $a$ and $b$ belong to $G$. Then,
1. $a \in a H .$ (easy to see)
2. $a H=H$ if and only if $a \in H .$ (easy to prove)
3. $(a b) H=a(b H)$ and $H(a b)=(H a) b$ (easy to prove)
4. $a H=b H$ if and only if $a \in b H .$ (easy to prove and thus, any element of a left coset can be used to represent the coset.)
5. $a H=b H$ or $a H \cap b H=\varnothing$ (follows from 4, $ah_1 = bh_2 \rightarrow a = bh_2h_1^{-1}$ $\rightarrow a \in bH$ or alternatively let $c \in aH \cap bH \rightarrow cH = aH = bH$ (from 4))
6. $a H=b H$ if and only if $b^{-1} a \in H .$ (alternate form of 4)
7. $|a H|=|b H|$ (Prove: To prove that $|a H|=|b H|,$ it suffices to define a one-to-one map-
  ping from $a H$ onto $b H .$ Obviously, the correspondence $a h \rightarrow b h$
  maps $a H$ onto $b H .$ That it is one-to-one follows directly from the
  cancellation property.)

  **Corollory:** Thus $|aH| = |H|$ as take $b$ to be an element of $H$.

8. $a H=H a$ if and only if $H=a H a^{-1}$ . (easy to prove)
9. $a H$ is a subgroup of $G$ if and only if $a \in H$. (easy to prove and thus, $H$ itself is the only coset of $H$ that is a subgroup of $G$)

Note that properties $1,5,$ and $7$ of the lemma guarantee that the left cosets of a subgroup $H$ of $G$ partition $G$ into blocks of equal size. Indeed, we may view the cosets of $H$ as a partitioning of $G$ into equivalence classes under the equivalence relation defined by $a \sim b$ if $a H=b H.$ (basically if they are in same partition then by 4 we have this)

**Example:** (Use case of property 5) To find the cosets of $H=\\{1,15\\}$ in $G=U(32)=$ $\\{1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31\\},$ we begin with
$H=\\{1,15\\} .$ We can find a second coset by choosing any element not
in $H,$ say $3,$ as a coset representative. This gives the coset $3 H=\\{3,13\\} .$
We find our next coset by choosing a representative not already appearing in the two previously chosen cosets, say $5 .$ This gives us the coset $5 H=$
$\\{5,11\\} .$ We continue to form cosets by picking elements from $U(32)$
that have not yet appeared in the previous cosets as representatives of
the cosets until we have accounted for every element of $U(32) .$ We then have the complete list of all distinct cosets of $H$

## Lagrange's Theorem

---

**Theorem 7.1:** If $G$ is a finite group and $H$ is a subgroup of $G,$ then $|H|$ divides $|G|$. Moreover, the number of distinct left (right) cosets of $H$ in $G$ is $|G| / |H|$ .

**Proof:** Let $a_{1} H, a_{2} H, \ldots, a_{r} H$ denote the distinct left cosets of $H$ in G. Then, for each $a$ in $G,$ we have $a H=a_{i} H$ for some $i$ . Also, by prop-
erty 1 of the lemma, $a \in a H .$ Thus, each member of $G$ belongs to one
of the cosets $a_{i} H .$ In symbols,

$$
G=a_{1} H \cup \cdots \cup a_{r} H
$$

Now, property 5 of the lemma shows that this union is disjoint, so that

$$
|G|=\left|a_{1} H\right|+\left|a_{2} H\right|+\cdots+\left|a_{r} H\right| .
$$

Finally, since $\left|a_{i} H\right|=|H|$ for each $i,$ we have $|G|=r|H|$

---

:::warning
The converse of Lagrange’s Theorem is false. For example, a group of order 12 need not have a subgroup of order 6.
:::

The **index** of a subgroup $H$ in $G$ is the number of distinct left cosets of $H$ in $G .$ This number
is denoted by $|G : H| .$

**Corollary 1:** If $G$ is a finite group and $H$ is a subgroup of $G,$ then $|G : H|=|G| / H |$ .

**Corollary 2:** $|a|$ Divides $|G|$

**Corollary 3:** A group of prime order is cyclic.

**Proof:**  Suppose that $G$ has prime order. Let $a \in G$ and $a \neq e .$ Then $|\langle a\rangle|$ divides $|G|$ and $|\langle a\rangle| \neq 1 .$ Thus, $|\langle a\rangle|=|G|$ and the corollary follows.

**Corollary 4:** $\boldsymbol{a}^{|G|}=\boldsymbol{e}$

**Corollary 5:** Fermat's Little Theorem, For every integer a and every prime $p, a^{p} \bmod p=a \bmod p$ By the division algorithm, $a=p m+r,$ where $0 \leq r<p$ Thus, $a$ mod $p=r,$ and it suffices to prove that $r^{p}$ mod $p=r .$ If $r=0$
the result is trivial, so we may assume that $r \in U(p) .$ [Recall that
$U(p)=\\{1,2, \ldots, p-1\\}$ under multiplication modulo $p . ]$ Then, by the preceding corollary, $r^{p-1} \bmod p=1$ and, therefore, $r^{p} \bmod p=r$

:::note Note
1. It is relatively easy to prove that if $a, m$ are relatively prime then $a \bmod m (= r), m$ are relatively prime and by similar procedure, we arrive at $r^{\phi(m)} \bmod m = 1$.
2. $U(p)$ for prime $p$ is also denoted as $\mathbb{Z}_p^{\times}$
:::

---

**Theorem 7.2:** For two finite subgroups $H$ and $K$ of a group, define the set
$HK = \\{hk \mid h \in H, k \in K\\}$. Then $|HK| = |H||K|/|H \cap K|$.

**Proof:** Although the set $HK$ has $|H||K|$ products, not all of these
products need represent distinct group elements. That is, we may have
$hk = h'k'$ where $h \neq h'$ and $k \neq k'$. To determine $|HK|$, we must find
the extent to which this happens. For every $t$ in $H \cap K$, the product $hk = (ht)(t^{-1}k)$, so each group element in $HK$ is represented by at least
$|H \cap K|$ products in $HK$. But $hk = h'k'$ implies $t = h^{-1}h' = kk'^{-1} \in H \cap K$, so that $h' = ht$ and $k' = t^{-1}k$. Thus, each element in $HK$ is represented by exactly $|H \cap K|$ products. So, $|HK| = |H||K|/| H \cap K|$.


---

**Examples:**

- A group of order 75 can have at most one subgroup of
  order 25. To see that a group of order 75 cannot have two
  subgroups of order 25, suppose $H$ and $K$ are two such subgroups. Since
  $|H \cap K|$ divides $|H| = 25$ and $|H \cap K| = 1 \text{ or } 5$ results in $|HK| = |H||K|/| H \cap K| = 25 \cdot 25/| H \cap K| = 625 \text{ or } 125$ elements, we have
  that $|H \cap K| = 25$ and therefore $H = K$.

---

**Theorem 7.3:** Let $G$ be a group of order $2p$, where $p$ is a prime greater than 2. Then $G$ is isomorphic to $Z_{2p}$ or $D_p$.

**Proof:** We assume that $G$ does not have an element of order $2p$ and
show that $G \approx D_p$. We begin by first showing that $G$ must have an
element of order $p$. By our assumption and Lagrange’s Theorem, any
nonidentity element of $G$ must have order $2$ or $p$. Thus, to verify our assertion, we may assume that every nonidentity element of $G$ has order $2$. And thus each element is equal to its inverse. Then, for any nonidentity elements $a, b \in G$ with $a \neq b$, the set $\\{e, a, b, ab\\}$ is closed and therefore is a subgroup of $G$ of order 4. Since this contradicts Lagrange’s Theorem, we have proved that $G$ must have an element of order $p$; call it $a$.

Now let $b$ be any element not in $\langle a\rangle .$ Then by Lagrange's Theorem
and our assumption that $G$ does not have an element of order $2 p,$ we
have that $|b|=2$ or $p .$ Because $|\langle a\rangle \cap\langle b\rangle|$ divides $|\langle a\rangle|=p$ and $\langle a\rangle \neq\langle b\rangle$
we have that $|\langle a\rangle \cap\langle b\rangle|=1 .$ But then $|b|=2,$ for otherwise, by Theorem $7.2 \mathrm{l}\langle a\rangle\langle b\rangle|=|\langle a\rangle| |\langle b\rangle\left|=p^{2}>2 p=\right| G |,$ which is impossible. So, any
element of $G$ not in $\langle a\rangle$ has order $ 2 .$ Next consider ab. Since $a b \notin\langle a\rangle,$ our argument above shows that
$|a b|=2 .$ Then $a b=(a b)^{-1}=b^{-1} a^{-1}=b a^{-1} .$ Moreover, this relation completely determines the multiplication table for $G .$ [For example,
$a^{3}\left(b a^{4}\right)=a^{2}(a b) a^{4}=a^{2}\left(b a^{-1}\right) a^{4}=a(a b) a^{3}=a\left(b a^{-1}\right) a^{3}=(a b) a^{2}=$
$\left(b a^{-1}\right) a^{2}=b a$.] since the multiplication table for all noncyclic groups
of order 2$p$ is uniquely determined by the relation $a b=b a^{-1},$ all
noncyclic groups of order 2$p$ must be isomorphic to each other. But of course, $D_{p},$ the dihedral group of order $2 p,$ is one such group.





---