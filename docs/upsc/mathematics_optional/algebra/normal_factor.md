---
id: normal_factor
title: Normal Subgroups and Factor Groups
sidebar_label: Normal Subgroups and Factor Groups
---


## Normal Subgroup

A subgroup $H$ of a group $G$ is called a normal subgroup of $G$ if $a H=$
$Ha$ for all $a$ in $G .$ We denote this by $H \triangleleft G .$

---

**Theorem 9.1: (Normal Subgroup Test)** A subgroup $H$ of $G$ is normal in $G$ if and only if $x H x^{-1} \subseteq H$
for all $x$ in $G .$  (Weaker version of what was shown in 7th chapter)

**Proof:** Converse is only required to be proved. Consider any $h \in H \rightarrow x^{-1}hx (= b \text{ say }) \in H$ $\rightarrow xbx^{-1} \in xHx^{-1} \rightarrow h \in xHx^{-1}$

---


**Examples:**

*Unless proof is given, assume it was easy*

- Every subgroup of an Abelian group is normal.
- The center $Z(G)$ of a group is always normal.
- The alternating group $A_n$ of even permutations is a normal subgroup of $S_n$.
-  Every subgroup of $D_n$ consisting solely of rotations is normal in $D_n$. 
-  Let $H$ be a normal subgroup of a group $G$ and $K$ be any subgroup of $G .$ Then $H K=\\{h k | h \in H, k \in K\\}$ is a subgroup of $G$.
-  If a group $G$ has a unique subgroup $H$ of some finite
  order, then $H$ is normal in $G$. To see that this is so, observe that for any $g \in G, g H g^{-1}$ is a subgroup of $G$ and $|g H g^{-1}|=| H |$.

## Factor Groups or Quotient Groups

---

**Theorem 9.2:** Let $G$ be a group and let $H$ be a normal subgroup of $G .$ The set
$G / H=\{a H | a \in G\}$ is a group under the operation $(a H)(b H)=a b H$ (easy to prove)

**Proof:** Group axioms are easy to verify but we must verify that the function is well defined, so we need to check whether single element gets map to exactly one element, so consider $a, a', b, b' \in G \text{ and } aH = a'H, bH = b'H$ to show $abH = a'b'H$ i.e. to show $ab \in a'b'H$, $a = a'h_1, b = b'h_2, ab = a'h_1b'h_2 = a'b'h_3h_2$

---

Converse of
Theorem 9.2 is also true; that is, if the correspondence $aHbH = abH$ defines a group operation on the set of left cosets of $H$ in $G$, then $H$ is
normal in $G$.

**Examples:**

- Let $4Z = \\{0, \pm 4, \pm 8, . . .\\}$. To construct $Z/4Z$, we
  first must determine the left cosets of $4Z$ in $Z$. Which are

  $0+4 Z=4 Z=\\{0, \pm 4, \pm 8, \ldots\\}$
  
  $1+4 Z=\\{1,5,9, \ldots ;-3,-7,-11, \ldots\\}$

  $2+4 Z=\\{2,6,10, \ldots ;-2,-6,-10, \ldots\\}$

  $3+4 Z=\\{3,7,11, \ldots ;-1,-5,-9,-9, \ldots\\}$

  Cayley's table

  $\begin{array}{l|llll} {} & {0 + 4Z} & {1 + 4Z} & {2 + 4Z} & {3 + 4Z} \\\ \hline {0 + 4Z} & {0 + 4Z} & {1 + 4Z} & {2 + 4Z} & {3 + 4Z} \\\ {1 + 4Z} & {1 + 4Z} & {2 + 4Z} & {3 + 4Z} & {0 + 4Z} \\\ {2 + 4Z} & {2 + 4Z} & {3 + 4Z} & {0 + 4Z} & {1 + 4Z} \\\ {3 + 4Z} & {3 + 4Z} & {0 + 4Z} & {1 + 4Z} & {2 + 4Z} \end{array}$

  Clearly, then, $Z / 4 Z \approx Z_{4} .$ More generally, if for any $n>0$ we let $n Z=$ $\\{0, \pm n, \pm 2 n, \pm 3 n, \ldots\\},$ then $Z / n Z$ is isomorphic to $Z_{n}$
  