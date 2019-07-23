---
id: vector_spaces
title: Vector Spaces, LSEQ and Rank of a Matrix
sidebar_label: Vector Spaces, LSEQ and Rank of a Matrix
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

- $k0 = 0$ (easy)
- $0u = 0$ (easy)
- if $ku = 0 \rightarrow k = 0 \text{ or } u = 0$ (Suppose $k \neq 0 \rightarrow \exists k^{-1} \operatorname{s.t.} kk^{-1} = 1$ $\rightarrow k^{-1}(ku) = 0 \rightarrow 1u = 0 \rightarrow u = 0$)
- $k(-u) = -ku$ (As $k(u - u) = 0 = ku + k(-u) \rightarrow -ku = k(-u))$)
- $(-k)u = -ku$ (Proof similar as above)
- $u + u = 2u$ (As $1u + 1u = (1 + 1)u = 2u$)
- Thus, an internal composition in $V$ is called vector addition and external composition in $V$ over the field $F$ is called scalar multiplication.

- If $F = \mathbb{R}, \mathbb{Q}, \mathbb{C}, \dots$ then $V$ is resp. called Real vector space, Rational vector space, Complex vector space, ...

- A field $F$ is a vector space over any subfield $K$ of $F$.

- Let $K$ be an arbitrary field, $K^n$ is used to denote the set of all $n$ tuples of elements in $K$. Here $K^n$ is a vector space over $K$ using the following operations:
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

---

**Theorem:** Suppose $W$ is a subset of a vector space $V$. Then $W$ is a subspace of $V$ if the following two conditions hold:

1.  The zero vector $0$ belongs to $W$.
2.  For every $u, v \in W, k \in K : \text { (i) The sum } u+v \in W . \text { (ii) The multiple } k u \in W$

Both properties may be combined into the following equivalent single statement:

$\text { For every } u, v \in W, a, b \in K, \text { the linear combination } a u+b v \in W$

---

- Now let $V$ be any vector space. Then $V$ automatically contains two subspaces: the set $\\{0\\}$ consisting of the zero vector alone and the whole space $V$ itself. These are sometimes called the trivial subspaces of $V$.

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

More generally, for any subset $S$ of $V$, $span(S)$ consists of all linear combinations of vectors in $S$ or, when $S = \phi$, $span(S) = \\{0\\}$.

Thus, in particular, S is a spanning set of $span(S)$.

**Theorem:** Let $S$ be a subset of a vector space $V$.

1. Then $span(S)$ is a subspace of $V$ that contains $S$. (easy to prove)
2. If $W$ is a subspace of $V$ containing $S$, then $span(S) \subseteq W$ (i.e. $span(S)$ is the 'smallest' subspace of $V$ containing $S$). (easy to prove)

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

  In the context of lseq, this would mean that row equivalent matrices have the same set of solution because they span same set of equations.
  (Note well that we are dealing with row operations, No column operations on the augmented matrix are permitted in this context because they would generally alter the soln set)

---

**Theorem:** Suppose $A = [a_{ij}]$ and $B = [b_{ij}]$ are row equivalent echelon matrices with respective pivot entries $a_{1j_1},a_{2j_2},\dots ,a_{rj_r}$ and $b_{1k_1},b_{2k_2},\dots ,
b_{sk_s}$ Then $A$ and $B$ have the same number of nonzero rows—that is, $r = s$—and their
pivot entries are in the same positions—that is, $j_{1}=k_{1}, j_{2}=k_{2}, \ldots, j_{r}=k_{r}$. (Easy as o/w row space is clearly different)

---

---

**Theorem:** Suppose $A$ and $B$ are row canonical matrices. Then $A$ and $B$ have the same row space if and only if they have the same nonzero rows.

**Proof:** Consider $i$th non zero row of $A$. Consider vectors belonging to its row space having only that pivot element set to 1 and rest all pivot elements set to 0. That means only this row is multiplied by 1 and rest all rows are multiplied by 0. So to get this vector in $B$, we would have to keep only this $i$th row multiplied by 1 and rest all zero. Thus the rows are same.

---

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

Why is linear independence important? Well, if a set of vectors is linearly dependent, then we can get rid of at least one or perhaps more of the vectors until we get a linearly independent set. This set is then the smallest "truly essential" set with which we can work.

**Lemma:** Suppose two or more nonzero vectors $v_1, v_2, \dots, v_m$ are linearly dependent. Then one of the vectors is a linear combination of the preceding vectors; that is, there exists $k > 1$ such that $v_{k}=c_{1} v_{1}+c_{2} v_{2}+\cdots+c_{k-1} v_{k-1}$ (easy to prove)

## Basis and Dimension

A set $S = {u_1, u_2, \dots, u_n}$ of vectors is a basis of $V$ if it spans V and is linearly independent.

**Theorem:** Let $V$ be a vector space such that one basis has $m$ elements and another basis has $n$ elements, then, $m = n$.

This theorem is the consequence of the following replacement lemma.

**Lemma:** Suppose $\\{v_1, v_2, \dots, v_n\\}$ spans $V$, and suppose $\\{w_1, w_2, \dots, w_m\\}$ is linearly independent. Then $m \leq n$, and $V$ is spanned by a set of the form $\left\\{w_{1}, w_{2}, \ldots, w_{m}, v_{i_{1}}, v_{i_{2}}, \ldots, v_{i_{n-m}}\right\\}$. Thus, in particular, $n + 1$ or more vectors in $V$ are linearly dependent.

