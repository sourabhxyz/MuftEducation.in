---
id: lseq
title: Linear System Of Equations
sidebar_label: Linear System Of Equations
---

## Matrix Multiplication

$c\_{jk} = a\_jb\_k$, where $a\_j$ is the $j$th row vector of $A$ and $b\_k$ is the $k$th column vector of $B$

Using this matrix multiplication can be computed parallelly (product is computed column wise)

$AB = A[b\_1 b\_2 \dots b\_p] = [Ab\_1 Ab\_2 \dots Ab\_p]$

## Motivation of Multiplication by Linear Transformation

Suppose $x\_1x\_2$-coordinate system is related to a $y\_1y\_2$-coordinate system as

$y = \begin{bmatrix} y\_1 \\\ y\_ 2 \end{bmatrix} = \begin{bmatrix} a\_{11}x\_1 + a\_{12}x\_2 \\\ a\_{21}x\_1 + a\_{22}x\_2 \end{bmatrix} = \begin{bmatrix}a_{11} & a_{12} \\\ a_{21} & a_{22}\end{bmatrix} \begin{bmatrix} x_1 \\\ x_2 \end{bmatrix} = Ax$

Now suppose further that the $x_1x_2$-system is related to a $w_1w_2$-system by another linear Transposition, say, 

$x = Bw$ 

Then $y$ is related to $w$ as $y = ABw$.

## Transposition properties

* $(A^T)^T = A$
* $(A + B)^T = A^T + B^T$
* $(cA)^T = c(A)^T$
* $(AB)^T = B^TA^T$   *--> This prop. can be extended* 

## Complex Conjugate

$\bar{A} = [\bar{a_{ij}}]$

## Special Matrices

* Symmetric: $A^T = A$
* Skew-Symmetric: $A^T = -A$
* Upper Triangular: $a_{ij} = 0$ if $i > j$
* Lower Triangular: $a_{ij} = 0$ if $j > i$
* Hermitian: $\bar{A^T} = A$, *i.e., equal to conjugate transpose*
* Skew-Hermitian: $\bar{A^T} = -A$
* Scalar: $S = cI$