---
id: vector_spaces
title: Vector Spaces
sidebar_label: Vector Spaces
---

## Field

Field has two operations, called addition and multiplication; it is an abelian group under the addition, with $0$ as additive identity; the nonzero elements are an abelian group under the multiplication, with $1$ as multiplicative identity; the multiplication is distributive over the addition.

## Subfield

Let $F$ be field and $K \subseteq F$. If $K$ is a field wrt same binary operations in $F$ then $K$ is called subfield of $F$.

Example:

- $I$ is not a subfield of $Q$
- $R$ is a subfield of $C$

## Internal Composition

Let $A$ be any set. If $a * b \in A \forall a, b \in A$ then $*$ is said to be internal composition on $A$

## External Composition

Let $V$ and $F$ be any two sets. If $a \circ v \in V \forall a \in F, v \in V$ then $\circ$ is said to be an external composition in $V$ over $F$.

## Vector Spaces

A set $V$ is said to be a vector space over a field $F$ (denoted as $V(F)$) if $V$ is an Abelian group under addition (denoted by $+$) and, if for each $a \in F$ and
$v \in V$, there is an element $av$ in $V$ such that the following conditions hold for all $a, b$ in $F$ and all $u, v$ in $V\$.

1. $a(v+u)=av+au$
2. $(a+b)v=av+bv$
3. $a(bv) = (ab)v$
4. $1v=v$

- Thus, an internal composition in $V$ is called vector addition and external composition in $V$ over the field $F$ is called scalar multiplication.

- If $F = \mathbb{R}, \mathbb{Q}, \mathbb{C}, \dots$ then $V$ is resp. called Real vector space, Rational vector space, Complex vector space, ...

- A field $F$ is a vector space over any subfield $K$ of $F$.

- Let $F$ be an arbitrary field, $K^n$ is used to denote the set of all $n$ tuples of elements in $K$. Here $K_n$ is a vector space over $K$ using the following operations:
  1. Vector Addition: $\left(a_{1}, a_{2}, \ldots, a_{n}\right)+\left(b_{1}, b_{2}, \dots, b_{n}\right)=\left(a_{1}+b_{1}, a_{2}+b_{2}, \ldots, a_{n}+b_{n}\right)$
  2. Scalar Multiplication: $k\left(a_{1}, a_{2}, \ldots, a_{n}\right)=\left(k a_{1}, k a_{2}, \ldots, k a_{n}\right)$
- Let $P_n(t)$ denote the set of all polynomials $p(t)$ over a field $K$, where the degree of $p(t)$ is less than or equal to $n$; that is, $p(t)=a_{0}+a_{1} t+a_{2} t^{2}+\cdots+a_{s} t^{s}$ where $s \leq n$. Then $P_n(t)$ is a vector space over $K$ with respect to the usual operations of addition of polynomials and of multiplication of a polynomial by a constant. We include the zero polynomial 0 as an element of $P_n(t)$, even though its degree is undefined.

- **Function Space:** Let $X$ be a nonempty set and let $K$ be an arbitrary field. Let $F(X)$ denote the set of all functions of $X$ into $K$. [Note that $F(X)$ is nonempty, because X is nonempty.] Then $F(X)$ is a vector space over $K$ with respect to the following operations:
  1. Vector Addition: The sum of two functions $f$ and $g$ in $F(X)$ is the function $f + g$ in $F(X)$ defined by $(f+g)(x)=f(x)+g(x) \quad \forall x \in X$
  2. Scalar Multiplication: The product of a scalar $k \in K$ and a function $f$ in $F(X)$ is the function $kf$ in $F(X)$ defined by $(k f)(x)=k f(x) \quad \forall x \in X$

## Spanning Sets

Let $V$ be a vector space over $K$. Vectors $u_1, u_2, \dots, u_m$ in $V$ are said to span $V$ or to form a spanning set of $V$ if every $v$ in $V$ is a linear combination of the vectors $u_1, \dots, u_m$ that is, if there exist scalars $a_1, a_2, \dots, a_m$ in K such that $v=a_{1} u_{1}+a_{2} u_{2}+\cdots+a_{m} u_{m}$

$\begin{array}{l}{\text { Remark 1: Suppose } u_{1}, u_{2}, \ldots, u_{m} \text { span } V \text { and suppose } u_{k} \\\ \text { is a linear combination of some of the }} \\\ {\text { other } u^{\prime} \text { s. Then the } u^{\prime} \text { s without } u_{k} \text { also span } V .}\end{array}$

