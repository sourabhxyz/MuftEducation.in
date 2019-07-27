---
id: subgroups
title: SubGroups 
sidebar_label: SubGroups 
---
**Definition: (Order of a group)** The number of elements of a group (finite or infinite) is called its order. We will use $\vert G \vert$ to denote the order of $G$.

**Definition: (Order of an element)** The order of an element $g$ in a group $G$ is the smallest positive integer $n$ such that $g^n = e$. (In additive notation, this would mean $ng = 0$.) If no such integer exists, we say that $g$ has infinite order. The order of an element $g$ is denoted by $\vert g \vert$

**Example:** Consider U(15) = {1, 2, 4, 7, 8, 11, 13, 14} under multiplication modulo 15. This group has order 8. $\vert 13 \vert$? Soln: Compute $13^1, 13^2, 13^3, 13^4$ to get answer as 4, however there is trick: $13 = -2 \bmod 15 \Rightarrow 13^2 = (-2)^2 = 4, 13^3 = -2 \cdot 4 = -8, 13^4 = (-2)(-8) = 1.$

**Example:** Consider $Z$ under ordinary addition. Here every nonzero element has infinite order, since the sequence $a, 2a, 3a, \dots$ never includes 0 when $a \neq 0$.

**Definition: (Subgroup)** If a subset $H$ of a group $G$ is itself a group under the operation of $G$, we say that $H$ is a subgroup of $G$.

We use the notation $H \leq G$ to mean that $H$ is a subgroup of $G$. If we want to indicate that $H$ is a subgroup of $G$ but is not equal to $G$ itself, we write $H < G$. Such a subgroup is called a proper subgroup. The subgroup ${e}$ is called the trivial subgroup of $G$; a subgroup that is not ${e}$ is called a nontrivial subgroup of G.

When determining whether or not a subset $H$ of a group $G$ is a subgroup of G, one need not directly verify the group axioms as it will become evident from discussion below.

**Theorem 1: (One-Step Subgroup Test)**
Let $G$ be a group and $H$ a nonempty subset of $G$. If $ab^{-1}$ is in $H$ whenever $a$ and $b$ are in $H$, then $H$ is a subgroup of $G$. (In additive notation, if $a - b$ is in $H$ whenever $a$ and $b$ are in $H$, then $H$ is a subgroup of $G$.)

**Proof:** Since the operation of $H$ is the same as that of $G$, it is clear that this operation is associative. Next, we show that $e$ is in $H$. Since $H$ is nonempty, we may pick some $x$ in H. Then, letting $a = x$ and $b = x$ in the hypothesis, we have $e = xx^{-1} = ab^{-1}$ is in $H$. To verify that $x^{-1}$ is in $H$ whenever $x$ is in $H$, all we need to do is to choose $a = e$ and $b = x$ in the statement of the theorem. Finally, the proof will be complete when we show that $H$ is closed; that is, if $x, y$ belong to $H$, we must show that $xy$ is in $H$ also. Well, we have already shown that $y^{-1}$ is in $H$ whenever $y$ is; so, letting $a = x$ and $b = y^{-1}$, we have $xy = x(y^{-1})^{-1} = ab^{-1}$ is in $H$.

:::tip Tip 
To apply the above theorem, follow these steps:-

1. Identify the property $P$ that distinguishes the elements of $H$; that is, identify a defining condition.
2. Prove that the identity has property $P$. (This verifies that $H$ is nonempty.)
3. Assume that two elements $a$ and $b$ have property $P$.
4. Use the assumption that $a$ and $b$ have property $P$ to show that $ab^{-1}$ has property $P$.
:::
**Example (easy):** Let $G$ be an Abelian group under multiplication with identity $e$. Then $H = \\{x^2 \mid x \in G\\}$ is a subgroup of $G$. Since $e^2 = e$, the identity has the correct form. Next, we write two elements of $H$ in the correct form, say, $a^2$ and $b^2$. We must show that $a^2(b^2)^{-1}$ also has the correct form; that is, $a^2(b^2)^{-1}$ is the square of some element. Since $G$ is Abelian, we may write it as $(ab^{-1})^2$, which is the correct form. Thus, $H$ is a subgroup of $G$.

**Theorem 2: (Two-Step Subgroup Test)**
Let $G$ be a group and let $H$ be a nonempty subset of $G$. If $ab$ is in $H$ whenever $a$ and $b$ are in $H$ ($H$ is closed under the operation), and $a^{-1}$ is in $H$ whenever $a$ is in $H$ ($H$ is closed under taking inverses), then $H$ is a subgroup of $G$.

**Proof:**
By Theorem 1, it suffices to show that $a, b \in H$ implies $ab^{-1} \in H$. So, we suppose that $a, b \in H$. Since $H$ is closed under taking inverses, we also have $b^{-1} \in H$. Thus, $ab^{-1} \in H$ by closure under multiplication.

:::note Note
Let $G$ be an Abelian group and $H$ and $K$ be subgroups of $G$. Then $HK = \\{hk \mid h \in H, k \in K\\}$ is a subgroup of $G$. (Easy to show.)
:::

How do you prove that a subset of a group is not a subgroup? Here are three possible ways, any one of which guarantees that the subset is not a subgroup:

1. Show that the identity is not in the set.
2. Exhibit an element of the set whose inverse is not in the set.
3. Exhibit two elements of the set whose product is not in the set.

When dealing with finite groups, it is easier to use the following subgroup test.

**Theorem 3: (Finite Subgroup Test)** Let $H$ be a nonempty finite subset of a group $G$. If $H$ is closed under the operation of $G$, then $H$ is a subgroup of $G$.

