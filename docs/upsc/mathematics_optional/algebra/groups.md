---
id: groups
title: Groups
sidebar_label: Groups
---

## Definition

---

Let $G$ be a set together with a binary operation (usually called multiplication that assigns to each ordered pair $(a, b)$ of elements of $G$ an element in $G$ (known as closure condition) denoted by $a b .$ We say $G$ is a group under this operation if
the following three properties are satisfied.

1. Associativity. The operation is associative; that is, $(a b) c=a(b c)$ for all $a, b, c$ in $G .$
2. Identity. There is an element $e$ (called the identity) in $G$ such that $a e=e a=a$ for all $a$ in $G .$
3. Inverses. For each element $a$ in $G,$ there is an element $b$ in $G$ (called an inverse of $a$ ) such that $a b=b a=e$ .

---

Be sure to verify closure when testing for a group.

Notice that if $b$ is the inverse of $a$, then $a$ is the inverse of $b$.

If a group has the property that $ab = ba$ for every pair of elements $a$
and $b$, we say the group is Abelian. A group is non-Abelian if there is
some pair of elements $a$ and $b$ for which $ab \neq ba$.

**Examples:**

- The set of integers under ordinary multiplication is not a
  group. Since property 3 fails (number 1 is the identity).
- The set $A(S)$ of all one to one mappings of a non empty set $S$ onto itself is a group wrt the product of mappings (i.e. function compositions).
- The set $S$ of positive irrational numbers together with 1
  under multiplication satisfies the three properties given in the
  definition of a group but is not a group. Indeed,
  $\sqrt{2} * \sqrt{2} = 2$, so $S$ is not closed under multiplication.

- The set $Z_{n}=\\{0,1, \ldots, n-1\\}$ for $n \geq 1$ is a group
  under addition modulo $n .$ For any $j>0$ in $Z_{n},$ the inverse of $j$ is $n-j$ .
  This group is usually referred to as the group of integers modulo $n .$

- Note: An integer $a$ has a multiplicative inverse modulo $n$ if and only if $a$ and $n$ are relatively prime (easy to prove) . So, for each $n > 1$, we define $U(n)$ to be the set of all positive integers less than $n$ and relatively prime to $n$. Then $U(n)$ is a group under multiplication modulo $n$ (very important observation is that if $b$ is the multiplicative inverse of $a$ then $ab \bmod n = 1$, define $b \bmod n = k \rightarrow ak \bmod n = 1$ thus $k \in U(n)$). (Note that this set is closed under this operation (Proof: $at_1 + nt_2 = 1, bt_3 + nt_4 = 1 \Rightarrow abt_1t_3 + at_1nt_4 + nt_2bt_3 + n^2t_2t_4 \Rightarrow ab(..) + n(..) = 1$).) For $n = 10$, we have $U(10) = \\{1, 3, 7, 9\\}$.

- The set of integers under subtraction is not a group, since
  the operation is not associative.
- The set $\\{1, 2, \dots , n - 1\\}$ is a group under multiplication modulo $n$ if and only if $n$ is prime (as each element must possess an inverse).
- The set of all $2 \times 2$ matrices with determinant 1 with entries from $Q$ (rationals), $\mathbf{R}(\text { reals }), \mathbf{C}(\text { complex numbers }),$ or $Z_{p}(p \text { a prime) }$
is a non-Abelian group under matrix multiplication. This group is called
the special linear group of $2 \times 2$ matrices over $Q, \mathbf{R},$ or $Z_{p},$ respectively.
If the entries are from $F,$ where $F$ is any of the above, we denote this group
by $S L(2, F) .$ For the group $S L(2, F),$ the formula for the inverse of $\left[\begin{array}{cc}{a} & {b} \\\ {c} & {d}\end{array}\right]$ simplifies to $\left[\begin{array}{rr}{d} & {-b} \\\ {-c} & {a}\end{array}\right] .$ When the matrix
entries are from $Z_{p},$ we use modulo $p$ arithmetic to compute determinants, matrix products, and inverses. To illustrate the case $S L\left(2, Z_{5}\right)$ consider the element $A=\left[\begin{array}{cc}{3} & {4} \\\ {4} & {4}\end{array}\right] .$ Then det $A=(3 \cdot 4-4 \cdot 4) \bmod 5=$
$-4 \bmod 5=1,$ and the inverse of $A$ is $\left[\begin{array}{rr}{4} & {-4} \\\ {-4} & {3}\end{array}\right]=\left[\begin{array}{rr}{4} & {1} \\\ {1} & {3}\end{array}\right] .$ Note that $\left[\begin{array}{ll}{3} & {4} \\\ {4} & {4}\end{array}\right]\left[\begin{array}{ll}{4} & {1} \\\ {1} & {3}\end{array}\right]=\left[\begin{array}{ll}{1} & {0} \\\ {0} & {1}\end{array}\right]$ when the arithmetic is done modulo 5

- Let $F$ be any of $Q, \mathbf{R}, \mathbf{C},$ or $Z_{p}(p \text { a prime). The set }$ $G L(2, F)$ of all $2 \times 2$ matrices with nonzero determinants and entries
from $F$ is a non-Abelian group under matrix multiplication. When $F$ is $Z_{p},$ modulo $p$ arithmetic is used to calculate
determinants, matrix products, and inverses. The usual formula for the inverse of $\left[\begin{array}{cc}{a} & {b} \\\ {c} & {d}\end{array}\right]$ remains valid for elements from
$G L\left(2, Z_{p}\right),$ provided we interpret division by $a d-b c$ as multiplication
by the inverse of $(a d-b c)$ modulo $p .$ For example, in $G L\left(2, Z_{7}\right)$
consider $\left[\begin{array}{cc}{4} & {5} \\\ {6} & {3}\end{array}\right] .$ Then the determinant $(a d-b c) \bmod 7$ is $(12-30)$
$\bmod 7=-18 \bmod 7=3$ and the inverse of 3 is 5$[\operatorname{since}(3 \cdot 5))$
$\bmod 7=1 ] .$ So, the inverse of $\left[\begin{array}{cc}{4} & {5} \\\ {6} & {3}\end{array}\right]$ is $\left[\begin{array}{cc}{3 \cdot 5} & {2 \cdot 5} \\\ {1 \cdot 5} & {4 \cdot 5}\end{array}\right]=\left[\begin{array}{cc}{1} & {3} \\\ {5} & {6}\end{array}\right]$ [The reader should check that $\left[\begin{array}{cc}{4} & {5} \\\ {6} & {3}\end{array}\right]\left[\begin{array}{cc}{1} & {3} \\\ {5} & {6}\end{array}\right]=\left[\begin{array}{cc}{1} & {0} \\\ {0} & {1}\end{array}\right]$ in $G L\left(2, Z_{7}\right)$] The group $G L(n, F)$ is called the general linear group of $n \times n$
matrices over $F .$