**Proof:** Because $\\{v_i\\}$ spans $V$, we have $\left\\{w_{1}, v_{1}, \ldots, v_{n}\right\\} \label{1} \tag{1}$ is linearly dependent and also spans $V$. By previous Lemma, one of the vectors in is a linear combination of
the preceding vectors. This vector cannot be $w_1$, so it must be one of the $v's$, say $v_j$: Thus we can delete $v_j$ from the spanning set and obtain the spanning set $\left\\{w_{1}, v_{1}, \ldots, v_{j-1}, \quad v_{j+1}, \ldots, v_{n}\right\\} \tag{2} \label{2}$ Now we repeat the argument with the vector $w_2$. That is, because $\eqref{2}$ spans $V$, the set $\left\\{w_{1}, w_{2}, v_{1}, \ldots, v_{j-1}, \quad v_{j+1}, \ldots, v_{n}\right\\} \label{3} \tag{3}$ is linearly dependent and also spans $V$. Again by previous Lemma, one of the vectors in $\eqref{3}$ is a linear
combination of the preceding vectors. We emphasize that this vector cannot be $w_1$ or $w_2$, because
$\\{w_1, \dots , w_m\\}$ is independent; hence, it must be one of the $v's$, say $v_k$. Thus, we can
delete $v_k$ from the spanning set $\eqref{3}$ and obtain the spanning set
$\left\\{w_{1}, w_{2}, v_{1}, \ldots, v_{j-1}, \quad v_{j+1}, \ldots, v_{k-1}, \quad v_{k+1}, \ldots, v_{n}\right\\}$
We repeat the argument with $w_3$, and so forth. At each step, we are able to add one of the $w's$ and delete
one of the $v's$ in the spanning set. If $m \leq n$, then we finally obtain a spanning set of the required form:
$\left\\{w_{1}, \ldots, w_{m}, v_{i_{1}}, \ldots, v_{i_{n-m}}\right\\}$

Finally, we show that $m > n$ is not possible. Otherwise, after $n$ of the above steps, we obtain the
spanning set $\\{w_1, \dots , w_n\\}$. This implies that $w_{n+1}$ is a linear combination of $w_1, \dots , w_n$, which contradicts
the hypothesis that $\\{w_i\\}$ is linearly independent.

A vector space $V$ is said to be of finite dimension $n$ or $n$-dimensional, written $dim(V) = n$ if $V$ has a basis with $n$ elements. The vector space $\\{0\\}$ is defined to have dimension 0.

Suppose a vector space $V$ does not have a finite basis. Then $V$ is said to be of infinite dimension or to be infinite-dimensional.

**Theorem:** Let $V$ be a vector space of finite dimension $n$.

1. Any linearly independent set $S = \\{u_1, u_2, \dots, u_n\\}$ with $n$ elements is a basis of $V$. (Always use this fact if possible to prove that the given $n$ element independent set form the basis)
2. Any spanning set $T = \\{v_1, v_2, \dots, v_n\\}$ of $V$ with $n$ elements is a basis of $V\$.

**Proof:**

1. Suppose it does not $span(V)$ that means there exist a vector $v$ which is not a linear combination of $S$ thus $S \cup \\{v\\}$ is linearly independent which by above lemma is not possible.
2. Suppose this set is not LI then its dimension is less than $n$, which we know is not possible as cardinality of basis is always the same.

Similarly it is straight forward to prove the following theorems:

---

**Theorem:** that if $S$ spans a vector space $V$. Then,

1. Any maximum number of linearly independent vectors in $S$ form a basis of $V$.
2. Suppose one deletes from $S$ every vector that is a linear combination of preceding vectors in $S$. Then the remaining vectors form a basis of $V$.

---

---

**Theorem:** Let $V$ be a vector space of finite dimension and let $S = \\{u_1, u_2, \dots , u_r\\}$ be a
set of linearly independent vectors in $V$. Then $S$ is part of a basis of $V$; that is, $S$ may be extended
to a basis of $V$

---


---

**Theorem:** Let $W$ be a subspace of an $n$-dimensional vector space $V$. Then $dim(W) \leq n$. In particular, if $dim(W) = n$, then $W = V$. (easy to prove)

---

## Rank of a Matrix

The rank of a matrix $A$ is the maximum number of linearly independent row vectors of $A$. It is denoted by rank $A$.

Note further that $rank A = 0$ if and only if $A = 0$. This follows directly from the definition.

**Theorem**: Row-equivalent matrices have the same rank. So to find rank of the matrix, convert it into row echelon form and count the number of non zero rows.

**Theorem**: Consider $p$ vectors that each have $n$ components. Then these vectors are linearly independent if the matrix formed, with these vectors as row vectors, has rank $p$. However, these vectors are linearly dependent if that matrix has rank less than $p$.

**Theorem**: The rank $r$ of a matrix $A$ equals the maximum number of linearly independent column vectors of $A$.
Hence $A$ and its transpose $A^T$ have the same rank.

**Proof**: Let $A$ be an $m \cdot n$ matrix of $rank A = r$. Then by definition of rank, $A$ has $r$ linearly independent rows which we denote by $v_{(1)}, \dots , v_{(r)}$ (regardless of their position in $A$), and all the rows $a_{(1)}, \dots , a_{(m)}$ of $A$ are linear combinations of those, say,

$a_{(1)} = c_{11}v_{(1)} + c_{12}v_{(2)} + \dots + c_{1r}v_{(r)}$

$a_{(2)} = c_{21}v_{(1)} + \dots + c_{2r}v_{(r)}$

$\vdots$

$a_{(m)} = c_{m1}v_{(1)} + \dots + c_{mr}v_{(r)}$

These are vector equations for rows. To switch to columns, we write in terms of
components as $n$ such systems, with $k = 1, \dots , n$,

$a_{1k} = c_{11}v_{1k} + c_{12}v_{2k} + \dots + c_{1r}v_{rk}$

$\vdots$

$a_{mk} = c_{m1}v_{1k} + c_{m2}v_{2k} + \dots + c_{mr}v_{rk}$

Treat the LHS as a column vector and RHS as linear combination of $r$ column vectors ($[c_{1i}, c_{2i}, \dots, c_{mi}]$). Now the vector on the left is the $k$th column vector of $A$. We see that each of these $n$ columns is a linear combination of the same $r$ columns on the right. Hence $A$ cannot have more linearly independent columns than rows. Now rows of $A$ are columns of the transpose $A^T$. For $A^T$ our conclusion is that $A^T$ cannot have more linearly independent columns than rows, so that $A$ cannot have more linearly independent rows than columns. Together, the number of linearly independent columns of $A$ must be $r$, the rank of $A$. $\blacksquare$

