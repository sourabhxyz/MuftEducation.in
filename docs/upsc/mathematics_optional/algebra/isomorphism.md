---
id: isomorphism
title: Isomorphism
sidebar_label: Isomorphism 
---

## Group Homomorphism

A homomorphism $\phi$ from a group $G$ to a group $\overline{G}$ is a mapping
from $G$ into $\overline{G}$ that preserves the group operation; that is, $\phi(a b)=$ $\phi(a) \phi(b)$ for all $a, b$ in $G$.

## Isomorphism

Special case of Homomorphism where $\phi$ (*called as an isomorphism)* is one-to-one and onto. If there is an isomorphism between $G$ onto $\overline{G}$, we say that $G$ and $\overline{G}$ are isomorphic and write $G \approx \overline{G}$.

It is implicit in the definition of isomorphism that isomorphic
groups have the same order. 

Easy to prove that $\phi^{-1}$ is as well an isomorphism.

**Examples:**

* Any infinite cyclic group is isomorphic to $Z$. Indeed, if $a$ is a generator of the cyclic group, the mapping $a^{k} \rightarrow k$ is an
  isomorphism. Any finite cyclic group $\langle a\rangle$ of order $n$ is isomorphic to $Z_{n}$ under the mapping $a^{k} \rightarrow k \bmod n .$ That these correspondences are functions and are one-to-one is the essence of Theorem 4.1. Obviously,
  the mappings are onto. That the mappings are operation-preserving
  follows from Exercise 9 in Chapter 0 in the finite case and from the
  definitions in the infinite case.
* $U(10) \not \approx U(12) .$ This is a bit trickier to prove. First, note that $x^{2}=1$ for all $x$ in $U(12) .$ Now, suppose that $\phi$ is an isomorphism from $U(10)$ onto $U(12) .$ Then

  $$
  \phi(9)=\phi(3 \cdot 3)=\phi(3) \phi(3)=1
  $$
  and,
  $\phi(1)=\phi(1 \cdot 1)=\phi(1) \phi(1)=1$ Thus, $\phi(9)=\phi(1),$ but $9 \neq 1,$ which contradicts the assumption that $\phi$ is one-to-one.

* There is no isomorphism from $Q$, the group of rational numbers under addition, to $Q^{*},$ the group of nonzero rational numbers
  under multiplication. If $\phi$ were such a mapping, there would be a ra-
  tional number $a$ such that $\phi(a)=-1 .$ But then $-1=\phi(a)=\phi\left(\frac{1}{2} a+\frac{1}{2} a\right)=\phi\left(\frac{1}{2} a\right) \phi\left(\frac{1}{2} a\right)=\left[\phi\left(\frac{1}{2} a\right)\right]^{2}$ However, no rational number squared is $-1$
  
* Any two cyclic group of order $m$ are isomorphic. (easy)

The relation of being isomorphic is an equivalence relation on groups:

* **Reflexivity:** The identity map is an isomorphism from any group to itself.
* **Symmetry:** The inverse of an isomorphism is an isomorphism.
* **Transitivity:** if $G$ is isomorphic to $H$ and $H$ is isomorphic to $K$, then $G$ is isomorphic to $K$, via the isomorphism obtained by composing the isomorphisms from $G$ to $H$ and from $H$ to $K$.


## Cayley's Theorem

---

**Theorem 6.1:** Every group is isomorphic to a group of permutations.

**Proof:** To prove this, let $G$ be any group. We must find a group $\overline{G}$ of
permutations that we believe is isomorphic to $G$. Since $G$ is all we have
to work with, we will have to use it to construct $\overline{G}$. For any $g$ in $G$,
define a function $T_g$ from $G$ to $G$ by $T_g(x) = gx$ 
 for all $x$ in $G$. It is easy to see that $T_g$ is a permutation on the of elements of $G$. Now, let $\overline{G}=\left\\{T_{g} | g \in G\right\\} .$ Then, $\overline{G}$ is a group under
the operation of function composition. To verify this, we first observe
that for any $g$ and $h$ in $G$ we have $T_{g} T_{h}(x)=T_{g}\left(T_{h}(x)\right)=T_{g}(h x)=g(h x)=$ $(g h) x=T_{g h}(x),$ so that $T_{g} T_{h}=T_{g h} .$ From this it follows that $T_{e}$ is the
identity and $\left(T_{g}\right)^{-1}=T_{g^{-1}} .$ since function composition
is associative, we have verified all the conditions for $\overline{G}$ to be a group.

