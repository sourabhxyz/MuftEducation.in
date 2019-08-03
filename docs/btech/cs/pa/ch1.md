---
id: ch1
title: Chapter 1
sidebar_label: Chapter 1
---

## Evaluation Scheme 

* Q1, Q2 - 20%
* Assignments - 15%
* Endsem - 45%
  
## Complexity Class $P$

* $P$ is the set of all decision problems solvable in polynomial time 
* $O(n^c)$ time for some constant c where n is the input size

## Complexity Class $EXP$

* $EXP$ is the set of all decision problems solvable in exponential time 
* $O(2^{n^c})$ time for some constant c where n is the input size 


A kernelization algorithm, or simply a kernel, for a parameterized problem $Q$ is an algorithm $\mathcal{A}$ that, given an instance $(I, k)$ of $Q,$ works in polynomial time and returns an equivalent
instance $\left(I^{\prime}, k^{\prime}\right)$ of $Q .$ Moreover, we require that size $_{\mathcal{A}}(k) \leq g(k)$ for some
computable function $g : \mathbb{N} \rightarrow \mathbb{N}$ .

Note: $\operatorname{size}_{\mathcal{A}}(k)=\sup \left\\{\left|I^{\prime}\right|+k^{\prime} :\left(I^{\prime}, k^{\prime}\right)=\mathcal{A}(I, k), I \in \Sigma^{*}\right\\}$

Lemma: If a parameterized problem $Q$ is FPT then it admits a kernelization algorithm.

Proof. since $Q$ is $\mathrm{FPT}$ , there is an algorithm $\mathcal{A}$ deciding if $(I, k) \in Q$ in time
$f(k) \cdot|I|^{c}$ for some computable function $f$ and a constant $c .$ We obtain a ker-
nelization algorithm for $Q$ as follows. Given an input $(I, k),$ the kernelization
algorithm runs $\mathcal{A}$ on $(I, k),$ for at most $|I|^{c+1}$ steps. If it terminates with an answer, use that answer to return either that $(I, k)$ is a yes-instance or that
it is a no-instance. If $\mathcal{A}$ does not terminate within $|I|^{c+1}$ steps, then return
$(I, k)$ itself as the output of the kernelization algorithm. Observe that since
$\mathcal{A}$ did not terminate in $|I|^{c+1}$ steps, we have that $f(k) \cdot|I|^{c}>|I|^{c+1},$ and thus $|I|<f(k) .$ Consequently, we have $|I|+k \leq f(k)+k,$ and we obtain a
kernel of size at most $f(k)+k ;$ note that this upper bound is computable as $f(k)$ is a computable function.