:::tip Info
Therefore dimension of row space (aka row rank) is same as dimension of column space (aka column rank) which is same as rank of the matrix.
:::

**Theorem**: From above two theorems, it follows that if we have $p$ vectors each having $n$ components. If $n < p$, then these vectors are linearly dependent.

**Theorem**: Column-equivalent (defined analogousely) matrices have the same rank. As elementary column operations is row operations on the transpose. Thus it follows that any combination of elementary row and column operations will not change the rank of the matrix and thus can be used to compute rank of it.

:::tip Info

1. Rank of a matrix is same as the order of highest order non zero submatrix. Thus if rank = $n$ then any submatrix of higher order will have determinant = 0 and $|A| \neq 0 \iff rank = n$ .
2. It is easily observable that if all minors of order k are zero then rank is certainly less than k as minor of higher order will use throughout its computation minors of smaller order.
3. Every non zero matrix have rank $\geq 1$ (as we have non zero minor of order 1).
4. From all this it follows that rank of a submatrix is $\leq$ rank of parent.
   :::

## Gauss Elimination

Is basically converting the augmented matrix into row echelon form (using elementary row operations), from $Ax = b$ to $Rx = f$ where $R$ is in row echelon form.

The number of nonzero rows, $r$, in $R$ is called the rank of $R$ and also the rank of $A$. Here is the method for determining whether $Ax = b$ has solutions and what they are:

1. No solution. If $r$ is less than $m$ (meaning that $R$ actually has at least one row of all 0s) and at least one of the numbers $f_{r+1}, f_{r+2}, \dots , f_m$ is not zero, then the system $Rx = f$ is inconsistent: No solution is possible.

If the system is consistent (either $r = m$, or $r < m$ and all the numbers $f_{r+1}, f_{r+2}, \dots , f_m$ are zero), then there are solutions.

2. Unique solution. If the system is consistent and $r = n$, there is exactly one solution, which can be found by back substitution.
3. Infinitely many solutions. To obtain any of these solutions, choose values of $x_{r+1}, \dots , x_n$ arbitrarily. Then solve the $r$th equation for $x_r$ (in terms of those arbitrary values), then the $(r - 1)$st equation for $x_{r-1}$, and so on up the line.

:::tip Info
Thus it can be said that the system is consistent if the rank of $A$ and $[A | b]$ is same.
:::


## Example of basis

