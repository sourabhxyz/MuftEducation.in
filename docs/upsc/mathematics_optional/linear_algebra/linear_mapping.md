---
id: linear_mapping
title: Linear Mappings
sidebar_label: Linear Mappings
---

## Matrix Mappings

Let $A$ be any $m \times n$ matrix over $K$. Then $A$ determines a mapping $F_{A} : K^{n} \rightarrow K^{m}$ by

$F_{A}(u)=A u$

where the vectors in $K_n$ and $K_m$ are written as columns.

For notational convenience, we will frequently denote the mapping $F_A$ by the letter $A$, the
same symbol as used for the matrix.

## Linear Mappings (Linear Transformations)

---

Let $V$ and $U$ be vector spaces over the same field $K$. A mapping $F : V \rightarrow U$ is called a
linear mapping or linear transformation if it satisfies the following two conditions:

1. For any vectors $v, w \in V, F(v+w)=F(v)+F(w)$
2. For any scalar $k$ and vector $v \in V, F(k v)=k F(v)$

---

Substituting $k = 0$ into condition (2), we obtain $F(0) = 0.$ Thus, every linear mapping takes the zero
vector into the zero vector.

For any scalars $a_i \in K$ and any vectors $v_i \in V$, we obtain the following basic property of
linear mappings:

$F\left(a_{1} v_{1}+a_{2} v_{2}+\cdots+a_{m} v_{m}\right)=a_{1} F\left(v_{1}\right)+a_{2} F\left(v_{2}\right)+\cdots+a_{m} F\left(v_{m}\right)$

---

**Remark:** A linear mapping $F : V \rightarrow U$ is completely characterized by the condition

$F(a v+b w)=a F(v)+b F(w)$

---

---

**Theorem 4.1:** Let $V$ and $U$ be vector spaces over a field $K$. Let $\\{v_1, v_2, \dots , v_n\\}$ be a basis of $V$ and let $u_1, u_2, \dots , u_n$ be any vectors in $U$. Then there exists a unique linear mapping
$F : V \rightarrow U$ such that $F(v_1) = u_1, F(v_2) = u_2, \dots , F(v_n) = u_n$.

Note that the vectors $u_1, u_2, \dots , u_n$ are completely arbitrary; they may be linearly dependent or they may even be equal to each other.

**Proof:**
Consider $v=a_{1} v_{1}+a_{2} v_{2}+\cdots+a_{n} v_{n}$

Define $F(v)=a_{1} u_{1}+a_{2} u_{2}+\cdots+a_{n} u_{n}$

Suppose $G : V \rightarrow U$ is linear and $G\left(v_{1}\right)=u_{i}, i=1, \ldots, n .$ Let

Then

$G(v)=G\left(a_{1} v_{1}+a_{2} v_{2}+\cdots+a_{n} v_{n}\right)=a_{1} G\left(v_{1}\right)+a_{2} G\left(v_{2}\right)+\cdots+a_{n} G\left(v_{n}\right)$

$=a_{1} u_{1}+a_{2} u_{2}+\cdots+a_{n} u_{n}=F(v)$

Because $G(v)=F(v)$ for every $v \in V, G=F .$ Thus, $F$ is unique and the theorem is proved.

---

## Matrices as Linear Mappings

$\begin{aligned} F_{A}(v+w) &=A(v+w)=A v+A w=F_{A}(v)+F_{A}(w) \\\ F_{A}(k v) &=A(k v)=k(A v)=k F_{A}(v) \end{aligned}$

In other words, using $A$ to represent the mapping, we have,

$A(v+w)=A v+A w \quad$ and $\quad A(k v)=k(A v)$

## Vector Space Isomorphism

Two vector spaces $V$ and $U$ over $K$ are isomorphic, written $V \cong U$, if there exists a bijective (one-to-one and onto) linear mapping $F : V \rightarrow U$. The mapping $F$ is then called an isomorphism between $V$ and $U$.

Consider any vector space $V$ of dimension $n$ and let $S$ be any basis of $V$. Then the mapping

$v \mapsto[v]_{S}$

which maps each vector $v \in V$ into its coordinate vector $[v]_S$, is an isomorphism between $V$ and $K^n$

## Kernal and Image of a Linear Mapping

Let $F : V \rightarrow U$ be a linear mapping. The kernel of $F$, written $\operatorname{Ker} F$, is:

$\operatorname{Ker} F=\\{v \in V : F(v)=0\\}$

And image or range of $F$ is defined as:

$\operatorname{Im} F=\\{u \in U : \text { there exists } v \in V \text { for which } F(v)=u\\}$

---

