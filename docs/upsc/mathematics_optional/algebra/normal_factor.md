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

A group is called Hamiltonian if it is non-abelian and all its subgroups are normal.

**Examples:**

*Unless proof is given, assume it was easy*

- If every left coset is a right coset, then $H \triangleleft G$.   
  **Proof:** $aH = Hb \rightarrow a \in Hb$ $\rightarrow ab^{-1} \in H$ $\rightarrow Ha = Hb$.
- Every subgroup of an Abelian group is normal.
  - But the converse is not true as consider for example Quaternion group $Q_8 = \langle \overline{e}, i, j, k \mid \overline{e}^2 = e, i^2 = j^2 = k^2 = ijk = \overline{e}\rangle$ where $e$ is the identity element and $\overline{e}$ commutes with the other elements of the group (can be derived). All its subgroups are $\\{e\\}, \\{e, \overline{e}\\}, \\{e, \overline{e}, i, \overline{e}i\\}, \\{e, \overline{e}, j, \overline{e}j\\}, \\{e, \overline{e}, k, \overline{e}k\\}, Q_8$ all of which are normal (easy to verify).
- The center $Z(G)$ of a group is always normal.
- The alternating group $A_n$ of even permutations is a normal subgroup of $S_n$.
- Every subgroup of $D_n$ consisting solely of rotations is normal in $D_n$. 
- Let $H$ be a normal subgroup of a group $G$ and $K$ be any subgroup of $G .$ Then $H K=\\{h k | h \in H, k \in K\\}$ is a subgroup of $G$.
- If a group $G$ has a unique subgroup $H$ of some finite
  order, then $H$ is normal in $G$. To see that this is so, observe that for any $g \in G, g H g^{-1}$ is a subgroup of $G$ and $|g H g^{-1}|=| H |$.
- Let $G$ be a finite group, $|G| = pm$ where $p$ is a prime and $p \not | m$ and $H \triangleleft G$ of order $p$. Show that for any autmorphism $\phi:G \rightarrow G, \phi(H) = H$ (easy, if $\phi(H) \neq H \rightarrow \because \phi(H) \cap H = \\{e\\}$ $, H\phi(H)$ is a subgroup of order $p^2 \Rightarrow \Leftarrow$)

## Factor Groups or Quotient Groups

---

**Theorem 9.2:** Let $G$ be a group and let $H$ be a normal subgroup of $G .$ The set
$G / H=\\{a H | a \in G\\}$ is a group under the operation $(a H)(b H)=a b H$ (easy to prove)

**Proof:** Group axioms are easy to verify but we must verify that the function is well defined, so we need to check whether single element gets map to exactly one element, so consider $a, a', b, b' \in G \text{ and } aH = a'H, bH = b'H$ to show $abH = a'b'H$ i.e. to show $ab \in a'b'H$, $a = a'h_1, b = b'h_2, ab = a'h_1b'h_2 = a'b'h_3h_2$

---

Converse of
Theorem 9.2 is also true; that is, if the correspondence $aHbH = abH$ defines a group operation on the set of left cosets of $H$ in $G$, then $H$ is
normal in $G$.

It is crucial to understand that when we factor out by a normal subgroup $H$, what we are essentially doing is defining every element in $H$ to be the identity.

Also remember that the order of the factor group is $|G|/|H|$

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
  