- Vector space $K^n$: $e_{1}=(1,0,0,0, \ldots, 0,0), e_{2}=(0,1,0,0, \ldots, 0,0), \ldots, e_{n}=(0,0,0,0, \ldots, 0,1)$ These vectors are linearly independent. (For example, they form a matrix in echelon form.) Accordingly, the vectors form a basis of $K^n$ called the usual or standard basis of $K^n$
- Vector space $M = M_{r,s}$ of all $r \times s$ matrices, let $E_{ij}$ be the matrix with $ij$-entry 1 and 0's elsewhere. Then all such matrices (in total $rs$) form a basis of $M_{r,s}$ (As matrix need to be represented as a linear combination of matrices) called the usual or standard basis of $M_{r,s}$. Accordingly, $dim (M_{r,s}) = rs$.
- Vector space $P_n(t)$ of all polynomials of degree $\leq n$: The set $S = \\{1, t, t^2, \dots, t^n\\}$ of $n + 1$ polynomials is a basis of $P_n(t)$.
- Vector space $P(t)$ of all polynomials: Consider any finite set $S = \\{f_1(t), f_2(t), \dots, f_m(t)\\}$ of polynomials in $P(t)$, and let $m$ denote the largest of the degrees of the polynomials. Then any polynomial $g(t)$ of degree exceeding $m$ cannot be expressed as a linear combination of the elements of $S$. Thus, $S$ cannot be a basis of $P(t)$. This means that the dimension of $P(t)$ is infinite. We note that the infinite set $S' = \\{1, t, t^2, t^3, \dots\\}$ consisting of all the powers of $t$, spans $P(t)$ and is linearly independent. Accordingly, $S'$ is an infinite basis of $P(t)\$.
- The following four vectors in $R^4$ form a matrix in echelon form: $(1,1,1,1),(0,1,1,1),(0,0,1,1),(0,0,0,1)$ Thus, the vectors are linearly independent, and, because $dim(R^4) = 4$, the four vectors form a basis of $R^4$.
- Echelon matrix $B$ (whose pivots are circled) is an echelon form of $A$:

  $A=\left[\begin{array}{cccccc}{1} & {2} & {1} & {3} & {1} & {2} \\\ {2} & {5} & {5} & {6} & {4} & {5} \\\ {3} & {7} & {6} & {11} & {6} & {9} \\\ {1} & {5} & {10} & {8} & {9} & {9} \\\ {2} & {6} & {8} & {11} & {9} & {12}\end{array}\right]$

  $B=\left[\begin{array}{llllll}{0} & {2} & {1} & {3} & {1} & {2} \\\ {0} & {0} & {3} & {1} & {2} & {1} \\\ {0} & {0} & {0} & {0} & {1} & {2} \\\ {0} & {0} & {0} & {0} & {0} & {0} \\\ {0} & {0} & {0} & {0} & {0} & {0}\end{array}\right]$

  Therefore basis of $rowsp(A) = \\{(1,2,1,3,1,2), \quad(0,1,3,1,2,1), \quad(0,0,0,1,1,2)\\}$

  Now to find each column $C_k$ of $A$ that is a linear combination of preceding columns of $A$.

  Let $M_k = [C_1, C_2, \dots, C_k]$ the submatrix of $A$ consisting of the first $k$ columns of $A$. Then $M_{k - 1}$ and $M_k$ are, respectively, the coefficient matrix and augmented matrix of the vector equation $x_{1} C_{1}+x_{2} C_{2}+\cdots+x_{k-1} C_{k-1}=C_{k}$ this system has a solution, or, equivalently, $C_k$ is a linear combination of the preceding columns of $A$ if and only if $rank(M_k) = rank(M_{k - 1})$. Now the first $k$ column of the echelon matrix $B$ is also an echelon form of $M_k$. Accordingly, $\operatorname{rank}\left(M_{2}\right)=\operatorname{rank}\left(M_{3}\right)=2$ and $\operatorname{rank}\left(M_{4}\right)=\operatorname{rank}\left(M_{5}\right)=\operatorname{rank}\left(M_{6}\right)=3$. Thus, $C_3, C_5, C_6$ are each a linear combination of the preceding columns of $A$.

  Now to find basis of column space, the fact that the remaining columns $C_1, C_2, C_4$ are not linear combinations of their respective preceding columns also tells us that they are linearly independent. Thus, they form a basis of the column space of $A$. That is, $\text { basis of } \operatorname{colsp}(A) : \quad[1,2,3,1,2]^{T}, \quad[2,5,7,5,6]^{T}, \quad[3,6,11,8,11]^{T}$ Observe that $C_1, C_2, C_4$ may also be characterized as those columns of $A$ that contain the pivots in any echelon form of $A$. (thus, if it is asked to express a column in terms of basis columns, we can go with equation $$\sum_{i < k \text{ and } C_i \text{ is a part of basis found above }}x_{i} C_{i}=C_{k}$$ then form an augemented matrix and solve to find variables)

  From this exercise we have the following two methods to find basis of the subspace spanned by the vectors $u_1, \dots, u_r$.

  **Algorithm 1**

  1. Form the matrix M whose rows are the given vectors.
  2. Row reduce M to echelon form.
  3. Output the nonzero rows of the echelon matrix.

  But sometimes we want to find a basis that only comes from the original given vectors.

  **Algorithm 2**

  1. Form the matrix $M$ whose columns are the given vectors.
  2. Row reduce $M$ to echelon form.
  3. For each column $C_k$ in the echelon matrix without a pivot, delete (cast out) the vector $u_k$ from the list $S$ of given vectors.
  4. Output the remaining vectors in $S$ (which correspond to columns with pivots).

  - **Example:** Let $W$ be the subspace of $R^5$ spanned by the following vectors:
    $u_{1}=(1,2,1,3,2), \quad u_{2}=(1,3,3,5,3), \quad u_{3}=(3,8,7,13,8)$
    $u_{4}=(1,4,6,9,7), \quad u_{5}=(5,13,13,25,19)$

    Find a basis of $W$ consisting of the original given vectors, and find $dim (W)$.

    $M=\left[\begin{array}{ccccc}{1} & {1} & {3} & {1} & {5} \\\ {2} & {3} & {8} & {4} & {13} \\\ {1} & {3} & {7} & {6} & {13} \\\ {3} & {5} & {13} & {9} & {25} \\\ {2} & {3} & {8} & {7} & {19}\end{array}\right] \sim\left[\begin{array}{ccccc}{1} & {1} & {3} & {1} & {5} \\\ {0} & {1} & {2} & {2} & {3} \\\ {0} & {0} & {0} & {1} & {2} \\\ {0} & {0} & {0} & {0} & {0} \\\ {0} & {0} & {0} & {0} & {0}\end{array}\right]$

    The pivots in the echelon matrix appear in columns $C_1, C_2, C_4$. Accordingly, we 'cast out' the vectors $u_3$ and $u_5$ from the original five vectors. The remaining vectors $u_1, u_2, u_4$, which correspond to the columns in the echelon matrix with pivots, form a basis of $W$. Thus, in particular, $dim(W) = 3$

- Extend $\\{u_1 = (1,1,1,1),u_2 = (2,2,3,4)\\}$ to a basis of $R^4$.

  First form the matrix with rows $u_1$ and $u_2$, and reduce to echelon form:

  $\left[\begin{array}{llll}{1} & {1} & {1} & {1} \\\ {2} & {2} & {3} & {4}\end{array}\right] \sim\left[\begin{array}{llll}{1} & {1} & {1} & {1} \\\ {0} & {0} & {1} & {2}\end{array}\right]$

  Then $w_1 =(1,1,1,1)$ and $w_2 =(0,0,1,2)$ span the same set of vectors as spanned by $u_1$ and $u_2$. Let $u_3 = (0,1,0,0)$ and $u_4 = (0,0,0,1)$. Then $w_1, u_3, w_2, u_4$ form a matrix in echelon form. Thus, they are linearly independent, and they form a basis of $R^4$. Hence, $u_1, u_2, u_3, u_4$ also form a basis of $R^4$.
- Find Basis of subspace $W$ of $R^3$ where $W = \\{(a, b, c) : a + b + c = 0\\}$
  i.e. vectors of the form $(x, y, -x - y)$, clearly $(1, 0, -1) \text{ and } (0, 1, -1)$ spans $W\$ and are linearly independent and hence they form the basis.

---

**Theorem:** The dimension of the solution space $W$ of a homogeneous system $AX = 0$ is $n - r$, where $n$ is the number of unknowns and $r$ is the rank of the coefficient matrix $A$.

---

In the case where the system $AX = 0$ is in echelon form, it has precisely $n - r$ free variables, say $x_{i_1} , x_{i_2} , \dots , x_{i_{n-r}}$ . Let $v_j$ be the solution obtained by setting $x_{i_j} = 1$ (or any nonzero constant) and the remaining free variables equal to 0. Its straightforward to see that the solutions $v_1, v_2, \dots , v_{n-r}$ are linearly independent; hence, they form a basis (as they as well span all the solutions) of the solution space $W$.


