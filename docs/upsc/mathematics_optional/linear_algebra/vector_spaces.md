---
id: vector_spaces
title: Vector Spaces
sidebar_label: Vector Spaces
---

## Vector Spaces

---

**Real vector space:** A nonempty set $V$ of elements $a, b, \dots$ is called a real vector space (or real linear space), and these elements are called vectors, if, in $V$, there are defined two algebraic operations (called vector addition and scalar multiplication) as follows.

1. Vector addition associates with every pair of vectors $a$ and $b$ of $V$ a unique vector **of** $V$, called the sum of $a$ and $b$ and denoted by $a + b$, such that the following axioms are satisfied.

   1. Commutativity. For any two vectors $a$ and $b$ of $V$, $a + b = b + a$.
   2. Associativity. For any three vectors $a, b, c$ of $V$, $(a + b) + c = a + (b + c)$ (written $a + b + c)$.
   3. There is a unique vector in $V$, called the zero vector and denoted by $0$, such that for every $a$ in $V$, $a + 0 = a$.
   4. For every $a$ in $V$ there is a unique vector in $V$ that is denoted by $-a$ and is such that $a + (-a) = 0$.

2. Scalar multiplication. The real numbers are called scalars. Scalar multiplication associates with every $a$ in $V$ and every scalar $c$ a unique vector of $V$, called the product of $c$ and $a$ and denoted by $ca$ (or $ac$) such that the following axioms are satisfied.

   1. Distributivity. For every scalar $c$ and vectors $a$ and $b$ in $V$, $c(a + b) = ca + cb$.
   2. Distributivity. For all scalars $c$ and $k$ and every $a$ in $V$, $(c + k)a = ca + ka$.
   3. Associativity. For all scalars $c$ and $k$ and every $a$ in $V$, $c(ka) = (ck)a$ (written $cka$).
   4. For every $a$ in $V$, $1a = a$.

---

If, in the above definition, we take complex numbers as scalars instead of real numbers, we obtain the axiomatic definition of a **complex vector space**.

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
