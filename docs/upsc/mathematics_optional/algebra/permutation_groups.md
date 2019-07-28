---
id: permutation_groups
title: Permutation Groups
sidebar_label: Permutation Groups
---

---
A permutation of a set $A$ is a function from $A$ to $A$ that is both one-
to-one and onto. A permutation group of a set $A$ is a set of permuta-
tions of $A$ that forms a group under function composition.

---

Although groups of permutations of any nonempty set $A$ of objects
exist, we will focus on the case where $A$ is finite. Furthermore, it is
customary, as well as convenient, to take $A$ to be a set of the form
$\\{1, 2, 3, . . . , n\\}$.

## Array form

$\beta$ of the set $\{1,2,3,4,5,6\}$ given by $\beta(1)=5, \quad \beta(2)=3, \quad \beta(3)=1, \quad \beta(4)=6, \quad \beta(5)=2, \quad \beta(6)=4$ is expressed in array form as

$\beta=\left[\begin{array}{llllll}{1} & {2} & {3} & {4} & {5} & {6} \\\ {5} & {3} & {1} & {6} & {2} & {4}\end{array}\right]$

### Composition

Consider 

$\sigma=\left[\begin{array}{lllll}{1} & {2} & {3} & {4} & {5} \\\ {2} & {4} & {3} & {5} & {1}\end{array}\right]$,
$\gamma=\left[\begin{array}{lllll}{1} & {2} & {3} & {4} & {5} \\\ {5} & {4} & {1} & {2} & {3}\end{array}\right]$

$\gamma \sigma=$
$\left[\begin{array}{cccc}{1} & {2} & {3} & {4} & {5} \\\ {} & {\downarrow} & {} & {} \\\ {5} & {4} & {1} & {2} & {3}\end{array}\right]$
$\left[\begin{array}{llll}{1} & {2} & {3} & {4} & {5} \\\ {\downarrow} & {} & {} & {} & {} \\\ {2} & {4} & {3} & {5} & {1}\end{array}\right]$

$=\left[\begin{array}{lllll}{1} & {2} & {3} & {4} & {5} \\\ {4} & {2} & {1} & {3} & {5}\end{array}\right]$

**Examples:** 

- Symmetric Group $S_{n}$: Let $A=\\{1,2, \ldots, n\\} .$ The set
  of all permutations of $A$ is called the symmetric group of degree $n$ and is
  denoted by $S_{n}$ . Elements of $S_{n}$ have the form

  $\alpha=\left[\begin{array}{cccc}{1} & {2} & {\ldots} & {n} \\\ {\alpha(1)} & {\alpha(2)} & {\dots} & {\alpha(n)}\end{array}\right]$

  It is easy to compute the order of $S_{n} .$ There are $n$ choices of $\alpha(1)$ . Once
  $\alpha(1)$ has been determined, there are $n-1$ possibilities for $\alpha(2)$ [since
  $\alpha$ is one-to-one, we must have $\alpha(1) \neq \alpha(2) ] .$ After choosing $\alpha(2),$ there
  are exactly $n-2$ possibilities for $\alpha(3)$ . Continuing along in this fashion,
  we see that $S_{n} \operatorname{has} n(n-1) \cdot \cdot 3 \cdot 2 \cdot 1=n !$ elements.

## Cycle Notation

Consider,

$\beta=\left[\begin{array}{llllll}{1} & {2} & {3} & {4} & {5} & {6} \\\ {5} & {3} & {1} & {6} & {2} & {4}\end{array}\right]$

In cycle notation, $\beta$ can be written $(2,3,1,5)(6,4)$ or $(4,6)(3,1,5,2),$
since both of these unambiguously specify the function $\beta .$ An expres-
sion of the form $\left(a_{1}, a_{2}, \ldots, a_{m}\right)$ is called a cycle of length $m$ or an
$m-c y c l e .$

A multiplication of cycles can be introduced by thinking of a cycle
as a permutation that fixes any symbol not appearing in the cycle.
Thus, the cycle (4, 6) can be thought of as representing the permutation $\left[\begin{array}{llllll}{1} & {2} & {3} & {4} & {5} & {6} \\\ {1} & {2} & {3} & {6} & {5} & {4}\end{array}\right]$.