The isomorphism $\phi$ between $G$ and $\overline{G}$ is now ready-made. For every
$g$ in $G,$ define $\phi(g)=T_{g} .$ If $T_{g}=T_{h},$ then $T_{g}(e)=T_{h}(e)$ or $g e=h e$ Thus, $g=h$ and $\phi$ is one-to-one. By the way $\overline{G}$ was constructed, we
see that $\phi$ is onto. The only condition that remains to be checked is that
$\phi$ is operation-preserving. To this end, let $a$ and $b$ belong to $G .$ Then $\phi(a b)=T_{a b}=T_{a} T_{b}=\phi(a) \phi(b)$

---

**Corollary:** Another way to say Cayley's theorem is that, for finite group $G$, $n = |G|$, there exist a homomorphism $\phi: G \rightarrow S_n$ which is injective.

The group $\overline{G}$ constructed previously is called the left regular repre-
sentation of $G$.

## Properties of Isomorphisms

---

**Theorem 6.2:** Suppose that $\phi$ is an isomorphism from a group $G$ onto a group $\overline{G}$ .
Then

1. $\phi$ carries the identity of $G$ to the identity of $\overline{G}$ (easy to see).
2. For every integer $n$ and for every group element $a$ in $G, \phi\left(a^{n}\right)=$ $\quad[\phi(a)]^{n} .$ (equivalent to saying $\phi(a^{-1}) = \phi(a)^{-1}$ which is easy to see)
3. For any elements $a$ and $b$ in $G, a$ and $b$ commute if and only if $\phi(a)$ and $\phi(b)$ commute. (easy to see, thus $G$ is abelian iff $\overline{G}$ is abelian)
4. $G=\langle a\rangle$ if and only if $\overline{G}=\langle\phi(a)\rangle$ (easy... and thus $G$ is cyclic iff $\overline{G}$ is cyclic)
5. $|a|=|\phi(a)|$ for all $a$ in $G$ (isomorphisms preserve orders).
6. For a fixed integer $k$ and a fixed group element $b$ in $G,$ the
  equation $x^{k}=b$ has the same number of solutions in $G$ as does
  the equation $x^{k}=\phi(b)$ in $\overline{G}$ . (easy to see, remember that our map is injective)
7. If $G$ is finite, then $G$ and $\overline{G}$ have exactly the same number of
  elements of every order. (follows from 5 and the fact that map is bijective)

8. $\phi(Z(G))=Z(\overline{G})$ (easy...)
9. If $K$ is a subgroup of $G,$ then $\phi(K)=\\{\phi(k) | k \in K\\}$ is $a$
  subgroup of $\overline{G}$ . (easy...)
10. If $\overline{K}$ is a subgroup of $\overline{G},$ then $\phi^{-1}(\overline{K})=\\{g \in G | \phi(g) \in \overline{K}\\}$ is
  a subgroup of $G .$ (easy...)
---

When the group operation is addition, property 2 of Theorem 6.2 is
$\phi(n a)=n \phi(a) ;$ property 4 says that an isomorphism between two
cyclic groups takes a generator to a generator.

Property 6 is quite useful for showing that two groups are not iso-
morphic. Often $b$ is picked to be the identity. For example, consider $\mathbf{C}^{\*}$
and $\mathbf{R}^{\*} .$ Because the equation $x^{4}=1$ has four solutions in $\mathbf{C}^{\*}$ but only
two in $\mathbf{R}^{\*},$ no matter how one attempts to define an isomorphism from
$\mathbf{C}^{\*}$ to $\mathbf{R}^{\*},$ property 6 cannot hold.

## Automorphism

An isomorphism from a group $G$ onto itself is called an automorphism
of $G$.

### Inner Automorphism induced by $a$

---

Let $G$ be a group, and let $a \in G .$ The function $\phi_{a}$ defined by $\phi_{a}(x)=$
$a x a^{-1}$ for all $x$ in $G$ is called the inner automorphism of $G$ induced by $a$ (It is easy to see that it is actually an automorphism of $G$, it is also denoted as $L_a$).

---

When $G$ is a group, we use $Aut(G)$ to denote the set of all auto-
morphisms of $G$ and $Inn(G)$ to denote the set of all inner automor-
phisms of $G$. 

---

**Theorem 6.3:** $Aut(G), Inn(G)$ is a group under the operation of function composition (easy to prove).

---