- Find the dimension and a basis of the solution space W of each homogeneous system:

  1. $x+2 y+2 z-s+3 t=0$

     $x+2 y+3 z+s+t=0$

     $3 x+6 y+8 z+s+5 t=0$

     Form an augmented matrix, to get $\begin{bmatrix}1 & 2 & -1 & 3 & 0 \\\ 1 & 2 & 3 & 1 & 1 & 0 \\\ 3 & 6 & 8 & 1 & 5 & 0\end{bmatrix} \sim \begin{bmatrix} 1 & 2 & 2 & -1 & 3 & 0 \\\ 0 & 0 & 1 & 2 & -2 & 0 \\\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$

     The system in echelon form has two (nonzero) equations in five unknowns. Hence, the system has
     $5 - 2 = 3$ free variables, which are $y, s, t$. Thus, $\operatorname{dim} W = 3$. We obtain a basis for $W$:

     1. Set $y=1, s=0, t=0 \quad$ to obtain the solution $\quad v_{1}=(-2,1,0,0,0)$
     2. Set $y=0, s=1, t=0 \quad$ to obtain the solution $\quad v_{2}=(5,0,-2,1,0)$
     3. Set $y=0, s=0, t=1 \quad$ to obtain the solution $\quad v_{3}=(-7,0,2,0,1)$

     The set $\left\\{v_{1}, v_{2}, v_{3}\right\\}$ is a basis of the solution space $W$

  2. $\begin{aligned} x+y+2 z &=0 \\\ 2 x+3 y+3 z &=0 \\\ x+3 y+5 z &=0 \end{aligned}$

     Reduce the coefficient matrix $A$ to echelon form:

     $A=\left[\begin{array}{lll}{1} & {1} & {2} \\\ {2} & {3} & {3} \\\ {1} & {3} & {5}\end{array}\right] \sim\left[\begin{array}{rrr}{1} & {1} & {2} \\\ {0} & {1} & {-1} \\\ {0} & {2} & {3}\end{array}\right] \sim\left[\begin{array}{rrr}{1} & {1} & {2} \\\ {0} & {1} & {-1} \\\ {0} & {0} & {5}\end{array}\right]$

     This corresponds to a triangular system with no free variables. Thus, 0 is the only solution; that is, $W = \\{0\\}$. Hence, $\operatorname{dim} W = 0$.

- Find a homogeneous system whose solution set $W$ is spanned by
  $\left\\{u_{1}, u_{2}, u_{3}\right\\}=\{(1,-2,0,3), \quad(1,-1,-1,4), \quad(1,0,-2,5)\}$

  Let $v = (x, y, z, t)$. Then $v \in W$ if and only if $v$ is a linear combination of the vectors $u_1, u_2, u_3$ that span
  $W$. Thus, form the matrix $M$ whose first columns are $u_1, u_2, u_3$ and whose last column is $v$, and then row reduce $M$ to echelon form. This yields

  $M=\left[\begin{array}{rrrr}{1} & {1} & {1} & {x} \\\ {-2} & {-1} & {0} & {y} \\\ {0} & {-1} & {-2} & {z} \\\ {3} & {4} & {5} & {t}\end{array}\right] \sim\left[\begin{array}{rrrr}{1} & {1} & {1} & {x} \\\ {0} & {1} & {2} & {2 x+y} \\\ {0} & {-1} & {-2} & {z} \\\ {0} & {1} & {2} & {-3 x+t}\end{array}\right] \sim\left[\begin{array}{cccc}{1} & {1} & {1} & {x} \\\ {0} & {1} & {2} & {2 x+y} \\\ {0} & {0} & {0} & {2 x+y+z} \\\ {0} & {0} & {0} & {-5 x-y+t}\end{array}\right]$

  Then $v$ is a linear combination of $u_1, u_2, u_3$ if $rank(M) = rank(A)$, where $A$ is the submatrix without column $A$v. Thus, set the last two entries in the fourth column on the right equal to zero to obtain the required homogeneous system:

  $2 x+y+z=0$

  $5 x+y \quad-t=0$


## Inverse of the matrix by Gauss-Jordan Method

Task is to find $A^{-1}$. I.e. to find $X$ s.t. $AX = I$. Make an augmented matrix $\tilde{A} = [A \text{  } I]$ Now reduce it Reduced Row Echelon form to get $[I \text{  } H]$ since this corresponds to $IX = H$, thus $X = H$.

From this analysis we observe that $A^{-1}$ is simply the result of elementary row operations and thus is product of elementary matrices therefore $A$ is as well the product of elementary matrices.

**Examples:**

- Find two non-singular matrices P and Q s.t. PAQ is in the normal (canonical) form (i.e. of the form $\begin{bmatrix} I_r & O \\\ O & O \end{bmatrix}$) where $A = \begin{bmatrix} 1 & 1 & 1 \\\ 1 & -1 & -1 \\\ 3 & 1 & 1\end{bmatrix}$

  For series of row operations $r_1, r_2, ...$ applied, apply them to $I$ to get $R$, similarly for any column operation applied in between, apply it to another $I$ to get $C$, now $P = R, Q = C$. Obv. $P$ and $Q$ aren't unique.

  :::tip Info
  It is observed that authors club row and column equivalent together to define **equivalent** (which is of course an equivalence relation) matrices which are obtained from each other via combination of elementary row and column operations. Thus, above example shows that any matrix is equivalent to this **normal** form.

  From above it follows that if $A$ and $B$ are of same order and of same rank then they are equivalent to each other.
  :::

- Is the matrix $\begin{bmatrix}1 & 2 & 1 \\\ -1 & 0 & 2 \\\ 2 & 1 & -3\end{bmatrix}$ equivalent to $I_3$

  Here determinant of given matrix is non zero and hence it's rank is 3 and therefore it is equivalent to $I_3$.