$\begin{array}{l}{\text { Remark 2: Suppose } u_{1}, u_{2}, \ldots, u_{m} \text { span } V \\\ \text { and suppose one of the } u^{\prime} \text { 's the zero vector. Then the }} \\\ {u^{\prime} \text { 's without the zero vector also span } V \text { . }}\end{array}$

## Subspacees

Let $V$ be a vector space over a field $K$ and let $W$ be a subset of $V$. Then $W$ is a subspace of $V$ if $W$ is itself a vector space over $K$ with respect to the operations of vector addition and scalar multiplication on $V$.

**Theorem:** Suppose $W$ is a subset of a vector space $V$. Then $W$ is a subspace of $V$ if the following two conditions hold:

1.  The zero vector $0$ belongs to $W$.
2.  For every $u, v \in W, k \in K : \text { (i) The sum } u+v \in W . \text { (ii) The multiple } k u \in W$

Both properties may be combined into the following equivalent single statement:

$\text { For every } u, v \in W, a, b \in K, \text { the linear combination } a u+b v \in W$

- Now let $V$ be any vector space. Then $V$ automatically contains two subspaces: the set ${0}$ consisting of the zero vector alone and the whole space $V$ itself. These are sometimes called the trivial subspaces of $V$.

- Let $V$ be the vector space of real-valued functions. Then the collection $W_1$ of continuous functions and the collection $W_2$ of differentiable functions are subspaces of $V$.

### Intersection of Subspaces

Let $U$ and $W$ be subspaces of a vector space $V$. We show that the intersection $U \cap W$ is also a subspace of $V$. Clearly, $0 \in U$ and $0 \in W$, because $U$ and $W$ are subspaces; whence $0 \in U \cap W$. Now suppose $u$ and $v$ belong to the intersection $U \cap W$ now because $U$ and $W$ are subspaces, for any scalars $a, b \in K$, $au + bv \in U \text{ and } au + bv \in W$

Thus, $au+bv \in U \cap W$. Therefore, $U \cap W$ is a subspace of $V$.

The above result generalizes as follows.

**Theorem:** The intersection of any number of subspaces of a vector space $V$ is a subspace of $V$.

Similarly,

**Theorem:** The solution set $W$ of a homogeneous system $AX = 0$ in $n$ unknowns is a subspace of $K^n$.

## Linear Spans

Suppose $u_1, u_2, \dots, u_m$ are any vectors in a vector space $V$. The collection of all linear combinations of them is denoted by $span(u_1, u_2, \dots, u_m) \text{ or } span(u_i)$ and is called linear span of them.

It is easy to see that $span(u_i)$ is a subspace of $V$.

More generally, for any subset $S$ of $V$, $span(S)$ consists of all linear combinations of vectors in $S$ or, when $S = \phi$, $span(S) = {0}$.

Thus, in particular, S is a spanning set of $span(S)$.

**Theorem:** Let $S$ be a subset of a vector space $V$.

1. Then $span(S)$ is a subspace of $V$ that contains $S$.
2. If $W$ is a subspace of $V$ containing $S$, then $span(S) \subseteq W$ (i.e. $span(S)$ is the 'smallest' subspace of $V$ containing $S$).

- Consider the vector space $V = R^3$
  - Let $u$ be any non zero vector in $R^3$. Then $span(u)$ consists of all scalar multiples of $u$. Geometrically, $span(u)$ is the line through the origin O and the endpoint of $u$
  - Let $u$ and $v$ be vectors in $R^3$ that are not multiples of each other. Then $span(u, v)$ is the plane through the origin O and the endpoints of $u$ and $v$

## Row space of a matrix

Let $A=[a_{ij}]$ be an arbitrary $m \times n$ matrix over a field $K$. The rows of $A$,

$R_{1}=\left(a_{11}, a_{12}, \ldots, a_{1 n}\right), \quad R_{2}=\left(a_{21}, a_{22}, \ldots, a_{2 n}\right), \quad \ldots, \quad R_{m}=\left(a_{m 1}, a_{m 2}, \ldots, a_{m n}\right)$

may be viewed as vectors in $K^n$; hence, they span a subspace of $K^n$ called the row space of $A$ and denoted by $rowsp(A)$. That is,
$rowsp(A) = span(R_1, R_2, \dots, R_m)$
Analgously we have column span, $colsp(A) = rowsp(A^T)$

- Suppose $M$ is the matrix obtained by applying elementary row operations on a matrix $A$. Then each row of $M$ is a row of $A$ or a linear combination of rows of $A$. Hence, the row space of $M$ is contained in the row space of $A$. On the other hand, we can apply the inverse elementary row operation on $M$ to obtain $A$; hence, the row space of $A$ is contained in the row space of $M$. Accordingly, $A$ and $M$ have the same row space. Thus, Row equivalent matrices have the same row space.