**Proof:** In view of Theorem 2, we need only prove that $a^{-1} \in H$ whenever $a \in H$. If $a = e$, then $a^{-1} = a$ and we are done. If $a \neq e$, consider the sequence $a, a^2, \dots$ By closure, all of these elements belong to $H$. Since $H$ is finite, not all of these elements are distinct. Say $a^i = a^j$ and $i > j$. Then, $a^{i-j} = e$; and since $a \neq e, i - j > 1$. Thus, $aa^{i-j-1} = a^{i-j} = e$ and, therefore, $a^{i-j-1} = a^{-1}$. But $i - j - 1 \geq 1$ implies $a^{i-j-1} \in H$ and we are done. $\blacksquare$

## Cyclic Subgroups

For any element $a$ from a group, we let $\<a\>$ denote the set $\\{a^n \mid n \in Z\\}$. In particular, observe that the exponents of $a$ include all negative integers as well as 0 and the positive integers ($a^0$ is defined to be the identity). _Clearly it forms a subgroup_. This subgroup is called the cyclic subgroup of $G$ generated by $a$.
In the case that $G = \<a\>$, we say that $G$ is cyclic and $a$ is a generator of $G$. (A cyclic group may have many generators.) Notice that although the list $\dots, a^{-2}, a^{-1}, a^0, a^1, a^2, \dots$ has infinitely many entries, the set $\\{a^n \mid n \in Z\\}$ might have only finitely many elements. Also note that, since $a^ia^j = a^{i+j} = a^{j+i} = a^ja^i$, every cyclic group is Abelian.

**Example:** In $D_n$, the dihedral group of order $2n$, let $R$ denote a rotation of $360/n$ degrees. Then,
$R^n = R\_{360°} = e, R^{n+1} = R, R^{n+2} = R^2, \dots$ Similarly, $R^{-1} = R^{n-1}, R^{-2} = R^{n-2}, \dots$, so that $\<R\> = \\{e,R, \dots, R^{n-1}\\}$. We see, then, that the powers of $R$ "cycle back" periodically.

For any element $a$ of a group $G$, it is useful to think of $\<a\>$ as the smallest subgroup of $G$ containing $a$. This notion can be extended to any collection $S$ of elements from a group $G$ by defining $\<S\>$ as the subgroup of $G$ with the property that $\<S\>$ contains $S$ and if $H$ is any subgroup of $G$ containing $S$, then $H$ also contains $\<S\>$. Thus, $\<S\>$ is the smallest subgroup of $G$ that contains $S$. The set $\<S\>$ is called the subgroup generated by $S$.

**Example:** in $Z, <8, 13> = Z$; in $C, <1, i> = \\{a + bi \mid a, b \in Z\\}$ (This group is called the "Gaussian integers"); in $R$, the group of real numbers under addition, $<2, \pi, \sqrt{2}> = \\{2a + b\pi + c\sqrt{2} \mid a, b, c \in Z\\}$; in a group in which $a, b, c,$ and $d$ commute, $< a, b, c, d> = \\{a^qb^rc^sd^t \mid q, r, s, t \in Z\\}$.

## Center of a Group

The center, $Z(G)$, of a group $G$ is the subset of elements in $G$ that commute with every element of $G$. In symbols, $Z(G) = \\{a \in G \mid ax = xa$ for all $x$ in G$\\}$.

**Theorem 4: Center is a Subgroup** The center of a group $G$ is a subgroup of $G$ (easy to prove)

**Example** For $n \geq 3$,

<script type="math/tex">% <![CDATA[
Z(D_n) =
\begin{cases} 
  \{R_0, R_{180}\} & \text{when n is even}\\ 
  \{R_0\} & \text{when n is odd} 
\end{cases} %]]></script>

To verify this, first observe that since every rotation in $D\_n$ is a power of $R\_{360/n}$, rotations commute with rotations. We now investigate when a rotation commutes with a reflection. Let $R$ be any rotation in $D\_n$ and let $F$ be any reflection in $D\_n$. Observe that since $RF$ is a reflection we have $RF = (RF)^{-1} = F^{-1}R^{-1} = FR^{-1}$. Thus, it follows that $R$ and $F$ commute if and only if $FR = RF = FR^{-1}$. By cancellation, this holds if and only if $R = R^{-1}$. But $R=R^{-1}$ only when $R=R\_0$ or $R=R\_{180}$, and $R\_{180}$ is in $D_n$ only when $n$ is even. So, we have proved that $Z(D_n) = \\{R_0\\}$ when $n$ is odd and $Z(D\_n) = \\{R_0, R\_{180}\\}$ when $n$ is even.

## Centralizer of $a$ in $G$

Let $a$ be a fixed element of a group $G$. The centralizer of $a$ in $G$, $C(a)$, is the set of all elements in $G$ that commute with $a$. In symbols, $C(a) = \\{g \in G \mid ga = ag\\}$.

**Theorem 5: $C(a)$ Is a Subgroup** (Easy to prove)

Notice that for every element $a$ of a group $G$, $Z(G) \subseteq C(a)$. Also, observe that $G$ is Abelian if and only if $C(a) = G$ for all $a$ in $G$.

**Example:** In $D\_4$, we have the following centralizers:
$C(R\_0) = D\_4 = C(R\_{180})$,

$C(R\_{90}) = \\{R\_0, R\_{90}, R\_{180}, R\_{270}\\} = C(R\_{270})$,

$C(H) = \\{R\_0, H, R\_{180}, V\\} = C(V),$

$C(D) = \\{R\_0, D, R\_{180}, D'\\} = C(D')$.
