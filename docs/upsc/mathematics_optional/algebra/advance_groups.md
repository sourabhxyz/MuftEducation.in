---
id: advance_groups
title: Advanced Group Theory Results
sidebar_label: Advanced Group Theory Results
---

## Chinese Remainder Theorem

Given $a_1, a_2, \dots, a_n, b_1, b_2, \dots, b_n \in \mathbb{Z}$ and $gcd(a_i, a_j) = 1 \forall i \neq j$. Find $a$ s.t. $a = b_i \bmod a_i$

**Solution:** 

Define $p_i = \prod_{j \neq i} a_j$

then $p_i \begin{cases} \equiv 0 (\bmod a_j) \text{ if } j \neq i \\\ \not \equiv 0 (\bmod a_i)\end{cases}$

We have,

$(\prod_{j \neq i} a_j) \bmod a_i \in U(a_i)$ (as they are relatively prime) $\rightarrow \exists c_i \text{ s.t. } c_i(\prod_{j \neq i}a_j) \equiv 1 \bmod a_i$

$\rightarrow a = \sum b_i (c_i \prod_{j \neq i}a_j)$

Mentioning without proof that such a solution is unique modulo $\prod a_j$

## Theorem AG.1:

$U(m)$ is cyclic precisely if $m \in \\{2, 4, p^r, 2p^r\\}, \text{ where } p \neq 2$ and is prime. 

**Proof:** 

Case 1: $m = 2^r; r > 2$

Let $\lambda = 2^{r - 1} - 1, \beta = 2^r - 1$

$\lambda^2 = 2^{2r - 2} + 1 - 2^r = 1$

And

$\beta^2 = 2^{2r} + 1 - 2^{r + 1} = 1$

Thus $U(m)$ is not cyclic. 

Case 2: $m = p_1^{a_1}p_2^{a_2} \cdots p_r^{a_r}, r > 1$ 

Define $\lambda_i \begin{cases} \equiv p_i^{a_i} - 1 \bmod p_i^{a_i} \\\ \equiv 1 \bmod p_j^{a_j} \text{ and } (j \neq i) \end{cases}$

Note that if $p_i = 2$ and $a_1 = 1$ then both equivalence will become same and hence following arguments will not be valid.

Which we can easily find using [CRT](#chinese-remainder-theorem).

Now, $\lambda_i^2 \equiv 1 \bmod p_j^{a_j}$ $\rightarrow \lambda_i^2 \equiv 1 \bmod m \forall i$ $\rightarrow \lambda_i^2 - 1$ is divisible by $m$.

$\\{\overline{\lambda_1}, \dots, \overline{\lambda_r}\\} \subset U(m)$ where $\overline{\lambda_i} = \lambda_i \bmod m$ and is such that $\overline{\lambda_i} \neq \overline{\lambda_j}$ and $\overline{\lambda_i}^2 \equiv \overline{\lambda_j}^2 \equiv 1 \bmod m$

Therefore $U(m)$ is not cyclic.

## Group Action

If $G$ is a group and $S$ is a set of objects, we say that $G$ acts on $S$ if there is a homomorphism $\psi$ from $G$ to $sym(S)$ (or also denoted as $A(S)$), the group of all permutations on $S$.

**Examples:**

- Let $S$ be a finite set of $n$ elements, choose an enumeration of $S = \\{s_1, s_2, \dots, s_n\\}$ then we get an action of $S_n$ on $S$, $\psi : S_n \rightarrow A(S), \psi(\sigma)(s_i) = s_{\sigma(i)}$.

## Problems

- Let $H$ be a subgroup of $G$. Define $L : G \rightarrow A(G / H), L(g)(aH) = gaH$. Clearly this is an homomorphism. What is $\operatorname{Ker}(L)$? 

  **Sol:** $gaH = aH \rightarrow$ $ga \in aH \rightarrow g \in aHa^{-1}$. So answer is intersection fo all conjugates, i.e. $\operatorname{Ker}(L) = \cap_{a \in G}aHa^{-1}$.

- $G$ is a finite group, $H \subset G$ is a subgroup. Assume $|G| \not | i_G(H)!$. Show that $\exists$ a normal subgroup $N \triangleleft H$ and $N \neq \\{e\\}$.

  **Sol:** Consider the homomorphism of above example, $L : G \rightarrow A(G / H) \approx S_{\frac{|G|}{|H|}}$, now since $n \not | \\; |A(G/H)|$ therefore $L$ cannot be injective and hence $\operatorname{Ker}(L) \neq \\{e\\}$, which is our required normal subgroup.

- Prove that a group of order $p^2$ (where $p$ is prime) has a normal subgroup of order $p$.
  
  **Sol:** Let $H \subset G$ be any subgroup of order $p$. Since $p^2 \not | p!$, $\therefore \operatorname{Ker}(L) \neq \\{e\\}$ and since $\operatorname{Ker}(L) \subseteq H$ but as $|H| = p \rightarrow \operatorname{Ker}(L) = H$, $\therefore H$ is normal in $G$.

- If $G$ is a non abelian group of order 6 then show that $G \approx S_3$.