- Express $\begin{bmatrix} 1 & 3 & 3 \\\ 1 & 4 & 3 \\\ 1 & 3 & 4\end{bmatrix}$ as a product of elementary matrices.

  Question is valid iff $|A| \neq 0$ which is true for the given case.

  Let $A$ be reduced into $I$ by elementary row transformations $r_1, r_2, \dots, r_k \rightarrow (r_k)\dots (r_1)A = I$

  $\rightarrow A = (r_k \dots r_1)^{-1}I = r_1^{-1}\dots r_k^{-1}I$

  For the given case, $r_1 = E_{21}(-1), r_2 = E_{31}(-1), r_3 = E_{12}(-3), r_4 = E_{13}(-3)$

  And thus answer is $E_{21}(1)E_{31}(1)E_{12}(3)E_{13}(3)$

## Rank of product of matrices

Rank of product of matrices cannot exceed rank of either of them.

**Proof:** Proof is simple, suppose we have two matrices $A$ and $B$ each of rank say $p, q$ resp. then it's possible to transform $A$ into $[G \text{  } O]$ where $G$ has only $p$ non zero rows at top, by left multiplication by $P$. Similarly it is possible to transform $B$ into $H$ where $H$ has only $q$ non zero columns at left, by right multiplication by $Q$. Now since $P, Q$ are result of elementary matrices that implies $rank(AB) = rank(PGHQ) = rank (GH)$ which is $\leq min(p, q)$

**Aliter:**

1. $RB$ is a linear combination of the rows of $B$, where $R$ is a row vector. (easy)
2. The row space of $AB$ is contained in the row space of $B$. (follows from above)
3. If $C$ is a column vector and $AC$ is defined, then $AC$ is a linear combination of the columns of $A$. (easy)
4. The column space of $AB$ is contained in the column space of $A$. (follows from above) [Or $colsp(AB) = rowsp((AB)^T) = rowsp(B^TA^T) = rowsp(A^T) = colsp(A)$]

## Cramer's Rule

Let the linear system $Ax = b$ have the same number of equations as the unknowns.

Let $D = |A|$, as discussed before the system $Ax = b$ has unique soln iff $rank(A) = n$ i.e. iff $D \neq 0$ and in this case soln is given by $x_i = \frac{D_i}{D}$ where $D_i$ is the determinant obtained from $D$ by replacing in $D$ the $i$th column by the column with entries $b_1, \dots, b_n$.

Hence if system is homogeneous and $D \neq 0$, it has only the trivial soln $x_i = 0$. If $D = 0$, the homogeneous system also has nontrivial solns.



## Sums and Direct Sums

Let $U$ and $W$ be subsets of a vector space $V$. The sum of $U$ and $W$, written $U + W$, consists of all sums $u+w$ where $u \in U$ and $w \in W$. That is,

$U+W=\\{v : v=u+w, \text { where } u \in U \text { and } w \in W\\}$

Now suppose $U$ and $W$ are subspaces of $V$. Then one can easily show that

1. $U + W$ is a subspace of $V$.
2. $U$ and $W$ are contained in $U + W$.
3. $U + W$ is the smallest subspace containing $U$ and $W$; that is, $U + W = span(U, W)$.
4. $W + W = W$

---

**Theorem:** Suppose $U$ and $W$ are finite-dimensional subspaces of a vector space $V$. Then $U + W$ has finite dimension and

$\operatorname{dim}(U+W)=\operatorname{dim} U+\operatorname{dim} W-\operatorname{dim}(U \cap W)$

**Proof:** Observe that $U \cap W$ is a subspace of both $U$ and $W$. Suppose $dim (U) = m, dim (W) = n, dim(U \cap W) = r$. Suppose $\\{v_1, \dots , v_r\\}$ is a basis of $U \cap W$. Thus, we can extend $\\{v_i\\}$ to a basis of $U$ and to a basis of $W$; say

$\left\\{v_{1}, \ldots, v_{r}, u_{1}, \dots, u_{m-r}\right\\} \quad$ and $\quad\left\\{v_{1}, \dots, v_{r}, w_{1}, \ldots, w_{n-r}\right\\}$

are bases of $U$ and $W$, respectively. Let

$B=\left\\{v_{1}, \ldots, v_{r}, u_{1}, \ldots, u_{m-r}, w_{1}, \ldots, w_{n-r}\right\\}$

Note that $B$ has exactly $m + n - r$ elements. Thus, the theorem is proved if we can show that $B$ is a basis of $U + W$. Because $\\{v_i, u_j\\}$ spans $U$ and $\\{v_i, w_k\\}$ spans $W$, the union $B = \\{v_i, u_j, w_k\\}$ spans $U + W$. Thus, it suffices to show that $B$ is independent. Suppose,

$a_{1} v_{1}+\cdots+a_{r} v_{r}+b_{1} u_{1}+\cdots+b_{m-r} u_{m-r}+c_{1} w_{1}+\cdots+c_{n-r} w_{n-r}=0 \tag{1}$

where $a_i, b_j, c_k$ are scalars. Let

$v=a_{1} v_{1}+\cdots+a_{r} v_{r}+b_{1} u_{1}+\cdots+b_{m-r} u_{m-r} \tag{2}$

By (1) we also have $v=-c_{1} w_{1}-\cdots-c_{n-r} w_{n-r} \tag{3}$

Because $\\{v_i, u_j\\} \subseteq U, v \in U$ by (2); and as $\\{w_k\\} \subseteq W, v \in W$ by (3). Accordingly, $v \in U \cap W$. Now $\\{v_i\\}$ is a basis of $U \cap W$, and so there exist scalars $d_1, \dots , d_r$ for which $v = d_1v_1 + \dots + d_rv_r$. Thus, by (3), we have

$d_{1} v_{1}+\cdots+d_{r} v_{r}+c_{1} w_{1}+\cdots+c_{n-r} w_{n-r}=0$

But $\\{v_i, w_k\\}$ is a basis of $W$, and so is independent. Hence, the above equation forces $c_1 = 0, \dots , c_{n-r} = 0$. Substituting this into (1), we obtain

$a_{1} v_{1}+\cdots+a_{r} v_{r}+b_{1} u_{1}+\cdots+b_{m-r} u_{m-r}=0$

