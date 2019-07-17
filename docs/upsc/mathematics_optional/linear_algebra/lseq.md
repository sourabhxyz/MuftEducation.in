---
id: lseq
title: Linear System Of Equations And Rank Of Matrix
sidebar_label: Linear System Of Equations And Rank Of Matrix
---

<!-- Some Latex Commands (doesn't work as of now) -->

<!-- Bold Text -->

<!-- $\newcommand{\bt}[1]{\textbf{#1}}$ -->

<!-- Italic Text -->

<!-- $\newcommand{\it}[1]{\textit{#1}}$ -->

<!-- End -->

## Intro

A linear system of $m$ equations in $n$ unknowns $x_1, \dots , x_n$ is a set of equations of the form

$a_{11}x_1 + \dots + a_{1n}x_n = b_1$

$a_{21}x_1 + \dots + a_{2n}x_n = b_2$

$a_{m1}x_1 + \dots + a_{mn}x_n = b_m$

The system is called linear because each variable $x_j$ appears in the first power only. If all the $b_j$ are zero, then this is called a homogeneous system o/w nonhomogeneous.

For a homogeneous system we always have trivial soln: $x_i = 0$

This system can be represented as $Ax = b$, $a_{ij}$ are called coefficients and thus $A$ is called coefficient matrix.

$\tilde{A} = 
\begin{bmatrix} 
  a_{11} & \dots & a_{1n} & | & b_1 \\\ 
  . & \dots & . & | & . \\\  
  . & \dots & . & | & . \\\  
  a_{m1} & \dots & a_{mn} & | & b_m 
\end{bmatrix}$ _--> is called Augmented Matrix, it determines the system completely_

## Elementary Row Operations

- Interchange of two rows
- Addition of a constant multiple of one row to another row
- Multiplication of a row by a **nonzero** constant c

Similarly we have **Elementary Column Operations**

We now call a linear system $S_1$ row-equivalent to a linear system $S_2$ if $S_1$ can be obtained from $S_2$ by (finitely many!) row operations (observe that it is an equivalence relation).

**Theorem**: Row-equivalent linear systems have the same set of solutions (Obviously as each of these operations when applied to equations doesn't change the soln set).

Note well that we are dealing with row operations, No column operations on the augmented matrix are permitted in this context because they would generally alter the soln set.

A system is called consistent if it has at least one solution (thus, one solution or infinitely many solutions), but inconsistent if it has no solutions at all.

## Elementary Matrix

Matrix which differs from Identity Matrix by one single elementary row operation. Left multiplication (pre-multiplication) by an elementary matrix represents elementary row operation, while right multiplication (post - multiplication) represents elementary column operations.

- $E_{ij}$, $E_i(k)$ and $E_{ij}(k)$, denotes elementary matrix obtained by:
  - swapping rows $i$ and $j$
  - multiplying $i$th row with non zero $k$
  - adding to the $i$th row the constant multiple ($k$) of the $j$th row, resp.
  - Clearly $E_{ij}^{-1} = E_{ij}$, $E_i(k)^{-1} = E_i(\frac{1}{k})$ and $E_{ij}(k)^{-1} = E_{ij}(-k)$ thus inverse of an elementary matrix is also an elementary matrix.
- $|E_{ij}| = -1$
- $|E_{i}(k)| = k$
- $|E_{ij}(k)| = 1$
- Thus elementary matrix is always non singular

## Row Echelon Form

For each row in a matrix, if the row does not consist of only zeros, then the leftmost nonzero entry is called the leading coefficient (or pivot) of that row. So if two leading coefficients are in the same column, then a row operation of type 3 could be used to make one of those coefficients zero. Then by using the row swapping operation, one can always order the rows so that for every non-zero row, the leading coefficient is to the right of the leading coefficient of the row above. If this is the case, then matrix is said to be in row echelon form.

## Reduced Row Echelon Form

A matrix is in reduced row echelon form (also called row canonical form, row reduced echelon form) if it satisfies the following conditions:

- It is in row echelon form.
- The leading entry in each nonzero row is a 1 (called a leading 1).
- Each column containing a leading 1 has zeros everywhere else (i.e. also in above).

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

## Inverse of the matrix by Gauss-Jordan Method

Task is to find $A^{-1}$. I.e. to find $X$ s.t. $AX = I$. Make an augmented matrix $\tilde{A} = [A \text{  } I]$ Now reduce it Reduced Row Echelon form to get $[I \text{  } H]$ since this corresponds to $IX = H$, thus $X = H$.

From this analysis we observe that $A^{-1}$ is simply the result of elementary row operations and thus is product of elementary matrices therefore $A$ is as well the product of elementary matrices.

**Examples:**

- Find two non-singular matrices P and Q s.t. PAQ is in the normal (canonical) form (i.e. of the form $\begin{bmatrix} I_r & O \\\ O & O \end{bmatrix}$) where $A = \begin{bmatrix} 1 & 1 & 1 \\\ 1 & -1 & -1 \\\ 3 & 1 & 1\end{bmatrix}$

  For series of row operations $r_1, r_2, ...$ applied, apply them to $I$ to get $R$, similarly for any column operation applied in between, apply it to another $I$ to get $C$, now $P = R, Q = C$. Obv. $P$ and $Q$ aren't unique.

  :::tip Info
  It is observed that authors club row and column equivalent together to define **equivalent** (which is of course an equivalence relation) matrices which are obtained from each other via combination of elementary row and column operations. Thus, above example shows that any matrix is equivalent to this **normal** form.

  From above it follows that if $A$ and $B$ are of same order (i.e. same dimension) and of same rank then they are equivalent to each other.
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

Proof is simple, suppose we have two matrices $A$ and $B$ each of rank say $p, q$ resp. then it's possible to transform $A$ into $[G \text{  } O]$ where $G$ has only $p$ non zero rows at top, by left multiplication by $P$. Similarly it is possible to transform $B$ into $H$ where $H$ has only $q$ non zero columns at left, by right multiplication by $Q$. Now since $P, Q$ are result of elementary matrices that implies $rank(AB) = rank(PGHQ) = rank (GH)$ which is $\leq min(p, q)$

## Cramer's Rule

Let the linear system $Ax = b$ have the same number of equations as the unknowns.

Let $D = |A|$, as discussed before the system $Ax = b$ has unique soln iff $rank(A) = n$ i.e. iff $D \neq 0$ and in this case soln is given by $x_i = \frac{D_i}{D}$ where $D_i$ is the determinant obtained from $D$ by replacing in $D$ the $i$th column by the column with entries $b_1, \dots, b_n$.

Hence if system is homogeneous and $D \neq 0$, it has only the trivial soln $x_i = 0$. If $D = 0$, the homogeneous system also has nontrivial solns.
