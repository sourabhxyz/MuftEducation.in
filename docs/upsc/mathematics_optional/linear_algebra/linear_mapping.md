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