- The set of all symmetries of the infinite ornamental pattern in which arrowheads are spaced uniformly a unit apart along a line is an Abelian group under composition. Let $T$ denote a translation
  to the right by one unit, $T^{-1}$ a translation to the left by one unit, and $H$
  a reflection across the horizontal line of the figure. Then, every member
  of the group is of the form $x_{1} x_{2} \cdots x_{n},$ where each $x_{i} \in$ $\left\\{T, T^{-1}, H\right\\} .$ In this case, we say that $T, T^{-1},$ and $H$ generate the group.
  
  ![image](assets/upsc/mathematics_optional/algebra/groups_arrow.png)
  
## Properties

The following three theorems were very easy to prove for me.

---
**Theorem 2.1** In a group $G$, there is only one identity element.

**Proof:** Suppose both $e$ and $e^{\prime}$ are identities of $G .$ Then
1. $a e=a$ for all $a$ in $G,$ and
2. $e^{\prime} a=a$ for all $a$ in $G .$

The choices of $a=e^{\prime}$ in (part 1$)$ and $a=e$ in (part 2$)$ yield $e^{\prime} e=e^{\prime}$
and $e^{\prime} e=e .$ Thus, $e$ and $e^{\prime}$ are both equal.

---

---

**Theorem 2.2:** In a group $G,$ the right and left cancellation laws hold; that is ,
$b a=c a$ implies $b=c,$ and $a b=a c$ implies $b=c$ (easy to see)

---

A consequence of the cancellation property is the fact that in a Cayley
table for a group, each group element occurs exactly once in each row
and column. **Proof:** Each element occurs at least once as suppose $M$
doesn't occur in column of $R$, its not possible as we have
$R^{-1}M =$ something (binary composition). Now to prove at most 1, we
have $RM = K$ and $RN = K \Rightarrow RM = RN \Rightarrow M = N$.

---

**Theorem 2.3:** Inverse is unique (easy to prove)

---

So we will unambiguously denote the inverse by $g^{-1}$

Similarly, when $n$ is a positive integer, the associative law allows us to
use $g^{n}$ to denote the unambiguous product
We define $g^{0}=e .$ When $n$ is negative, we define $g^{n}=\left(g^{-1}\right)^{|n|}$ [for example, $g^{-3}=\left(g^{-1}\right)^{3}.$] 
familiar laws of exponents hold for groups; that is, for all integers $m$ and
$n$ and any group element $g,$ we have $g^{m} g^{n}=g^{m+n}$ and $\left(g^{m}\right)^{n}=g^{m n}$

_Note: $ax = b \Rightarrow x = a^{-1}b$ which is unique as inverse is
unique_

Also, one must be careful with this notation when dealing with a
specific group whose binary operation is addition and is denoted by
"+"

---

Multiplicative Group $\hspace{80pt}$ Additive Group
<!-- {\text { Multiplicative Group }} & & {\text { Additive Group }} \\\ -->
$\begin{array}{lllll}{ a \cdot b \text { or ab}} & {\text { Multiplication }} & {a+b} & {\text { Addition }} \\\  {e \text { or } 1} & {\text { Identity or one }} & {0} & {\text { Zero }} \\\ {a^{-1}} & {\text { Multiplicative inverse of } a} & {-a} & {\text { Additive inverse of } a} \\\ {a^{n}} & {\text { Power of } a} & {n a} & {\text { Multiple of } a} \\\ {a b^{-1}} & {\text { Quotient }} & {a-b} & {\text { Difference }}\end{array}$

