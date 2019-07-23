---
id: basic
title: Basics and Linear System Of Equations (LSEQ) Intro
sidebar_label: Basics and Linear System Of Equations (LSEQ) Intro
---

If not mentioned, consider dimension of matrix $A$ to be $m$ x $n$

## Matrix Multiplication

$c_{jk} = a_jb_k$, where $a_j$ is the $j$th row vector of $A$ and $b_k$ is the $k$th column vector of $B$

Using this matrix multiplication can be computed parallelly (product is computed column wise)

$AB = A[B_1 B_2 \dots B_p] = [AB_1 AB_2 \dots AB_p] = \begin{bmatrix}A_1 \\\ \vdots \\\ A_m\end{bmatrix}B = \begin{bmatrix}A_1B \\\ \vdots \\\ A_mB\end{bmatrix}$

- Matrix multiplication is associative.

## Motivation of Multiplication by Linear Transformation

Suppose $x_1x_2$-coordinate system is related to a $y_1y_2$-coordinate system as

$y = \begin{bmatrix} y_1 \\\ y_ 2 \end{bmatrix} = \begin{bmatrix} a_{11}x_1 + a_{12}x_2 \\\ a_{21}x_1 + a_{22}x_2 \end{bmatrix} = \begin{bmatrix}a_{11} & a_{12} \\\ a_{21} & a_{22}\end{bmatrix} \begin{bmatrix} x_1 \\\ x_2 \end{bmatrix} = Ax$

Now suppose further that the $x_1x_2$-system is related to a $w_1w_2$-system by another linear Transposition, say,

$x = Bw$

Then $y$ is related to $w$ (which if you go by substitution of variables) as $y = ABw$.

## Transposition properties

- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(cA)^T = c(A)^T$
- $(AB)^T = B^TA^T$ _--> This prop. can be extended_

## Complex Conjugate

$\bar{A} = [\bar{a_{ij}}]$

- $\overline{kA} = \bar{k}\bar{A}$
- $\overline{AB} = \bar{A}\bar{B}$
- $\overline{A^T} = \bar{A}^T$ (Obvious), and $\overline{A^T}$ is also denoted simply as $A^{\theta}$
- $(AB)^{\theta} = B^{\theta}A^{\theta}$
- $(kA)^{\theta} = \bar{k}A^{\theta}$

## Special Square Matrices

All these are defined solely for **square** matrices.

- Symmetric: $A^T = A$
- Skew-Symmetric: $A^T = -A$ so diagonal elements must be zero (diagonal is defined only for square matrices).
- Upper Triangular: $a_{ij} = 0$ if $i > j$
- Lower Triangular: $a_{ij} = 0$ if $j > i$
- Hermitian: $\overline{A^T} = A$, _i.e., equal to conjugate transpose_ (Thus elements in diagonal must be real)
- Skew-Hermitian: $\overline{A^T} = -A$
- Scalar: $S = cI$
- Orthogonal: $A^{T}A = I$ (thus $|A| \neq 0 (= \pm 1)$ and $A^{-1} = A^{T}$)
- Unitary: $A^{\theta}A = I$ (thus $|A| \neq 0 (= e^{it} \text{ as } \overline{|A|}|A| = ||A||^2 = 1$ and $A^{-1} = A^{\theta}$)
- Involutory: $A^2 = I$
- Nilpotent: Square matrix $A$ such that there exist some positive integer $n$ for which $A^n = O$. Such a smallest positive integer is called an index.
- Idempotent: $A^2 = A$
- Singular: $|A| = 0$ o/w non singular

## Trace

- $tr(AB) = tr(BA)$ (easy to prove)

## Determinant

- $(-1)^{i + j}M_{ij} = C_{ij}$
- Determinant (which is defined only for square matrix) remains the same when expanded along any row or column.
- $|A| = |A^T|$
- $|AB| = |A||B|$ So if $|AB| = 0 \rightarrow |A| = 0 \text{ or } |B| = 0$

  $AB = O \text{ doesn't imply } A = O \text{ or } B = O$ but that atleast one of them is singular.

- Swapping any 2 rows or any 2 columns multiplies the determinant by -1
- $\begin{bmatrix} ka_1 & b_1 & c_1 \\\ ka_2 & b_2 & c_2 \\\ ka_3 & b_3 & c_3 \end{bmatrix} = k\begin{bmatrix} a_1 & b_1 & c_1 \\\ a_2 & b_2 & c_2 \\\ a_3 & b_3 & c_3 \end{bmatrix}$
- $\begin{bmatrix} ka_1 & kb_1 & kc_1 \\\ a_2 & b_2 & c_2 \\\ a_3 & b_3 & c_3 \end{bmatrix} = k\begin{bmatrix} a_1 & b_1 & c_1 \\\ a_2 & b_2 & c_2 \\\ a_3 & b_3 & c_3 \end{bmatrix}$
- $|kA_{n}| = k^{n}|A_n|$
- If 2 rows (or 2 columns) are identical, then determinant is zero.
- Sum of the product of elements of any row (or column) with the cofactors of the corresponding elements of any other row (or column) is zero. Can be used to prove $Aadj(A) = |A|I$. (*Note*: Adjoint = $C^T$ where $C$ is the cofactor matrix)
- Adding a constant multiple of a row (or column) to another row (or colum) doesn't change the determinant.
- $|\bar{A}| = \overline{|A|}$ (Can be easily shown by induction or even otherwise as $\overline{a + cb} = \bar{a} + \bar{b}\bar{c}$)
- $|A^{\theta}| = \overline{|A|}$ ($|A^{\theta}| = |\bar{A^{T}}| = \overline{|A^T|} = \overline{|A|}$)
- Determinant of Hermitian is always a real number. To show: $|A| = \overline{|A|}$ i.e., to show $|A^{\theta}| = \overline{|A|}$, which is true.
- Similarly determinant of a skew hermitian matrix is always imaginary.
- Determinant of skew symmetric matrix of odd order is 0.

## Adjoint

$(adj(A))A = A(adj(A)) = |A|I \rightarrow A^{-1} = adj(A)/|A|$, as evident inverse is defined only for square matrices and exists iff $|A| \neq 0$.

- $adj(X) = |X|X^{-1}$
- $adj(AB) = adj(B)adj(A)$ (follows from above)
- $(A^{\theta})^{-1} = (A^{-1})^{\theta}$

  $A^{\theta}B = I \rightarrow B^{\theta}A = I$

  $\rightarrow B^{\theta} = A^{-1} \rightarrow B = (A^{-1})^{\theta}$

- $(A^{T})^{-1} = (A^{-1})^{T}$ (easy)
- $adj(kA) = k^{n - 1}adj(A)$ (as cofactor will consist of determinant of order $n - 1$)
- $adj(A^T) = adj(A)^{T}$ (proof omitted)
- If $A$ is symmetric then $adj(A)$ is symmetric.
- $|A^{-1}| = |A|^{-1}$ (easy, thus from this it follow $|adj(A)| = |C| = |A|^{n - 1}$)

## Linear System Of Equations Intro

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


## Side Problems

- If $P$ and $Q$ are non singular matrices then show that $\begin{bmatrix} P & O \\\ O & Q\end{bmatrix}^{-1} = \begin{bmatrix} P^{-1} & O \\\ O & Q^{-1} \end{bmatrix}$

  Let inverse be $\begin{bmatrix}A & B \\\ C & D\end{bmatrix}$

  $\rightarrow \begin{bmatrix} PA & PB \\\ QC & QD\end{bmatrix} = \begin{bmatrix}I & O \\\ O & I \end{bmatrix} \blacksquare$

