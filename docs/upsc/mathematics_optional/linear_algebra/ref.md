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