- It can be shown that every finite Abelian group is
  isomorphic to a direct product of cyclic groups. In particular, an
  Abelian group of order 8 is isomorphic to one of $Z_8, Z_4 \oplus Z_2, \text{ or } Z_2 \oplus Z_2 \oplus Z_2$ . In the next two examples, we examine Abelian factor groups
  of order 8 and determine the isomorphism type of each.

  - Let $G = U(32) = \\{1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31\\}$ and $H = U_{16}(32) = \\{1, 17\\}$. Then $G/H$ is an Abelian
    group of order $16/2 = 8$. Which of the three Abelian groups of order 8
    is it—$Z_8, Z_4 \oplus Z_2, Z_2 \oplus Z_2 \oplus Z_2$ ? To answer this question, we need
    only determine the elements of $G/H$ and their orders. Observe that the
    eight cosets
    $\begin{array}{ll}{1 H=\\{1,17\\},} & {3 H=\\{3,19\\},  5 H=\\{5,21\\},  7 H=\\{7,23\\}} \\\ {9 H=\\{9,25\\},} & {11 H=\\{11,27\\},  13 H=\\{13,29\\},}\end{array}$ and $15 H=\\{15,31\\}$

    are all distinct, so that they form the factor group $G / H .$ Clearly,
    $(3 H)^{2}=9 H \neq H,$ and $\operatorname{so} 3 H$ has order at least $4 .$ Thus, $G / H$ is not
    $Z_{2} \oplus Z_{2} \oplus Z_{2} .$ On the other hand, direct computations show that both 7$H$ and 9$H$ have order $2,$ so that $G / H$ cannot be $Z_{8}$ either, since a cyclic
    group of even order has exactly one element of order 2 (Theorem 4.4$)$ .
    This proves that $U(32) / U_{16}(32) \approx Z_{4} \oplus Z_{2},$ which (not so incidentally!) is isomorphic to $U(16)$.

  - Let $G=U(32)$ and $K=\\{1,15\\} .$ Then $|G / K|=8$ and we ask, which of the three Abelian groups of order 8 is $G/K$? Since $(3 K)^{4}=81 K=17 K \neq K,|3 K|=8 .$ Thus, $G / K \approx Z_{8}$

- If $H$ has index 2 in $G$, then $H$ is normal in $G$. **Proof:** Let $a \not\in H \rightarrow aH \neq H \text{ and } Ha \neq H$ but since we only have two cosets $\rightarrow aH = Ha$.

## Applications of Factor Groups

- The group $A_4$ of even permutations on the set $\\{1, 2, 3, 4\\}$ has no subgroup $H$ of order 6. To see this, suppose that $A_4$ does have a subgroup $H$ of order 6. By above example, we know that $H \triangleleft A_4$. Thus, the factor group $A_4 / H$ exists and has order 2. We have for all $\alpha \in A_4$ that $\alpha^2H = (\alpha H)^2 = H$. Thus, $\alpha^2 \in H$ for all $\alpha \in A_4$. Referring to the main diagonal of the group table for $A_4$ however, we observe that $A_4$ has nine different elements of the form $\alpha^2$, all of which must belong to $H$, a subgroup of order 6. This is clearly impossible, so a subgroup of order 6 cannot exist in $A_4$.

---

**Theorem 9.3:** Let $G$ be a group and let $Z(G)$ be the center of $G$. If $G/Z(G)$ is cyclic, then $G$ is Abelian.

**Proof:** Since $G$ is Abelian is equivalent to $Z(G) = G$, it suffices to show that the only element of $G/Z(G)$ is the identity coset $Z(G)$. To this end, let $G / Z(G)=\langle g Z(G)\rangle$ and let $a \in G .$ Then there exists an integer $i$ such that
$a Z(G)=(g Z(G))^{i}=g^{i} Z(G) .$ Thus, $a=g^{i} z$ for some $z$ in $Z(G)$ . Since both
$g^{i}$ and $z$ belong to $C(g),$ so does $a$ . Because $a$ is an arbitrary element of $G$ this means that every element of $G$ commutes with $g$ so $g \in Z(G)$. Thus, $gZ(G) = Z(G)$ is the only element of $G/Z(G)$.

---