**Theorem:** Suppose $A = [a_{ij}]$ and $B = [b_{ij}]$ are row equivalent echelon matrices with respective pivot entries $a_{1j_1},a_{2j_2},\dots ,a_{rj_r}$ and $b_{1k_1},b_{2k_2},\dots ,
b_{sk_s}$ Then $A$ and $B$ have the same number of nonzero rows—that is, $r = s$—and their
pivot entries are in the same positions—that is, $j_{1}=k_{1}, j_{2}=k_{2}, \ldots, j_{r}=k_{r}$.

**Theorem:** Suppose $A$ and $B$ are row canonical matrices. Then $A$ and $B$ have the same row space if and only if they have the same nonzero rows.

**Corollary:** Every matrix $A$ is row equivalent to a unique matrix in row canonical form.

- Consider the following two sets of vectors in $R^4$:

  $u_{1}=(1,2,-1,3), \quad u_{2}=(2,4,1,-2), \quad u_{3}=(3,6,3,-7)$

  $w_{1}=(1,2,-4,11), \quad w_{2}=(2,4,-5,14)$

  Let $U = span(u_i)$ and $W = span(w_i)$. There are two ways to show that $U = W$.

  1. Show that each $u_i$ is a linear combination of $w_1$ and $w_2$, and show that each $w_i$ is a linear combination of $u_1, u_2, u_3$. Observe that we have to show that six systems of linear equations are consistent.

  2. Form the matrix $A$ whose rows are $u_1, u_2, u_3$ and row reduce $A$ to row canonical form, and form the matrix $B$ whose rows are $w_1$ and $w_2$ and row reduce $B$ to row canonical form:

  $A=\left[\begin{array}{rrrr}{1} & {2} & {-1} & {3} \\\ {2} & {4} & {1} & {-2} \\\ {3} & {6} & {3} & {-7}\end{array}\right] \sim\left[\begin{array}{rrrr}{1} & {2} & {-1} & {3} \\\ {0} & {0} & {3} & {-8} \\\ {0} & {0} & {6} & {-16}\end{array}\right] \sim\left[\begin{array}{rrrr}{1} & {2} & {0} & {\frac{1}{3}} \\\ {0} & {0} & {1} & {-\frac{8}{3}} \\\ {0} & {0} & {0} & {0}\end{array}\right]$

  $B=\left[\begin{array}{rrrr}{1} & {2} & {-4} & {11} \\\ {2} & {4} & {-5} & {14}\end{array}\right] \sim\left[\begin{array}{rrrr}{1} & {2} & {-4} & {11} \\\ {0} & {0} & {3} & {-8}\end{array}\right] \sim\left[\begin{array}{cccc}{1} & {2} & {0} & {\frac{1}{3}} \\\ {0} & {0} & {1} & {-\frac{8}{3}}\end{array}\right]$

  Because the nonzero rows of the matrices in row canonical form are identical, the row spaces of $A$ and $B$ are equal. Therefore, $U = W$.

## Linear Dependence and Independence

We say that the vectors $v_1, v_2, \dots, v_m$ in $V$ are linearly dependent if there exist scalars $a_1, a_2, \dots, a_m$ in $K$, not all of them 0, such that

$a_{1} v_{1}+a_{2} v_{2}+\cdots+a_{m} v_{m}=0$

Otherwise, we say that the vectors are linearly independent.

A set $S = {v_1, \dots, v_m}$ of vectors in $V$ is linearly dependent or independent according to whether the vectors $v_1, \dots, v_m$ are linearly dependent or independent.

An infinite set $S$ of vectors is linearly dependent or independent according to whether there do or do not exist vectors $v_1,v_2,\dots,v_k$ in $S$ that are linearly dependent.

- Suppose 0 is one of the vectors $v_1, v_2, \dots , v_m$, say $v_1 = 0$. Then the vectors must be linearly dependent.
- Suppose v is a nonzero vector. Then v, by itself, is linearly independent
- Let $V$ be the vector space of functions from $R$ into $R$. We show that the functions $f (t) = sin t, g(t) = e^t , h(t) = t^2$ are linearly independent. We form the vector (function) equation $xf + yg + zh = 0$, where $x, y, z$ are unknown scalars. This function equation means that, for every value of $t$,
  $x \sin t+y e^{t}+z t^{2}=0$

