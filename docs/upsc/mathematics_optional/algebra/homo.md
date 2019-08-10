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
identity $e$ is the set $\\{x \in G \mid \phi(x) = e\\}$. The kernel of $\phi$ is denoted by $\operatorname{Ker} \phi$.

The kernel of an isomorphism is the trivial subgroup.

Relation with linear algebra: Every linear transformation is a group homomorphism and the null-space is the same as the kernel. An invertible linear transformation is a group isomorphism.

## Properties of Homomorphisms

**Theorem 10.1:** Let $\phi$ be a homomorphism from a group $G$ to a group $G$ and let $g$ be an element of $G$. Then
1. $\phi$ carries the identity of $G$ to the identity of $G$.
2. $\phi(g^n) = (\phi(g))^n$ for all $n$ in $Z$.
3. If $|g|$ is finite, then $|\phi(g)|$ divides $|g|$. (easy)
4. $\operatorname{Ker} \phi$ is a subgroup of $G$.
5. $\phi(a) = \phi(b)$ if and only if $a\operatorname{Ker} \phi = b\operatorname{Ker} \phi$.
6. If $\phi(g) = g'$, then $\phi^{-1}(g') = \\{x \in G \mid \phi(x) = g'} = g\operatorname{Ker} \phi$.