But $\\{v_i, u_j\\}$ is a basis of $U$, and so is independent. Hence, the above equation forces

$a_1 = 0, \ldots, a_{r}=0, b_{1}=0, \ldots, b_{m-r}=0$

Because (1) implies that the $a_i, b_j, c_k$ are all 0, $B = \\{v_i, u_j, w_k\\}$ is independent, and the theorem is proved.

---

**Example:** Let $V = M_{2,2}$, the vector space of $2 \times 2$ matrices. Let $U$ consist of those matrices whose second
row is zero, and let $W$ consist of those matrices whose second column is zero. Then

$U=\left\\{\left[\begin{array}{ll}{a} & {b} \\\ {0} & {0}\end{array}\right]\right\\}, \quad W=\left\\{\left[\begin{array}{ll}{a} & {0} \\\ {c} & {0}\end{array}\right]\right\\}$ and

$U+W=\left\\{\left[\begin{array}{ll}{a} & {b} \\\ {c} & {0}\end{array}\right]\right\\}, \quad U \cap W=\left\\{\left[\begin{array}{ll}{a} & {0} \\\ {0} & {0}\end{array}\right]\right\\}$

$\operatorname{dim}(U+W)=\operatorname{dim} U+\operatorname{dim} V-\operatorname{dim}(U \cap W)=2+2-1=3$

- Consider the following subspaces of $R^5$

  $U=\operatorname{span}\left(u_{1}, u_{2}, u_{3}\right)=\operatorname{span}\{(1,3,-2,2,3), \quad(1,4,-3,4,2), \quad(2,3,-1,-2,9)\}$

  $W=\operatorname{span}\left(w_{1}, w_{2}, w_{3}\right)=\operatorname{span}\{(1,3,0,2,1), \quad(1,5,-6,6,3), \quad(2,5,3,2,1)\}$

  Find a basis and the dimension of (a) $U + W$, (b) $U \cap W$

  ***

  (a) $U + W$ is the space spanned by all six vectors. Hence, form the matrix whose rows are the given six
  vectors, and then row reduce to echelon form:

  $\left[\begin{array}{rrrrr}{1} & {3} & {-2} & {2} & {3} \\\ {1} & {4} & {-3} & {4} & {2} \\\ {2} & {3} & {-1} & {-2} & {9} \\\ {1} & {3} & {0} & {2} & {1} \\\ {1} & {5} & {-6} & {6} & {3} \\\ {2} & {5} & {3} & {2} & {1}\end{array}\right] \sim\left[\begin{array}{rrrrr}{1} & {3} & {-2} & {2} & {3} \\\ {0} & {1} & {-1} & {2} & {-1} \\\ {0} & {-3} & {3} & {-6} & {3} \\\ {0} & {0} & {2} & {0} & {-2} \\\ {0} & {2} & {-4} & {4} & {0} \\\ {0} & {-1} & {7} & {-2} & {-5}\end{array}\right] \sim\left[\begin{array}{rrrrr}{1} & {3} & {-2} & {2} & {3} \\\ {0} & {1} & {-1} & {2} & {-1} \\\ {0} & {0} & {1} & {0} & {-1} \\\ {0} & {0} & {0} & {0} & {0} \\\ {0} & {0} & {0} & {0} & {0} \\\ {0} & {0} & {0} & {0} & {0}\end{array}\right]$

  The following three nonzero rows of the echelon matrix form a basis of $U + W$:

  $(1,3,-2,2,2,3), \quad(0,1,-1,2,-1), \quad(0,0,1,0,-1)$

  Thus, $\operatorname{dim}(U + W) = 3$

  (b) Let $v = (x, y, z, s, t)$ denote an arbitrary element in $R^5$. First find, like before, homogeneous
  systems whose solution sets are $U$ and $W$, respectively.
  Let $M$ be the matrix whose columns are the $u_i \text{ and } v$, and reduce $M$ to echelon form:

  $M=\left[\begin{array}{rrrr}{1} & {1} & {2} & {x} \\\ {3} & {4} & {3} & {y} \\\ {-2} & {-3} & {-1} & {z} \\\ {2} & {4} & {-2} & {s} \\\ {3} & {2} & {9} & {t}\end{array}\right] \sim\left[\begin{array}{rrrr}{1} & {1} & {2} & {x} \\\ {0} & {1} & {-3} & {-3 x+y} \\\ {0} & {0} & {0} & {-x+y+z} \\\ {0} & {0} & {0} & {4 x-2 y+s} \\\ {0} & {0} & {0} & {-6 x+y+t}\end{array}\right]$

  That implies:

  $-x+y+z=0, \quad 4 x-2 y+s=0, \quad-6 x+y+t=0$

  Similarly,

  $M^{\prime}=\left[\begin{array}{rrrr}{1} & {1} & {2} & {x} \\\ {3} & {5} & {5} & {y} \\\ {0} & {-6} & {3} & {z} \\\ {2} & {6} & {2} & {s} \\\ {1} & {3} & {1} & {t}\end{array}\right] \sim\left[\begin{array}{rrrr}{1} & {1} & {2} & {x} \\\ {0} & {2} & {-1} & {-3 x+y} \\\ {0} & {0} & {0} & {-9 x+3 y+z} \\\ {0} & {0} & {0} & {4 x-2 y+s} \\\ {0} & {0} & {0} & {2 x-y+t}\end{array}\right]$

  That implies:

  $-9+3+z=0, \quad 4 x-2 y+s=0, \quad 2 x-y+t=0$

  Combine both of the above systems to obtain a homogeneous system, whose solution space is $U \cap W$, and
  reduce the system to echelon form, yielding

  $-x+y+z=0$
  $2 y+4 z+s=0$
  $8 z+5 s+2 t=0$
  $s-2 t=0$

  There is one free variable, which is $t$; hence, $dim(U \cap W) = 1$. Setting $t = 2$, we obtain the solution $u = (1, 4, -3, 4, 2)$, which forms our required basis of $U \cap W$

  :::caution IMP Note
  Here we can't just reduce $A = \begin{bmatrix} u_1 \\\ u_2 \\\ u_3 \end{bmatrix}$ to row canonical matrix $R_1$ and $B = \begin{bmatrix} w_1 \\\ w_2 \\\ w_3 \end{bmatrix}$ to row canonical matrix $R_2$ and take common rows in two to find basis of $U \cap W$ as common elements can be linear combination of the rows in $R_1$!
  :::