Thus, in this equation, we choose appropriate values of $t$ to easily get $x = 0, y = 0, z = 0$.

1. $\text { Substitute } t=0 \quad \text { to } \operatorname{obtain} x(0)+y(1)+z(0)=0 \quad \text { or } \quad y=0$
2. $\text { Substitute } t=\pi \quad \text { to } \operatorname{obtain} x(0)+0\left(e^{\pi}\right)+z\left(\pi^{2}\right)=0 \quad \text { or } \quad \text { or } \quad z=0$
3. $\text { Substitute } t=\pi / 2 \quad \text { to obtain } x(1)+0\left(e^{\pi / 2}\right)+0\left(\pi^{2} / 4\right)=0 \quad \text { or } \quad x=0$

Thus $u, v$ and $w$ are LI.

Why is linear independence important? Well, if a set of vectors is linearly dependent, then we can get rid of at least one or perhaps more of the vectors until we get a linearly independent set. This set is then the smallest “truly essential” set with which we can work.

## Basis and Dimension

A set $S = {u_1, u_2, \dots, u_n}$ of vectors is a basis of $V$ if it spans V and is linearly independent.

**Theorem:** Let $V$ be a vector space such that one basis has $m$ elements and another basis has $n$ elements, then, $m = n$.

This theorem is the consequence of the following replacement lemma.

**Lemma:** Suppose $\\{v_1, v_2, \dots, v_n\\}$ spans $V$, and suppose $\\{w_1, w_2, \dots, w_m\\}$ is linearly independent. Then $m \leq n$, and $V$ is spanned by a set of the form $\left\\{w_{1}, w_{2}, \ldots, w_{m}, v_{i_{1}}, v_{i_{2}}, \ldots, v_{i_{n-m}}\right\\}$. Thus, in particular, $n + 1$ or more vectors in $V$ are linearly dependent.

A vector space $V$ is said to be of finite dimension $n$ or $n$-dimensional, written $dim(V) = n$ if $V$ has a basis with $n$ elements. The vector space $\\{0\\}$ is defined to have dimension 0.

Suppose a vector space $V$ does not have a finite basis. Then $V$ is said to be of infinite dimension or to be infinite-dimensional.

**Theorem:** Let $V$ be a vector space of finite dimension $n$.

1. Any linearly independent set $S = \\{u_1, u_2, \dots, u_n\\}$ with $n$ elements is a basis of $V$.
2. Any spanning set $T = \\{v_1, v_2, \dots, v_n\\} of $V$ with $n$ elements is a basis of $V\$.

**Proof:**

1. Suppose it does not $span(V)$ that means there exist a vector $v$ which is not a linear combination of $S$ thus $S \cup \\{v\\}$ is linearly independent which by above lemma is not possible.
2. Suppose this set is not LI then its dimension is less than $n$, which we know is not possible as cardinality of basis is always the same.

-> On page 125

### Example of bases

- Vector space $K^n$: $e_{1}=(1,0,0,0, \ldots, 0,0), e_{2}=(0,1,0,0, \ldots, 0,0), \ldots, e_{n}=(0,0,0,0, \ldots, 0,1)$ These vectors are linearly independent. (For example, they form a matrix in echelon form.) Accordingly, the vectors form a basis of $K^n$ called the usual or standard basis of $K^n$
- Vector space $M = M_{r,s}$ of all $r \times s$ matrices, let $E_{ij}$ be the matrix with $ij$-entry 1 and 0's elsewhere. Then all such matrices (in total $rs$) form a basis of $M_{r,s}$ called the usual or standard basis of $M_{r,s}$. Accordingly, $dim (M_{r,s}) = rs$.
- Vector space $P_n(t)$ of all polynomials of degree $\leq n$: The set $S = \\{1, t, t^2, \dots, t^n\\}$ of $n + 1$ polynomials is a basis of $P_n(t)$.
- Vector space $P(t)$ of all polynomials: Consider any finite set $S = \\{f_1(t), f_2(t), \dots, f_m(t)\\}$ of polynomials in $P(t)$, and let $m$ denote the largest of the degrees of the polynomials. Then any polynomial $g(t)$ of degree exceeding $m$ cannot be expressed as a linear combination of the elements of $S$. Thus, $S$ cannot be a basis of $P(t)$. This means that the dimension of $P(t)$ is infinite. We note that the infinite set $S' = \\{1, t, t^2, t^3, \dots\\}$ consisting of all the powers of $t$, spans $P(t)$ and is linearly independent. Accordingly, $S'$ is an infinite basis of $P(t)\$.

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
