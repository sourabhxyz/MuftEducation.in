---
id: homo
title: Group Homomorphisms
sidebar_label: Group Homomorphisms
---

When defining a homomorphism from a group in which there are
several ways to represent the elements, caution must be exercised to
ensure that the correspondence is a function.

## Kernal of a Homomorphism

The kernel of a homomorphism $\phi$ from a group $G$ to a group with
identity $e$ is the set $\\{x \in G \mid \phi(x) = e\\}$. The kernel of $\phi$ is denoted by $\operatorname{Ker} \phi$ and clearly it forms a subgroup.

The kernel of an isomorphism is the trivial subgroup.

Relation with linear algebra: Every linear transformation is a group homomorphism and the null-space is the same as the kernel. An invertible linear transformation is a group isomorphism.

## Properties of Homomorphisms

**Theorem 10.1:** Let $\phi$ be a homomorphism from a group $G$ to a group $\overline{G}$ and let $g$ be an element of $G$ and let $H$ be a subgroup of $G$. Then
1. $\phi$ carries the identity of $G$ to the identity of $\overline{G}$.
2. $\phi(g^n) = (\phi(g))^n$ for all $n$ in $Z$.
3. If $|g|$ is finite, then $|\phi(g)|$ divides $|g|$. (easy)
4. $\phi(a) = \phi(b)$ if and only if $a\operatorname{Ker} \phi = b\operatorname{Ker} \phi$. (easy)
5. If $\phi(g) = g'$, then $\phi^{-1}(g') = \\{x \in G \mid \phi(x) = g'\\} = g\operatorname{Ker} \phi$. (easy, $g\operatorname{Ker} \subseteq \phi^{-1}(g')$ is straight forward, for other dirn, we have, $\phi(x) = \phi(g') \rightarrow g'^{-1}x \in \operatorname{Ker} \phi$)
6. $\phi(H) = \\{\phi(h) \mid h \in H\\}$ is a subgroup of $\overline{G}$. (easy)
7. If $H$ is cyclic, then $\phi(H)$ is cyclic. (easy)
8. If $H$ is Abelian, then $\phi(H)$ is Abelian. (easy)
9. If $H$ is normal in $G$, then $\phi(H)$ is normal in $\phi(G)$. (easy)