**Theorem 4.2** Let $F : V \rightarrow U$ be a linear mapping. Then the kernel of $F$ is a subspace of $V$ and the image of $F$ is a subspace of $U$. (easy to see)

---

---

**Theorem 4.3** Suppose $v_1, v_2, \dots , v_m$ span a vector space $V$, and suppose $F : V \rightarrow U$ is linear. Then $F(v_1), F(v_2), \dots , F(v_m)$ span $\operatorname{Im} F$. (easy to see)

Thus one can either use this, or theorem 4.4 to find the dimension of $\operatorname{Im} F$

---

**Examples:**

- Let $F : R^3 \rightarrow R^3$ be the projection of a vector $v$ into the $xy$-plane that is, $F(x, y, z) = (x, y, 0)$ Clearly the image of $F$ is the entire $xy$-plane—that is, points of the form $(x, y, 0)$. Moreover, the kernel of $F$ is the $z$-axis—that is, points of the form $(0, 0, c)$.

## Kernal and Image of Matrix Mappings

Let $A$ by any $m \times n$ matrix over a field $K$ viewed as a linear map $A : K^n \times K^m$. Then

1. $\operatorname{Im} A=\operatorname{colsp}(A)$ as consider usual basis $e_i$ of $K^n$, $Ae_1, Ae_2, \dots, Ae^n$ are respectively the columns of $A$.
2. Kernel of $A$ consists of all vectors $v$ for which $Av = 0$. This means that the kernel of $A$ is the solution space of the homogeneous system $AX = 0$, called the null space of A.

If we have computed the dimension of column space, which is same as rank of the matrix, $r$. And hence the dimension of kernal of $A$ is $n - r$.

**Examples:**

- Find a linear map $F : R^3 \rightarrow R^4$ whose image is spanned by $(1, 2, 0, -4)$ and $(2, 0, 1, -3)$.

  $u = (x + 2y, 2x, -y, -4x - 3y)$

  $\therefore A=\left[\begin{array}{rrr}{1} & {2} & {2} \\\ {2} & {0} & {0} \\\ {0} & {-1} & {-1} \\\ {-4} & {-3} & {-3}\end{array}\right]$

  Also recall that $A$ determines a linear map $A : R^3 \rightarrow R^4$ whose image is spanned by the columns of $A$. Thus, $A$ satisfies the required condition

## Rank and Nullity of a Linear Mapping

Let $F : V \rightarrow U$ be a linear mapping.

$\operatorname{rank}(F)=\operatorname{dim}(\operatorname{Im} F) \quad$ and $\quad$ nullity $(F)=\operatorname{dim}(\operatorname{Ker} F)$

**Theorem 4.4** Let $V$ be of finite dimension, and let $F : V \rightarrow U$ be linear. Then

$\operatorname{dim} V=\operatorname{dim}(\operatorname{Ker} F)+\operatorname{dim}(\operatorname{Im} F)=$ nullity $(F)+\operatorname{rank}(F)$

## Singular and Nonsingular Linear Mappings, Isomorphisms

Let $F : V \rightarrow U$ be a linear mapping. Recall that $F(0) = 0$. $F$ is said to be singular if the image of some nonzero vector $v$ is $0$. Thus, $F : V \rightarrow U$ is nonsingular if the zero vector $0$ is the only vector whose image under $F$ is $0$ or, in other words, if $\operatorname{Ker} F = \\{0\\}$

---

**Theorem 4.5:** Let $F : V \rightarrow U$ be a nonsingular linear mapping. Then the image of any linearly independent set is linearly independent.

---

---

**Theorem 4.6:** A linear mapping $F : V \rightarrow U$ is one-to-one if and only if $F$ is nonsingular. (easy to see)

---

---

**Theorem 4.7:** Suppose $V$ has finite dimension and $dim V = dim U$. Suppose $F : V \rightarrow U$ is linear. Then $F$ is an isomorphism if and only if $F$ is nonsingular.

---

## Operations with Linear Mappings

Let $F : V \rightarrow U$ and $G : V \rightarrow U$ be linear mappings over a field $K$. The sum $F + G$ and the scalar product $kF$, where $k \in K$, are defined to be the following mappings from $V$ into $U$:

$(F+G)(v) \equiv F(v)+G(v) \quad$ and $\quad(k F)(v) \equiv k F(v)$

It is easy to see that if $F$ and $G$ are linear, then $F + G$ and $kF$ are also linear.

---

**Theorem 4.8:** Let $V$ and $U$ be vector spaces over a field $K$. Then the collection of all linear mappings from $V$ into $U$ with the above operations of addition and scalar multiplication forms a vector space over $K$.

---

## TODO

Left 5.21