**Examples:** 
- To determine $\operatorname{Inn}\left(D_{4}\right),$ we first observe that the complete list of inner
  automorphisms is $\phi_{R_{0}}, \phi_{R_{90}}, \phi_{R_{180}}, \phi_{R_{270}}, \phi_{H}, \phi_{V}, \phi_{D},$ and $\phi_{D^{\prime}} .$ Our job is
  to determine the repetitions in this list. Since $R_{180} \in Z\left(D_{4}\right),$ we have
  $\phi_{R_{180}}(x)=R_{180} x R_{180}^{-1}=x,$ so that $\phi_{R_{180}}=\phi_{R_{0}} .$ Also, $\phi_{R_{270}}(x)=$ $R_{270} x R_{270}^{-1}=R_{90} R_{180} x R_{180}^{-1} R_{90}^{-1}=R_{90} x R_{90}^{-1}=\phi_{R_{90}}(x) .$ Similarly,
  since $H=R_{180} V$ and $D^{\prime}=R_{180} D,$ we have $\phi_{H}=\phi_{V}$ and $\phi_{D}=\phi_{D^{\prime}}$
  This proves that the previous list can be pared down to $\phi_{R_{0}}, \phi_{R_{90}}, \phi_{H}$
  and $\phi_{D} .$ It can be seen that these are distinct

  *Evidently, computing $Inn(G)$ is straightforward unlike $Aut(G)$*

- To compute Aut ($Z_{10}$), we try to discover enough information about an
element $\alpha$ of Aut ($Z_{10}$) to determine how $\alpha$ must be defined. Because $Z_{10}$
is so simple, this is not difficult to do. To begin with, observe that once
we know $\alpha(1),$ we know $\alpha(k)$ for any $k$ , because it is cyclic and also as $|\alpha(1)| = 10$, we have four candidates for $\alpha(1)$

$\alpha(1)=1, \quad \alpha(1)=3, \quad \alpha(1)=7, \quad \alpha(1)=9$

Now $\alpha_{3}(a+b)=3(a+b)=3 a+3 b=\alpha_{3}(a)+\alpha_{3}(b)$, we see that $\alpha_3$ is operation preserving and hence is an automorphism, similarly $\alpha_7$ and $\alpha_9$ are also automorphisms.

This gives us the elements of $\operatorname{Aut}\left(Z_{10}\right)$ but not the structure. For in-
stance, what is $\alpha_{3} \alpha_{3} ?$ Well, $\left(\alpha_{3} \alpha_{3}\right)(1)=\alpha_{3}(3)=3 \cdot 3=9=\alpha_{9}(1),$ so $\alpha_{3} \alpha_{3}=\alpha_{9} .$ Similar calculations show that $\alpha_{3}^{3}=\alpha_{7}$ and $\alpha_{3}^{4}=\alpha_{1},$ so
that $\left|\alpha_{3}\right|=4 .$ Thus, Aut $\left(Z_{10}\right)$ is cyclic. Actually, the following Cayley tables reveal that Aut $\left(Z_{10}\right)$ is isomorphic to $U(10)$

$\begin{array}{c|cccc}{U(10)} & {1} & {3} & {7} & {9} \\\ \hline 1 & {1} & {3} & {7} & {9} \\\ {3} & {3} & {9} & {1} & {7} \\\ {7} & {7} & {1} & {9} & {3} \\\ {9} & {9} & {7} & {3} & {1}\end{array}$

$\begin{array}{c|cccc}{\operatorname{Aut}\left(Z_{10}\right)} & {\boldsymbol{\alpha_{1}}} & {\boldsymbol{\alpha_{3}}} & {\boldsymbol{\alpha_{7}}} & {\boldsymbol{\alpha_{9}}} \\\ \hline \boldsymbol{\alpha_{1}} & {\alpha_{1}} & {\alpha_{3}} & {\alpha_{7}} & {\alpha_{9}} \\\ {\boldsymbol{\alpha_{3}}} & {\alpha_{3}} & {\alpha_{9}} & {\alpha_{1}} & {\alpha_{7}} \\\ {\boldsymbol{\alpha_{7}}} & {\alpha_{7}} & {\alpha_{1}} & {\alpha_{9}} & {\alpha_{3}} \\\ {\boldsymbol{\alpha_{9}}} & {\alpha_{9}} & {\alpha_{7}} & {\alpha_{3}} & {\alpha_{1}}\end{array}$

---

**Theorem 6.5:** For every positive integer $n, \operatorname{Aut}\left(Z_{n}\right)$ is isomorphic to $U(n)$

**Proof:** Any automorphism $\alpha$ is determined by the
value of $\alpha(1)$, and $\alpha(1) \in U(n)$. Now consider the correspondence
from $Aut(Zn) \text{ to } U(n)$ given by $T: \alpha → \alpha(1)$. Clearly it is one - one and onto. To see that it is operation preserving, we have, $T(\alpha \beta) = \alpha(\beta(1)) = \beta(1)\alpha(1) = \alpha(1)\beta(1) = T(\alpha)T(\beta)$. 

---