A few remarks about Theorem 9.3 are in order. First, our proof shows
that a better result is possible: If $G/H$ is cyclic, where $H$ is a subgroup of
$Z(G)$, then $G$ is Abelian. Second, in practice, it is the contrapositive of
the theorem that is most often used—that is, if $G$ is non-Abelian, then
$G/Z(G)$ is not cyclic. For example, it follows immediately from this
statement and Lagrange’s Theorem that a non-Abelian group of order
$pq$, where $p$ and $q$ are primes, must have a trivial center (suppose center is not trivial, that implies its order is either $p \text{ or } q$. Say it is $p \rightarrow$ order of $G / Z(G) = q$ and hence it must be cyclic. Third, if $G/Z(G)$ is cyclic, it must be trivial.

---

**Theorem 9.4:** For any group $G$, $G/Z(G)$ is isomorphic to $Inn(G)$.

**Proof:**  Consider the correspondence from $G/Z(G)$ to $Inn(G)$ given by
$T : gZ(G) → \phi_g$. We can now easily show that it is well defined and as well satisfies properties for it being isomorphism. For one-one, note that $g_1xg_1^{-1} = g_2xg_2^{-1} \rightarrow (g_2^{-1}g_1)x = x(g_2^{-1}g_1)$ thus $g_1 = g_2z, z \in Z(G)$.

---

**Examples:**
- We know that $|Z(D_6)| = 2$. Thus, $|D_6 /Z (D_6)| = 6$. So, by our classification of groups of order 6 (Theorem 7.3), we know that $Inn(D_6)$ is isomorphic to $D_3$ or $Z_6$. Now, if $Inn(D_6)$ were cyclic, then, by Theorem 9.4, $D_6/Z(D_6)$ would be also. But then, Theorem 9.3 would tell us that $D_6$ is Abelian. So, $Inn(D_6)$ is isomorphic to $D_3$.

---

**Theorem 9.5: (Cauchy's Theorem for Abelian Groups)** Let $G$ be a finite Abelian group and let $p$ be a prime that divides the
order of $G$. Then $G$ has an element of order $p$.

**Proof:** Clearly, this statement is true for the case in which $G$ has
order 2. We prove the theorem by using the Second Principle of Mathematical Induction on $|G|$. That is, we assume that the statement is true
for all Abelian groups with fewer elements than $G$ and use this assumption to show that the statement is true for $G$ as well. Certainly, $G$ has
elements of prime order, for if $|x| = m$ and $m = qn$, where $q$ is prime,
then $|x^n| = q$. So let $x$ be an element of $G$ of some prime order $q$, say. If
$q = p$, we are finished; so assume that $q \neq p$. Since every subgroup of
an Abelian group is normal, we may construct the factor group $\overline{G} = G/< x >$. Then $\overline{G}$ is Abelian and $p$ divides $|\overline{G}|$, since $|\overline{G}| = |G|/q$. By
induction, then, $\overline{G}$ has an element—call it $y < x >$—of order $p$.
Then, $(y < x >)^p = y^p < x > = < x >$ and therefore $y^p \in < x >$. If $y^p = e$, we are
done. If not, then $y^p$ has order $q$ and $y^q$ has order $p$.

## Internal Direct Products

---

We say that $G$ is the internal direct product of $H$ and $K$ and write $G = H \times K$ if $H$ and $K$ are normal subgroups of $G$ and $G = HK$ and $H \cap K = \\{e\\}$.

---

---

Let $H_1, H_2, ..., H_n$ be a finite collection of normal subgroups of $G$. We say that $G$ is the internal direct product of $H_1, H_2, ..., H_n$ and write
$G = H_1 \times H_2 \times ... \times H_n$, if
1. $G=H_{1} H_{2} \cdots H_{n}=\left\\{h_{1} h_{2} \cdots h_{n} | h_{i} \in H_{i}\right\\}$
2. $\left(H_{1} H_{2} \cdots H_{i}\right) \cap H_{i+1}=\\{e\\}$ for $i=1,2, \ldots, n-1$ 

---
 
:::note Note
Condition 2 above will guarantee for $i \neq j, H_i \cap H_j = \\{e\\}$ as wlog assume $j > i$ then by making other $h_k$ as $e$ we get using ($H_1H_2\cdots H_i \cdots H_{j - 1}) \cap H_j = \\{e\\}, H_i \cap H_j = \\{e\\}$
:::

---

**Theorem 9.6:** $H_{1} \times H_{2} \times \cdots \times H_{n} \approx H_{1} \oplus H_{2} \oplus \cdots \oplus H_{n}$

**Proof:** We first show that the normality of the $H$’s together with the
second condition of the definition guarantees that $h$’s from different
$H_i$’s commute. We have $h_ih_j = h_jh_i' = h_j'h_i \rightarrow h_j'^{-1}h_j = h_ih_i'^{-1}$ $\rightarrow h_j'^{-1}h_j = e \rightarrow h_j = h_j'...$

Similarly we can easily prove that each member of $G$ can be expressed
uniquely in the form $h_1h_2 \cdots h_n$, where $h_i \in H_i$. 

We may now define a function $\phi$ from $G$ to $H_1 \oplus H_2 \oplus \cdots \oplus H_n$ by $f(h_1h_2 \cdots h_n ) = (h_1, h_2, ..., h_n)$. Which is easily verifiable to be an isomorphism.

---

---

**Theorem 9.7:** Every group of order $p^{2},$ where $p$ is a prime, is isomorphic to $Z_{p^{2}}$ or
$Z_{p} \oplus Z_{p}$

**Proof:** Let $G$ be a group of order $p^2$, where $p$ is a prime. If $G$ has an
element of order $p^2$, then $G$ is isomorphic to $Z_{p^2}$. So, by Corollary 2 of
Lagrange’s Theorem, we may assume that every nonidentity element of
$G$ has order $p$. First we show that for any element $a$, the subgroup $< a >$ is
normal in $G$. If this is not the case, then there is an element $b$ in $G$ such
that $bab^{-1}$ is not in $< a >$. Then $< a >$ and $<bab^{-1}>$ are distinct subgroups of order $p$. Since $< a > \cap < bab^{-1}>$ is a subgroup of both $< a >$ and $<bab^{-1}>$, we have that $< a > \cap < bab^{-1}> = \\{e\\}$. From this it follows that the distinct
left cosets of $< bab^{-1} >$ are $< bab^{-1} >, a< bab^{-1} >, a^2< bab^{-1} >, \dots, a^{p - 1}< bab^{-1} >$ (as if $a^i \in a^j\langle bab^{-1} \rangle \rightarrow a^{i - j} \in \langle bab^{-1} \rangle$). Since $b^{-1}$ must lie in one of these cosets, we may write
$b^{-1}$ in the form $b^{-1} = a^i (bab^{-1})^j = a^iba^jb^{-1}$ for some $i$ and $j$. Canceling the $b^{-1}$ terms, we obtain $e = a^iba^j$ and therefore $b = a^{-i-j} \in < a >$.
This contradiction verifies our assertion that every subgroup of the form
$< a >$ is normal in $G$. To complete the proof, let $x$ be any nonidentity element in $G$ and $y$ be any element of $G$ not in $< x >$. Then, by comparing orders and using Theorem 9.6, we see that $G = < x > \times < y > \approx Z_p \oplus Z_p$.

---

**Corollary:** If $G$ is a group of order $p^2$, where $p$ is a prime, then $G$ is Abelian.

*Note:* Indian authors seems to switch the notation for EDP and IDP.

It follows directly from Theorem 8.3, its corollary, and
Theorem 9.6 that if $m = n_1n_2 \cdots n_k$, where $gcd(n_i, n_j) = 1$ for $i \neq j$, then

$U(m) = U_{m/n_1}(m) \times U_{m/n_2}(m) \times \cdots  U_{m/n_k}(m)$

$\approx U(n_1) \oplus U(n_2) \oplus \cdots \oplus U(n_k)$.

:::note Note
$U_{m/n_i}(m) \cap U_{m/n_j}(m) = \\{e\\} \\;\forall i \neq j$ as $x = mk/n_1 + 1 = mk'/n_2 + 1 \rightarrow n_1k' = n_2k \rightarrow k' = n_2, k = n_1$ $\rightarrow x = m + 1$ which is absurd.
:::