---

So, $g^{-3}$ means $(-g) + (-g) + (-g)$ and is written as $-3g$.

As is the case for real numbers, we use $a - b$ as an abbreviation for $a + (-b)$.

_Note:_ $a^{2}\left(b c d b^{2}\right)=a^{2} b(c d) b^{2}=\left(a^{2} b\right)(c d) b^{2}=a(a b c d b) b$

---

**Theorem 2.4:** For group elements $a$ and $b,(a b)^{-1}=b^{-1} a^{-1}$ (easy to prove) 

---

## Dihedral Group

Suppose we remove a square region from a plane, move it in some way,
then put the square back into the space it originally occupied. We would like to describe all possible ways in which this can be
done. More specifically, we want to describe the possible relationships
between the starting position of the square and its final position in
terms of motions. However, we are interested in the net effect of a
motion, rather than in the motion itself.

To begin, we can think of the square region as being transparent (glass,
say), with the corners marked on one side with the colors blue, white,
pink, and green. This makes it easy to distinguish between motions that
have different effects.

The eight motions $R_0, R_{90}, R_{180}, R_{270}, H, V, D,$ and $D'$,
together with the operation composition, form a mathematical system
called the dihedral group of order 8. _Note: Inverse of $R_\alpha$, L is
$R_{360 - \alpha}$, L resp. (L is a reflection)_

To be sure that $D_4$ is indeed a group, we should check this equation
for each of the $8^3$ = 512 possible choices of a, b, and c in $D_4$. In
practice, however, this is rarely done! Here, for example, we simply
observe that the eight motions are functions and the operation is
function composition. Then, since function composition is associative,
we do not have to check the equations.

**Cayley Table (i.e. operation table, aka composition table) for $D_4$**

$\begin{array}{l|llllllll}{} & {R_{0}} & {R_{90}} & {R_{180}} & {R_{270}} & {H} & {V} & {D} & {D^{\prime}} \\\ \hline R_{0} & {R_{0}} & {R_{90}} & {R_{180}} & {R_{270}} & {H} & {V} & {D} & {D^{\prime}} \\\ {R_{90}} & {R_{90}} & {R_{180}} & {R_{270}} & {R_{0}} & {D^{\prime}} & {D} & {H} & {V} \\\ {R_{180}} & {R_{180}} & {R_{270}} & {R_{0}} & {R_{90}} & {V} & {H} & {D^{\prime}} & {H} \\\ {R_{270}} & {R_{270}} & {R_{0}} & {R_{90}} & {R_{180}} & {D} & {D^{\prime}} & {V} & {H} \\\ {H} & {H} & {D} & {V} & {D^{\prime}} & {R_{0}} & {R_{180}} & {R_{90}} & {R_{270}} \\\ {V} & {V} & {D^{\prime}} & {H} & {D} & {R_{180}} & {R_{0}} & {R_{270}} & {R_{90}} \\\ {D} & {D} & {V} & {D^{\prime}} & {H} & {R_{270}} & {R_{90}} & {R_{0}} & {R_{180}} \\\ {D^{\prime}} & {D^{\prime}} & {H} & {D} & {V} & {R_{90}} & {R_{270}} & {R_{180}} & {R_{0}}\end{array}$

The analysis carried out above for a square can similarly be done for an
equilateral triangle or regular pentagon or, indeed, any regular $n$-gon
($n \geq 3$). The corresponding group is denoted by $D_n$ and is called
the dihedral group of order $2n$. It is often called the group of
symmetries of a regular n-gon.

A plane symmetry of a figure F in a plane is a function from the plane
to itself that carries F onto F and preserves distances; that is, for
any points p and q in the plane, the distance from the image of p to the
image of q is the same as the distance from p to q.

The symmetry group of a plane figure is the set of all symmetries of the
figure. Obviously, a rotation of a plane about a point in the plane is a
symmetry of the plane, and a rotation about a line in three dimensions
is a symmetry in three-dimensional space. Similarly, any translation of
a plane or of three-dimensional space is a symmetry. A reflection across
a line L is that function that leaves every point of L fixed and takes
any point q, not on L, to the point q' so that L is the perpendicular
bisector of the line segment joining q and q'. A reflection across a
plane in three dimensions is defined analogously.

Just as a reflection across a line is a plane symmetry that cannot be
achieved by a physical motion of the plane in two dimensions, a
reflection across a plane is a three-dimensional symmetry that cannot be
achieved by a physical motion of three-dimensional space.

### Another Representation of $D_n$

Let $S = \mathbb{R}^2$ and $n \in \mathbb{N}; n > 2$

Consider, 

$f: S \rightarrow S$ s.t. $f(x, y) = (-x, y)$

and $h: S \rightarrow S$ be a rotation by an angle of $2\pi/n$ in the counterclockwise dirn.

Then $G = \\{f^kh^j \mid k = 0, 1 \text{ and } j = 0, 1, ..., n - 1\\} = D_n$