Let $\alpha = (13)(27)(456)(8)$ and $\beta = (1237)(648)(5)$. (When the domain consists of single-digit integers, it is common practice to omit the commas between the digits.) $\alpha \beta = ?$

Well, keeping in mind that function composition is done from right to left and that each cycle that does not contain a symbol fixes the symbol, we observe that (5) fixes 1; (648) fixes 1; (1237) sends 1 to 2; (8) fixes 2; (456) fixes 2; (27) sends 2 to 7; and (13) fixes 7. So the net effect of $\alpha \beta$ is to send 1 to 7. Thus, we begin $\alpha \beta = (17 ? ? ?) ? ? ?$ . Now, repeating the entire process beginning with 7, and so on, we have $\alpha \beta=(1732)(48)(56)$

Mathematicians prefer not to
write cycles that have only one entry. In this case, it is understood that any
missing element is mapped to itself. Of course, the identity permutation consists
only of cycles with one entry, so we cannot omit all of these! In this
case, one usually writes just one cycle. For example,
$\varepsilon=\left[\begin{array}{lllll}{1} & {2} & {3} & {4} & {5} \\\ {1} & {2} & {3} & {4} & {5}\end{array}\right]$
can be written as $\varepsilon=(5)$ or $\varepsilon=(1)$

---

**Theorem 5.1:** Every permutation of a finite set can be written as a cycle or as a product of disjoint cycles. (Just give algorithm to find such disjoint cycles)

---

---

**Theorem 5.2:** If the pair of cycles $\alpha=\left(a_{1}, a_{2}, \ldots, a_{m}\right)$ and $\beta=\left(b_{1}, b_{2}, \ldots, b_{n}\right)$
have no entries in common, then $\alpha \beta=\beta \alpha .$ (easy to prove)

---

---

**Theorem 5.3:** The order of a permutation of a finite set written in disjoint cycle
form is the least common multiple of the lengths of the cycles.

**Proof:** First, observe that a cycle of length $n$ has order $n .$ . (easy to see) Next, suppose that $\alpha$ and $\beta$ are disjoint cycles of lengths $m$
and $n,$ and let $k$ be the least common multiple of $m$ and $n .$ It follows from
Theorem 4.1 that both $\alpha^{k}$ and $\beta^{k}$ are the identity permutation $\varepsilon$ and, since
$\alpha$ and $\beta$ commute, $(\alpha \beta)^{k}=\alpha^{k} \beta^{k}$ is also the identity. Thus, we know by Corollary 2 to Theorem 4.1$\left(a^{k}=e \text { implies that }|a| \text { divides } k\right)$ that the
order of $\alpha \beta-$ let us call it $t$ -must divide $k .$ But then $(\alpha \beta)^{t}=\alpha^{t} \beta^{t}=\varepsilon$
so that $\alpha^{t}=\beta^{-t} .$ However, it is clear that if $\alpha$ and $\beta$ have no common
symbol, the same is true for $\alpha^{t}$ and $\beta^{-t},$ since raising a cycle to a power
does not introduce new symbols. But, if $\alpha^{t}$ and $\beta^{-t}$ are equal and have
no common symbol, they must both be the identity, because every symbol in $\alpha^{t}$ is fixed by $\beta^{-t}$ and vice versa (remember that a symbol not ap-
pearing in a permutation is fixed by the permutation). It follows, then,
that both $m$ and $n$ must divide $t$ . This means that $k$ , the least common
multiple of $m$ and $n$ , divides $t$ also. This shows that $k=t$ . 

Thus far, we have proved that the theorem is true in the cases
where the permutation is a single cycle or a product of two disjoint
cycles. The general case involving more than two cycles can be handled in an analogous way.

---

**Examples:** 