- Suppose $U$ and $W$ are distinct four-dimensional subspaces of a vector space $V$, where $\operatorname{dim} V = 6$. Find the possible dimensions of $U \cap W$.

  Because $U$ and $W$ are distinct, $U + W$ properly contains $U$ and $W$; consequently, $dim(U + W) > 4$.
  But $dim(U + W)$ cannot be greater than 6, as $\operatorname{dim} V = 6$. Hence, we have two possibilities:

  1. $dim(U + W) = 5$ and thus $dim(U \cap W) = 3$
  2. $dim(U + W) = 6$ and thus $dim(U \cap W) = 2$

## Direct Sums

The vector space $V$ is said to be the direct sum of its subspaces $U$ and $W$, denoted by

$V=U \oplus W$

if every $v \in V$ can be written in one and only one way as $v = u + w$ where $u \in U$ and $w \in W$.

**Theorem:** The vector space $V$ is the direct sum of its subspaces $U$ and $W$ if and only if:

$\text { (i) } V=U+W,(\text { ii) } U \cap W=\\{0\\}$ (easy to prove)

## General Direct Sums

$V$ is the direct sum of subspaces $W_1, W_2, \dots , W_r$, written $V=W_{1} \oplus W_{2} \oplus \cdots \oplus W_{r}$

if every vector $v \in V$ can be written in one and only one way as

$v=w_{1}+w_{2}+\cdots+w_{r}$

$\text { where } w_{1} \in W_{1}, w_{2} \in W_{2}, \ldots, w_{r} \in W_{r}$

**Theorem:** Suppose $V=W_{1} \oplus W_{2} \oplus \cdots \oplus W_{r}$. Also, for each $k$, suppose $S_k$ is a linearly independent subset of $W_k$. Then

$\text { (a) The union } S=\cup_{k} S_{k} \text { is linearly independent in } V$ (easy to prove as, if they are linearly dependent then one side is a linear combination of $S_1$ (which would imply coefficients on left side are 0 and so on...))

$\text { (b) If each } S_{k} \text { is a basis of } W_{k}, \text { then } \bigcup_{k} S_{k} \text { is a basis of } V$ (follows from (a))

$\text { (c) } \operatorname{dim} V=\operatorname{dim} W_{1}+\operatorname{dim} W_{2}+\cdots+\operatorname{dim} W_{r}$ (follows from (b))

**Theorem:** $\text { Suppose } V=W_{1}+W_{2}+\cdots+W_{r} \text { and } \operatorname{dim} V=\sum_{k} \operatorname{dim} W_{k} . \text { Then }$

$V=W_{1} \oplus W_{2} \oplus \cdots \oplus W_{r}$

## Coordinates

Let $V$ be an $n$-dimensional vector space over $K$ with basis $S = \\{u_1, u_2, \dots , u_n\\}$. Then any vector $v \in V$ can be expressed uniquely as a linear combination of the basis vectors in $S$ (this is a theorem for basis which is easy to prove), say $v = a_1u_1 + a_2u_2 + \dots + a_nu_n$ These $n$ scalars $a_1, a_2, \dots , a_n$ are called the coordinates of $v$ relative to the basis $S$, and they form a vector $[a_1, a_2, \dots , a_n]$ in $K^n$ called the coordinate vector of $v$ relative to $S$. We denote this vector by $[v]_S$, or
simply $[v]$, when $S$ is understood.

- In the space $M = M_{2,3}$, determine whether or not the following matrices are linearly dependent:

  $A=\left[\begin{array}{lll}{1} & {2} & {3} \\\ {4} & {0} & {5}\end{array}\right], \quad B=\left[\begin{array}{lll}{2} & {4} & {7} \\\ {10} & {1} & {13}\end{array}\right], \quad C=\left[\begin{array}{lll}{1} & {2} & {5} \\\ {8} & {2} & {11}\end{array}\right]$

  If the matrices are linearly dependent, find the dimension and a basis of the subspace $W$ of $M$ spanned by the matrices

  The coordinate vectors of the above matrices relative to the usual basis of $M$ are as follows:

  $[A]=[1,2,3,4,0,5], \quad[B]=[2,4,7,10,1,13], \quad[C]=[1,2,5,8,2,11]$

  $M=\left[\begin{array}{cccccc}{1} & {2} & {3} & {4} & {0} & {5} \\\ {2} & {4} & {7} & {10} & {1} & {13} \\\ {1} & {2} & {5} & {8} & {2} & {11}\end{array}\right] \sim\left[\begin{array}{cccccc}{1} & {2} & {3} & {4} & {0} & {5} \\\ {0} & {0} & {1} & {2} & {1} & {3} \\\ {0} & {0} & {0} & {0} & {0} & {0}\end{array}\right]$

  Because the echelon matrix has only two nonzero rows, the coordinate vectors $[A], [B], [C]$ span a space of
  dimension two, and so they are linearly dependent. Thus, $A, B, C$ are linearly dependent. Furthermore,
  $\operatorname{dim} W = 2$, and the matrices

  $w_{1}=\left[\begin{array}{lll}{1} & {2} & {3} \\\ {4} & {0} & {5}\end{array}\right] \quad$ and $\quad w_{2}=\left[\begin{array}{lll}{0} & {0} & {1} \\\ {2} & {1} & {3}\end{array}\right]$

  corresponding to the nonzero rows of the echelon matrix form a basis of $W$.
