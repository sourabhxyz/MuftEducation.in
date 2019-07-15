---
id: vector_spaces
title: Vector Spaces
sidebar_label: Vector Spaces
---

## Field

Field is a set $F$ together with two operations called addition and multiplication. An operation is a mapping that associates an element of the set to every pair of its elements. The result of the addition of $a$ and $b$ is called the sum of $a$ and $b$ and denoted $a + b$. Similarly, the result of the multiplication of $a$ and $b$ is called the product of $a$ and $b$, and denoted $ab$ or $a⋅b$. These operations are required to satisfy the following properties, referred to as field axioms. In these axioms, $a$, $b$ and $c$ are arbitrary elements of the field $F$.

1. Associativity of addition and multiplication: $a + (b + c) = (a + b) + c$ and $a · (b · c) = (a · b) · c$.
2. Commutativity of addition and multiplication: $a + b = b + a$ and $a · b = b · a$.
3. Additive and multiplicative identity: there exist two different elements $0$ and $1$ in $F$ such that $a + 0 = a$ and $a · 1 = a$.
4. Additive inverses: for every $a$ in $F$, there exists an element in $F$, denoted $−a$, called the additive inverse of $a$, such that $a + (−a) = 0$.
5. Multiplicative inverses: for every $a ≠ 0$ in $F$, there exists an element in $F$, denoted by $a^{−1}, 1/a$, or $\frac{1}{a}$, called the multiplicative inverse of $a$, such that $a · a^{−1} = 1$.
6. Distributivity of multiplication over addition: $a · (b + c) = (a · b) + (a · c)$.

This may be summarized by saying: a field has two operations, called addition and multiplication; it is an abelian group under the addition, with $0$ as additive identity; the nonzero elements are an abelian group under the multiplication, with $1$ as multiplicative identity; the multiplication is distributive over the addition.

## Vector Spaces

A set $V$ is said to be a vector space over a field $F$ if $V$ is an Abelian group under addition (denoted by $+$) and, if for each $a \in F$ and
$v \in V$, there is an element $av$ in $V$ such that the following conditions hold for all $a, b$ in $F$ and all $u, v$ in $V$.

1. $a(v+u)=av+au$
2. $(a+b)v=av+bv$
3. $a(bv) = (ab)v$
4. $1v=v$

$V$ has dimension $n$, or is $n$-dimensional, if it contains a linearly independent set of $n$ vectors, whereas any set of more than $n$ vectors in $V$ is linearly dependent. That set of $n$ linearly independent vectors is called a basis for $V$. Then every vector in $V$ can be written as a linear combination of the basis vectors. Furthermore, for a given basis, this representation is unique.

---

**Example:** The real $2 \cdot 2$ matrices form a four-dimensional real vector space. A basis is

$B_{11} = \begin{bmatrix}1 & 0\\\ 0 & 0\end{bmatrix},$
$B_{12} = \begin{bmatrix}0 & 1\\\ 0 & 0\end{bmatrix},$
$B_{21} = \begin{bmatrix}0 & 0\\\ 1 & 0\end{bmatrix},$
$B_{22} = \begin{bmatrix}0 & 0\\\ 0 & 1\end{bmatrix}$

Similarly, the real $m \cdot n$ matrices with fixed $m$ and $n$ form an $mn$-dimensional vector space.

---

**Example:** The set of all constant, linear, and quadratic polynomials in $x$ together is a vector space of dimension 3 with basis ${1, x, x^2}$ under the usual addition and multiplication by real numbers.

---

If a vector space $V$ contains a linearly independent set of n vectors for every $n$, no matter how large, then $V$ is called infinite dimensional, as opposed to a finite dimensional ($n$-dimensional) vector space just defined. An example of an infinite dimensional vector space is the space of all continuous functions on some interval $[a, b]$ of the $x$-axis, as we mention without proof.

## Inner Product Spaces

If $a$ and $b$ are vectors in $R^n$, regarded as column vectors, we can form the product $a^Tb$. This is a $1 \times 1$ matrix, which we can identify with its single entry, that is, with a number, called **inner product** or **dot product**) also denoted as $(a, b)$ or $a \cdot b$. $R^n$ with this inner product space is called $n$-dimensional Euclidean space and is denoted by $E^n$ or simply by $R^n$.

We now extend this concept to general real vector spaces.

---

**Definition: Real Inner Product Space**

A real vector space $V$ is called a real inner product space (or real pre-Hilbert space) if it has the following property. With every pair of vectors $a$ and $b$ in $V$ there is associated a real number, which is denoted by $(a, b)$ and is called the inner product of $a$ and $b$, such that the following axioms are satisfied.

1. (Linearity) For all scalars $q_1$ and $q_2$ and all vectors $a, b, c$ in $V$,$(q_1a + q_2b, c) = q_1(a, c) + q_2(b, c)$.
2. (Symmetry) For all vectors $a$ and $b$ in $V$, $(a, b) = (b, a)$.
3. (Positive-definiteness) For every $a$ in $V$, $(a, a) \geq 0$, $(a, a) = 0$ and $a = \textbf{0}$

---

Vectors whose inner product is zero are called orthogonal.

The length or norm of a vector $V$ is defined by $||a|| = \sqrt{(a, a)}$

A vector of unit norm is called unit vector.

From these axioms one can derive (omitted for now) the basic inequality

- $|(a,b)| \leq ||a||||b||$ (Cauchy–Schwarz inequality). From this follows

- $||a + b|| \leq ||a|| + ||b||$ (Triangle inequality) (just square both sides and you will arive at above ineq.)

  A simple direct calculation gives

- $||a + b||^2 + ||a - b||^2 = 2(||a||^2 + ||b||^2)$ (Parallelogram equality).

## Linear Transformations

---

Let $X$ and $Y$ be any vector spaces. To each vector $x$ in $X$ we assign a unique vector $y$ in $Y$. Then we say that a mapping (or transformation or operator) of $X$ into $Y$ is given. Such a mapping is denoted by a capital letter, say $F$. The vector $y$ in $Y$ assigned to a vector $x$ in $X$ is called the image of $x$ under $F$ and is denoted by $F(x)$ [or $Fx$, without parentheses].

$F$ is called a **linear mapping** or **linear transformation** if, for all vectors $v$ and $x$ in$X$ and scalars $c$,
$F(v + x) = F(v) + F(x) \text{ and } F(cx) = cF(x)$.

---
