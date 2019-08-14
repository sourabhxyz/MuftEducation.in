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