- To determine the orders of the 7! = 5040 elements of $S_{7},$ we need only consider the possible disjoint cycle structures of the
  elements of $S_{7} .$ For convenience, we denote an $n$ -cycle by $(n) .$ Then, arranging all possible disjoint cycle structures of elements of $S_{7}$
  according to longest cycle lengths left to right, we have

  $(\underline{7})$

  $(\underline{6})(\underline{1})$

  $(\underline{5})(\underline{2})$

  $(\underline{5})(\underline{1})(\underline{1})$

  $(\underline{4})(\underline{3})$

  $(\underline{4})(\underline{2})(\underline{1})$

  $(\underline{4})(\underline{1})(\underline{1})(\underline{1})$

  $(\underline{3})(\underline{3})(\underline{1})$

  $(\underline{3})(\underline{2})(\underline{2})$

  $(\underline{3})(\underline{2})(\underline{1})(\underline{1})$

  $(\underline{3})(\underline{1})(\underline{1})(\underline{1})(\underline{1})$

  $(\underline{2})(\underline{2})(\underline{2})(\underline{1})$

  $(\underline{2})(\underline{2})(\underline{1})(\underline{1})(\underline{1})$

  $(\underline{2})(\underline{1})(\underline{1})(\underline{1})(\underline{1})(\underline{1})$
  
  $(\underline{1})(\underline{1})(\underline{1})(\underline{1})(\underline{1})(\underline{1})(\underline{1})$

  Now, from Theorem 5.3 we see that the orders of the elements of $S_7$
  are 7, 6, 10, 5, 12, 4, 3, 2, and 1.

- We determine the number of elements of $S_{7}$ of order 3. By Theorem $5.3,$ we need only count the number of permutations of
  the forms $\left(a_{1} a_{2} a_{3}\right)$ and $\left(a_{1} a_{2} a_{3}\right)\left(a_{4} a_{5} a_{6}\right) .$ In the first case consider the
  triple $a_{1} a_{2} a_{3} .$ Clearly there are 7$\cdot 6 \cdot 5$ such triples. But this product counts the permutation $\left(a_{1} a_{2} a_{3}\right)$ three times (for example, it counts $134,$
  $341,413$ as distinct triples whereas the cycles $(134),(341),$ and $(413)$
  are the same group element). Thus, the number of permutations in $S_{7}$ for the form $\left(a_{1} a_{2} a_{3}\right)$ is $(7 \cdot 6 \cdot 5) / 3=70$ . For elements of $S_{7}$ of the form
  $\left(a_{1} a_{2} a_{3}\right)\left(a_{4} a_{5} a_{6}\right)$ there are $(7 \cdot 6 \cdot 5) / 3$ ways to create the first cycle and
  $(4 \cdot 3 \cdot 2) / 3$ to create the second cycle but the product of $(7 \cdot 6 \cdot 5) / 3$ and $(4 \cdot 3 \cdot 2) / 3$ to create the second cycle but the product of $(7 \cdot 6 \cdot 5) / 3$ and
  $(4 \cdot 3 \cdot 2) / 3$ counts $\left(a_{1} a_{2} a_{3}\right)\left(a_{4} a_{5} a_{6}\right)$ and $\left(a_{4} a_{5} a_{6}\right)\left(a_{3} a_{2} a_{1}\right)$ as distinct when
  they are equal group elements. Thus, the number of elements in $S_{7}$ for the
  form $\left(a_{1} a_{2} a_{3}\right)\left(a_{4} a_{5} a_{6}\right)$ is $(7 \cdot 6 \cdot 5)(4 \cdot 3 \cdot 2) /(3 \cdot 3 \cdot 2)=280 .$ This gives us 350 elements of order 3 in $S_{7}$.

---

**Theorem 5.4:** Every permutation in $S_{n}, n>1,$ is a product of 2 -cycles.

**Proof:** First, note that the identity can be expressed as (12)(12), and so it is a product of 2-cycles. By Theorem 5.1, we know that every permutation can be written in the form $\left(a_{1} a_{2} \cdots a_{k}\right)\left(b_{1} b_{2} \cdots b_{t}\right) \cdots\left(c_{1} c_{2} \cdots c_{s}\right)$ A direct computation shows that this is the same as

$\left(a_{1} a_{k}\right)\left(a_{1} a_{k-1}\right) \cdots\left(a_{1} a_{2}\right)\left(b_{1} b_{t}\right)\left(b_{1} b_{t-1}\right) \cdots\left(b_{1} b_{2}\right)$

$\cdots\left(c_{1} c_{s}\right)\left(c_{1} c_{s-1}\right) \cdot \cdot \cdot\left(c_{1} c_{2}\right)$

This completes the proof.

---