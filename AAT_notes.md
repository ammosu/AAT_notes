# AAT 課程筆記（Algebraic Automata Theory / 半群與自動機）

> 由手寫掃描檔 `AAT001.jpg` ～ `AAT016.jpg` 轉錄。數學式以 LaTeX（`$...$`）表示。
> 原筆記以多色筆書寫，左右兩欄；轉錄時依閱讀順序（先左欄、後右欄）排列。
> 筆記中劃掉的字不轉錄；無法辨識處以 `[?]` 標註。常用縮寫：sgp = semigroup、gp = group、homo = homomorphism。

---

## 第 1 頁（AAT001）

**Def:** Semigroup $(S,\mu)$ is a set $S$ with associative operation $\mu$. Where associative means

$$\mu(a,\mu(b,c)) = \mu(\mu(a,b),c)\quad \forall a,b,c\in S$$

or simply: $a\mu(b\mu c) = (a\mu b)\mu c$.

Let $S$ be set, $*$ be binary operation on $S$ which is not associative, how many different kinds of combination of $n$ elements with $*$?

- $a*b*c$: 2 kinds — $((a*b)*c)$, $(a*(b*c))$
- $a*b*c*d$: 5 kinds — $(((a*b)*c)*d)$, $((a*(b*c))*d)$, $((a*b)*(c*d))$, $(a*(b*(c*d)))$, $(a*((b*c)*d))$

**Ex:** $(\mathbb N,+), (\mathbb Z,+), (\mathbb R,\cdot), (\mathbb C,\cdot),\dots$ are semigps.
$S$ set. $(P(S),\cup)$, $(P(S),\cap)$ are semigps. $(P(S),\Delta)$ forms abelian group.

$x(g\circ f) = (xg)f$

### Brief History

- Semigroup: 1900⁺
- Semigroups & automata enriching each other for the last few decades.
- L.A. de Séguier, 1904, *Éléments de la Théorie des Groupes Abstraits*
- First research: K. Suschkewitsch in 1928: Every finite semigroup contains a simple ideal.
- Books: Petrich 1973, ✡ Howie 1976, Lallement 1979, Grillet 1995.
- Theory of automata. A. Turing (Turing Machine)

**Ex:** $(\mathbb R,\max)$ with $x \max y := \max\{x,y\}\ \forall x,y\in\mathbb R$.
$(M_n(\mathbb R),\cdot)$ monoid, $(M_n(\mathbb R),+)$ ab gp, $(\mathbb R[x],+)$ ab gp, $(\mathbb R[x],\cdot)$ monoid, $(\mathbb R[x],\circ)$ monoid.
$S\neq\emptyset$ set, $(S^S,\circ)$ monoid.
$(S,+)$ gp $\Rightarrow (S^S,+,\circ)$ nearring.
$\|\mathbb N\| = \aleph_0$ (aleph null), $\|\mathbb R\| = \aleph_1$ (aleph one).

**Def:** Let $(S,\circ)$ be semigroup, $x\in S$.

1. $x$ is called a **zero element** of $S$ if $x\circ t = t\circ x = x\ \forall t\in S$.
2. $x$ is called an **identity element** of $S$ if $x\circ t = t\circ x = t\ \forall t\in S$.
3. $x$ is called **idempotent** if $x\circ x = x$.
4. If $(S,\circ)$ has an identity, then $(S,\circ)$ is called **monoid**.
5. If $(S,\circ)$ is a monoid, then $x$ is called **invertible** or an invertible element if $\exists!\, y\in S \ni x\circ y = $ identity.
6. If $(S,\circ)$ is a monoid and $\forall s\in S\ \exists!\, t\in S \ni s\circ t = t\circ s = $ identity, then $(S,\circ)$ forms a **group**.

**Def:** Let $(M,\circ)$ be monoid, then $G_M := \{x\in S : x \text{ is invertible}\}$ is called the **group kernel** (unit group) of $(M,\circ)$.

**Thm:** $(G_M,\circ)$ is a group within $(S,\circ)$.

If $x,y\in G_M$, then $x\circ y$ has $y^{-1}\circ x^{-1}$ as inverse. $\therefore x\circ y\in G_M$.
Since $1_M\circ 1_M = 1_M$, we have $1_M\in G_M$.
If $x\in G_M$, then $x\circ x^{-1} = 1_M = x^{-1}\circ x \Rightarrow x^{-1}\in G_M$.
Hence $(G_M,\circ)$ forms a group.

**Ex:**

| Monoids | Group kernels |
|---|---|
| $(\mathbb N_0,+)$ | $\{0\}$ |
| $(\mathbb N,\cdot)$ | $\{1\}$ |
| $(\mathbb Z,\cdot)$ | $\{1,-1\}$ |
| $(\mathbb Q,\cdot)$ | $\mathbb Q\setminus\{0\}$ |
| $(M_n(\mathbb R),\cdot)$ | $GL(n,\mathbb R)$ |
| $(S^S,\circ)$ | $\{f\in S^S : f: S\to S \text{ bijective}\}$ |
| $(P(X),\Delta)$ | $P(X)$ |
| $(G,\cdot)$ | $G$ |

**Remark:** The larger the group kernel the closer a monoid resembles a group.

What is the group kernel of $(\mathbb Z/n\mathbb Z,\cdot)$?

---

## 第 2 頁（AAT002）

The inverse of $x$ (in group kernel) can be found by representing $1$ as $1 = xa + nb$ for some suitable $a,b\in\mathbb Z$
$\Rightarrow [1] = [x]\cdot[a] + [n][b] = [x]\cdot[a]$

## Chap 2: Subsemigroups and Homomorphism

With a semigp we can have smaller semigroup as the substructures (or subsemigroups). $(\mathbb N,\cdot) < (\mathbb Z,\cdot)$

**Def:** Let $(S,\circ)$ be a semigroup (sgp) and $A,B\subseteq S$, then $A\circ B := \{a\circ b : a\in A, b\in B\}$.
Instead of $A\circ A, A\circ A\circ A,\dots$, we write $A^2, A^3,\dots$, and $\{a\}\circ B := a\circ B := aB$.

**Def:** Let $(S,\circ)$ be a sgp and $\emptyset\neq U\subseteq S$. $U$ is a **subsgp** of $S$ if $U^2\subseteq U$.
In the sequel (following), we write $(U,\circ)\le(S,\circ)$ or simply $U\le S$ if the operations are obvious to denote $U$ is a subsgp of $S$.

**Ex:** $(\mathbb N,\cdot)\lneq(\mathbb Z,\cdot)$, $(\mathbb N,+)\lneq(\mathbb Z,+)$, $(\mathbb N,+)\not\le(\mathbb Z,\cdot)$

One can immediately realize that subsgp $U$ of monoid $S$ in general is not a monoid.
**Ex:** $(\mathbb N,+) < (\mathbb N\cup\{0\},+)$

One must be careful to the fact that even if $U$ is a submonoid of the monoid $S$, the identity of $U$ need not to be equal to the identity of $S$.
**Ex:** $(\{0\},\cdot)\lneq(\mathbb Z,\cdot)$

**Thm 2.4:** Nonempty intersection of subsgps of sgp is again a subsgp.

Let $x,y\in\bigcap_{i\in I}S_i$ with $S_i\le S$, $I\subseteq\mathbb N$, $i\in I$.
$\Rightarrow x,y\in S_i\ \forall i\in I$. Since $S_i\le S\ \forall i\in I$, we have $x\circ y\in S_i\ \forall i\in I \Rightarrow x\circ y\in\bigcap_{i\in I}S_i$
$\therefore \bigcap_{i\in I}S_i\le S$

**Note:** Union of subsgps is not necessary a subsgp in general.
**CEx:** $(\mathbb N,+)\lneq(\mathbb Z,+)$, $(\langle 2\rangle,+)\lneq(\mathbb Z,+)$ but $(\langle 2\rangle\cup\mathbb N,+)\not\le(\mathbb Z,+)$

If $S\in SGP := \{S : S \text{ is sgp}\}$ and $S\neq\emptyset\neq T\subseteq S$, then the intersection of all subsgps containing $T$ forms a subsgp. According Thm 2.4, this subsgp is the smallest subsgp which contains $T$, we denote this subsgp as $\langle T\rangle$.

Since subsgps of $S$, along with $\emptyset$, forms an inductive Moore System, it is possible to speak about generated subsgps.

**Def 2.5:** $\langle T\rangle$ called the subsgp of $S$ **generated by** $T$.

**Note:** If $T=\{y\}$, we use notation $\langle y\rangle$ instead of $\langle\{y\}\rangle$. It is clear that $T$ is subsgp $\Leftrightarrow \langle T\rangle = T$.

**Thm 2.6:** $\forall\, T\subseteq S\in SGP$, $T\neq\emptyset$,
$$\langle T\rangle = \bigcup_{n\in\mathbb N}T^n = \Big\{\prod_{i=1}^m t_i : \{t_i\}_{i=1}^m\subseteq T,\ m\in\mathbb N\Big\}$$

---

## 第 3 頁（AAT003）

$\bigcup_{n\in\mathbb N}T^n\le(S,\circ)$ and any subsgp containing $T$ contains $\bigcup_{n\in\mathbb N}T^n$ by closed, then $\bigcup_{n\in\mathbb N}T^n$ is the smallest subsgp of $(S,\circ)$ containing $T$.
$\therefore \bigcup_{n\in\mathbb N}T^n = \langle T\rangle$

$T\subseteq V\subseteq S$, $\langle T\rangle = S \Rightarrow \langle V\rangle = S$

We want to find out those generating systems which are as small as possible.

**Def:** Let $S$ be sgp, $S$ is said to be **finitely generated** if $\exists\, T\subseteq S$ with $|T|<\aleph_0$ and $\langle T\rangle = S$.

**Ex:**
- $(\mathbb N,+) = \langle 1\rangle$ is cyclic
- $(\mathbb N,\cdot) = \langle\{1\}\cup\mathbb P\rangle$ is not finitely generated
- $(\mathbb N_0,+) = \langle\{0,1\}\rangle$

**Vorobev Theorem:** Bijective functions on finite set $X$ together with one simple nonsurjective generate $X^X$:

**Thm 2.9:** Let $X$ be set with $|X|\in\mathbb N\setminus\{1\}$ and $f\in X^X$ with $|f(X)| = |X|-1$. Then $\langle S_X\cup\{f\}\rangle = X^X$.

> Clifford and Preston 1953, *Theory of Semigroups*. AMS p.7 Ex 10(c)

**Def 2.10:** $(S,\circ),(S',*)\in Sgp$, $f: S\to S'$ called **homo** if $\forall x,y\in S$, $f(x\circ y) = f(x)*f(y)$.

- Injective homo: **mono**
- Surjective homo: **epi**
- Bijective homo: **iso**

**Ex:** $f,p: (\mathbb Z,\cdot)\to(\mathbb N_0,\cdot)$, $x\overset{f}{\mapsto}|x|$, $x\overset{p}{\mapsto}0$

$(P(\{1,2,3\}),\cap) \hookrightarrow\!\!\!\!\to (P(\{a,b,c\}),\cap)$ — Isomorphic sgps

---

## 第 4 頁（AAT004，第 3 頁內容的放大重寫版）

**Thm 2.9** (Cayley embedding；$S_n$: mother group，$S^S$: mother semigroup)
$X\in Set$, $|X| = n > 1$, $f\in X^X$ with $|f(X)| = n-1$
$$\Rightarrow (X^X,\circ) = \langle S_X\cup\{f\}\rangle$$
（旁註：Wallis formula）

$(12)(23) = (132)$

> 1953 Clifford and Preston, *Theory of Semigroups*, AMS p.7 Ex 10(c)

**Def 2.10:** $(S,\circ),(S',*)\in Sgp$. $f: S\to S'$ called homo if $\forall x,y\in S$, $f(x\circ y) = f(x)*f(y)$.

- Injective homo: mono
- Surjective homo: epi
- Bijective homo: iso

**Ex:** $f: (\mathbb Z,\cdot)\to(\mathbb N_0,\cdot)$, $x\overset{f}{\mapsto}|x|$；$p: (\mathbb Z,\cdot)\to(\mathbb N_0,\cdot)$ via $x\overset{p}{\mapsto}0$
$(P(\{1,2,3\}),\cap) \hookrightarrow\!\!\!\!\to (P(\{a,b,c\}),\cap)$

Iso sgps can be regarded as being "essential equal".

**Def 2.12:** $(S,\circ)\in Sgp$, $\sim$ equivalence relation on $S$. Then $\sim$ is called **congruence relation** on $(S,\circ)$ if
$$a\sim a' \text{ and } b\sim b' \Rightarrow a\circ b\sim a'\circ b'$$

（習題）Find $|\mathrm{End}(V_4)|$, $V_4 = \mathbb Z_2\times\mathbb Z_2$.

For congruence relations $\sim$ on $(S,\circ)$ we define on the factor set $S/\!\sim$ an binary operator $\odot$ ("split") by
$$[a]\odot[b] = [a\circ b].$$
This definition is well-defined:

---

## 第 5 頁（AAT005）

If $[a]=[a']$, $[b]=[b']$
$\Rightarrow a\sim a'$, $b\sim b'$
hence $a\circ b\sim a'\circ b'$
whence $[a\circ b] = [a'\circ b']$
$\Rightarrow [a]\odot[b] = [a']\odot[b']$

**Def:** Let $\sim$ be congruence relation on the sgp $(S,\circ)$. $(S/\!\sim,\odot)$ is a sgp which called the **factor sgp** (or **quotient sgp**) of $(S,\circ)$ w.r.t. $\sim$.

**Thm (2.13):** Given $\sim$ congruence relation on sgp $(S,\circ)$, $\pi: S\to S/\!\sim$, $x\mapsto[x]$ is an epi called **canonical (natural) epi**.

$\odot$ well-defined $\Rightarrow \forall [a],[b],[c]\in S/\!\sim$, we have $([a]\odot[b])\odot[c] = [a]\odot([b]\odot[c])$
$\therefore (S/\!\sim,\odot)$ is semigroup.
$\pi$ onto is obviously.
$\pi(a\circ b) = [a\circ b] = [a]\odot[b] = \pi(a)\odot\pi(b)$
$\therefore \pi$ is homo $\Rightarrow \pi$ is epi.

**Thm 2.14 (Homo Thm):** $f: (S,\circ)\to(T,*)$ epi. Then $\sim$ defined by $a\sim b\Leftrightarrow f(a)=f(b)$ is congruence relation on $(S,\circ)$ and $(S/\!\sim,\odot)\cong(T,*)$.

**Pf:** congruence relation:
1. $\forall s\in S$, $f(s)=f(s)\Rightarrow s\sim s$
2. $\forall a,b\in S$, $a\sim b$: $f(a)=f(b)\Leftrightarrow f(b)=f(a)\Leftrightarrow b\sim a$
3. $\forall a,b,c\in S$, $a\sim b\wedge b\sim c\Leftrightarrow f(a)=f(b)\wedge f(b)=f(c)\Rightarrow f(a)=f(c)\Leftrightarrow a\sim c$

By 2.13, $\exists\,\pi: S\twoheadrightarrow S/\!\sim$ canonical via $x\mapsto[x]$ $\wedge$ $(S/\!\sim,\odot)$ is a quotient sgp.
Define $\mu: S/\!\sim\ \to T$ via $\mu([x]) = f(x)\ \forall x\in S$.
well-defined: $[x]=[y]\Rightarrow x\sim y\Rightarrow \mu([x]) = f(x) = f(y) = \mu([y])$
$\forall [x],[y]\in S/\!\sim$, $\mu([x]\odot[y]) = \mu([x\circ y]) = f(x\circ y) = f(x)*f(y) = \mu([x])*\mu([y])$
$\therefore \mu$ is sgp homo, which is trivially epi.
$\mu([x]) = \mu([y])\Leftrightarrow x\sim y$
$\therefore \mu$ is iso.

**Thm 2.22 (Embedding):** $\forall$ sgp $(X,\cdot)$, $\exists\, S\ni (X,\cdot)\hookrightarrow(S^S,\circ)$

If $(X,\cdot)$ is monoid, we can choose $S = X$; otherwise, construct $X^{(1)} := X\cup\{1_X\}$ such that $(X^{(1)},\cdot)$ is monoid with identity $1_X$. Choose $S = X^{(1)}$.
For $x\in X$, $f_x: S\to S$ defined by $f_x(a) = x\cdot a\ \forall a\in S$, $f_x\in S^S$.
Let $\phi: X\to S^S$ via $\phi(x) = f_x\ \forall x\in X$. We need claim $\phi$ is mono.
$x,x'\in X$, $\phi(x\cdot x') = f_{xx'} = f_x\circ f_{x'} = \phi(x)\circ\phi(x')$ $\therefore \phi$ is homo.
$\phi(x) = \phi(x')\Rightarrow f_x = f_{x'}\overset{1_S}{\Rightarrow} x = x'$ $\therefore \phi$ is mono.

---

## 第 6 頁（AAT006）

**Note:** We can say that any sgp is a subsgp of transformations (mappings or function). But this property is usually neither particularly useful nor natural. Only a few people will regard $(\mathbb N,+)$ as subsgp of $(\mathbb N_0^{\mathbb N_0},\circ)$.

## Chap 3: Free Sgps

In linear algebra, one often uses the important result that any mapping of a basis $\beta$ of a vector space $V$ into a vector space $W$ can be uniquely extended to a linear mapping from $V$ into $W$. This can also be done for sgps (also other structures). Sgp with a "basis" $B$ will be called "free on $B$".

（旁註：Does mathematic have elements?）

- $\langle a\rangle$: free sgp
- $\langle a\rangle^* = \{\lambda\}\cup\langle a\rangle$: free monoid
- $\{a\}$ free basis. $\langle\emptyset\rangle = \{1\} = \{\lambda\}$

**Def 3.1:** Let $\mathcal S$ be the class of all sgp, $F\in\mathcal S$ and $\emptyset\neq\beta\subseteq F$. $F$ is called **free sgp on $\beta$** if each mapping $f: \beta\to S\in\mathcal S$ can be extended to a unique sgp homo $h_f: F\to S$. $\beta$ is called a **basis** of $F$. $F = F_\beta$.

We should really write $(F,\cdot)$ but we shall omit this from now and come back later. Definition 3.1 can be formally restated as follows:

**Def 3.1':** Let $F\in\mathcal S$. $F$ is called free on the basis (generating set) $B\subseteq F$ if $\forall S\in\mathcal S$, $f\in S^B$, $\exists!\, h\in\mathrm{Hom}(F,S)\ni h|_B = f$. With diagram on the right:

```
  B ──ι──> F
   \       |
  f \      | h        f = h∘ι
     ↘     ↓
         S
```

For better understanding (since the abstract definition of free sgp in the universal language is rather difficult for beginner), we pause a while here and give a more concrete idea of free sgp in a combinatorial approach.

**Def 3.1'':** Let $X\in Set\setminus\{\emptyset\}$ and
$$X^+ := \{(a_1,\dots,a_n) : a_i\in X, 1\le i\le n, n\in\mathbb N\} := \{a_1\cdots a_n : a_i\in X, 1\le i\le n, n\in\mathbb N\}\ \text{(in coding language)}$$
We define the **concatenation** $*$ in $X^+$ by $a_1\cdots a_n * b_1\cdots b_m := a_1\cdots a_n b_1\cdots b_m$, then $(X^+,*)$ is a semigroup called the **free sgp on $X$**. If we add the empty word $\Lambda$ (the empty string) to $X$, we get the free (word) monoid $X^*$ on $X$.

**Remark 3.2:**
1. $X = \{a\}\Rightarrow (X^+,*)\cong(\mathbb N,+)$
2. $|X|>1\Rightarrow (X^+,*)$ non commutative.
3. $X^+$ is always infinity.
4. No finite sgp can be free except $\langle\emptyset\rangle$, and therefore no finite sgp can have a (free) basis except $\{\lambda\} = \langle\emptyset\rangle$.

---

## 第 7 頁（AAT007）

Thus, free sgps are rather "rare", but there are still plenty of them, since every sgp is the homomorphic image of a free sgp.

Now, we come back to the theory of free sgps in universal language. Hence many questions arise immediately:
Is there a basis for any sgp? If yes, how many? Are all basis of the same cardinality?
We can show that not every sgp has basis. However, if it has bases, then all of them are of same cardinality.

**Thm 3.3:** Let $F$ be free sgp with basis $B$. Then $F = \langle B\rangle$.

Since $B\subseteq F$, consider the diagram $B\overset{\iota}{\hookrightarrow}F$, $f: B\to S = \langle B\rangle$, $h: F\to S$ such that the diagram is commute, with $f: B\to S = \langle B\rangle$, $b\mapsto b$. Then by the definition of free sgp, $\exists!\, h: F\to S$ which extends $f$ to homomorphism. Now consider another diagram, $\mathrm{id}_F$ also extends $B\hookrightarrow F$ ($\iota$). Hence $h = \mathrm{id}_F$ and $F = \langle B\rangle$.

Now it is the right time to start with an set $B$ and try to find a sgp $F\ni B$ is a basis of $F$.

**Thm 3.4:** For any set $B\neq\emptyset$, $\exists$ sgp $F$ which is free on $B$.

Let $\emptyset\neq B\in Set$ and $F = \{\prod_{i=1}^n b_i : b_i\in B, i=1,\dots,n, n\in\mathbb N\}$, then we have
$$\prod_{i=1}^n b_i = \prod_{j=1}^m b'_j \Leftrightarrow n=m \wedge b_t = b'_t,\ t\in\{1,\dots,n\}.$$
We define $\forall x = \prod_{i=1}^n b_i$, $y = \prod_{i=1}^m c_i$, $x,y\in F$, $b_i,c_j\in B$:
$$x*y := \prod_{i=1}^n b_i\cdot\prod_{i=1}^m c_i$$
The operation $*$ on sequences simply consists of writing the two sequence next to each other (called **concatenation** or **juxtaposition**).
$(F,*)$ is obviously a sgp. We have to show that $F$ satisfied the conditions in Def 3.1': $B\hookrightarrow F$, $f: B\to S$, where $S$ is sgp, $f$ is any map.
Define $h: F\to S$ via $h: \prod_{i=1}^n b_i\mapsto\prod_{i=1}^n f(b_i)$, then $h|_B = f$ and $h\in\mathrm{Hom}(F,S)$. If $h'\in\mathrm{Hom}(F,S)$ is an (other) extension of $f$, we have
$$h'\Big(\prod_{i=1}^n b_i\Big) = \prod_{i=1}^n h'(b_i) = \prod_{i=1}^n f(b_i)$$
$\therefore h' = h$

**Thm 3.5:** Let $F$ and $F'$ be free sgps on $B$ and $B'$ resp. Then $F\cong F'\Leftrightarrow |B| = |B'|$.

"$\Rightarrow$": Let $h: F\to F'$ iso. For $b\in B$, $h(b) = b'_1\cdots b'_n\in F'$ for $b'_i\in B'$, $i=1,\dots,n$.
Then $b = h^{-1}(b'_1\cdots b'_n) = h^{-1}(b'_1)\cdot h^{-1}(b'_2)\cdots h^{-1}(b'_n)$.
Thus $n=1$. Since the representation is unique, $\therefore h|_B$ is bij from $B$ to $B'$ and $|B| = |B'|$.

"$\Leftarrow$": The converse follows by the reverse argument.

（旁註：How many ab gps are order 8? $\mathbb Z_8$, $\mathbb Z_4\times\mathbb Z_2$, $\mathbb Z_2^3$, $V_4\times\mathbb Z_2$, $D_8$）

**Cor 3.6:** Let $F$ and $F'$ be free on $B$, then $F\cong F'$. So we can speak of "the" free sgp on $B$. Moreover,

**Cor 3.7:** If $F$ has two basis $B$ and $B'$, then $|B| = |B'|$. Thus all basis for a free sgp are of the same cardinality.

---

## 第 8 頁（AAT008）

So for any cardinal $\alpha$, there exists a free sgp $F_\alpha$ with a basis $B$ with $|B| = \alpha$. Hence we go back to Remark 3.2 (iv).

**Thm 3.8:** Let $S\in Sgp$ and $S = \langle E\rangle$, where $E$ is a generating system (not necessary a basis on $S$). Then $S$ is a homo image of $F_{|E|}\ (=F_E)$.

Consider the diagram $E\overset{\text{canonical}}{\hookrightarrow}F_E$, $\iota: E\to\langle E\rangle$, $h: F_E\to\langle E\rangle$ such that the diagram is commutative. Then $h: F_E\to S$ is an extension of $\iota$.
$\therefore E = \iota(E) = h(E)\subseteq h(F_E)\le\langle E\rangle = S$ and thus $S = \langle E\rangle\subseteq h(F_E)$
$\therefore h(F_E) = S$ $\therefore h$ is epi.

Another proof:
Let $h: E^*\to S$ be given by $h: x_1\cdots x_n\mapsto x_1\circ x_2\circ\cdots\circ x_n$.
Then $h$ is sgp homo and $E = h(E)\subseteq h(E^*)\le S$ and thus $S = \langle E\rangle\subseteq h(E^*)$
$\therefore h(E^*) = S$ $\therefore h$ is epi.

This gives a full explanation of the "free sgp" $F_E$ (or $E^*$) is "free" of all restricted relation (such as commutating). By "adding" such relations, we can obtain any sgp. $F_{|E|}$ is the most general sgp which can be obtained from a generating set (or system) of content $\alpha$. Thm 3.8 enables us to describe a sgp in terms of its generating set and relations.

**Def 3.9:** Let $S\in Sgp$ which is generated by $X$. Let $R$ be relation on $F_X = X^*$. If
$$(X:R) := F_X/\!\sim_R\ = X^*/\!\sim_R\ \cong S,$$
the pair $(X:R)$ is called a **presentation** of $S$, and we usually write $S = (X:R)$.

**Ex:** $(\{x,y\} : \{(x^2,1),(y^3,1),(xy^2,yx)\})\cong S_3$

Elements of $R$ are called **defining relations**, despite the fact that they are not relations at all. Thm 3.8 guarantees a representation for every sgp. Note that a sgp has many different presentations.

**Ex 3.10:** Let $(S,\circ) = (\mathbb Z_4,\cdot)$, $X = \{x_1,x_2\}$,
$$R = \{(x_1x_2, x_2x_1), (x_2x_2x_1, x_1), (x_2x_2x_2, x_2), (x_1x_1x_1, x_1x_1), (x_1x_2, x_1)\}$$
We consider the equivalence classes $a_0 := [x_1]$, $a_1 := [x_2]$, $a_2 := [x_1x_1]$, $a_3 := [x_2x_2]\in F_X/\!\sim_R$, with operator $*$.
Operation on these classes is as follows:

| $*$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ |
|---|---|---|---|---|
| $a_0$ | $a_2$ | $a_0$ | $a_2$ | $a_0$ |
| $a_1$ | $a_0$ | $a_3$ | $a_2$ | $a_1$ |
| $a_2$ | $a_2$ | $a_2$ | $a_2$ | $a_2$ |
| $a_3$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ |

$a_0*a_0 = [x_1]*[x_1] = [x_1x_1] = a_2$
$a_0*a_1 = [x_1]*[x_2] = [x_1x_2] = [x_1] = a_0$
and so on, we have $F_X/\!\sim_R\ \cong S$ by $\varphi: F_X/\!\sim_R\ \to S$ via $\varphi: a_0\mapsto 2$, $a_1\mapsto 3$, $a_2\mapsto 0$, $a_3\mapsto 1$ is iso.

All that can be done also for the classes of monoids, gps, ab gps, modules, algebras, and so on, to obtain free monoids, free gps, free ab gps, free modules, free algebras, and so on, resp.
The free monoid with basis $X$ is denoted by $X_* = X^*\cup\{\lambda\}$ only by adding an additional "empty word (empty string)" $\lambda$.
Here we again point out that the free sgp $X^* = \{a\}^*\cong(\mathbb N,+)$, the free monoid $X_* = \{a\}_*\cong(\mathbb N_0,+)$, and the free (ab) gp over $X = \{a\}$ is iso to $(\mathbb Z,+)$.

（註：此處筆記的記號與 Def 3.1'' 不同——這裡 $X^*$ 指 free sgp，$X_*$ 指 free monoid。）

Presentation are often by far the most concise way to describe sgps. They are the method to investigate sgps and gps on a computer.

## Chap 4: Sgp and Automata

We see automata and machines in various fields such as calculating machines, computers, money-changing machines, telephone switch boards, and elevator or lift switchings. We can use a black box to indicate what is common to all general automata.

**Ex:** Coca Cola automaton $\mathcal A$:
Capacity of 5 bottles of Coca Cola. Define it as automata such that the states $z$ means "there are $z$ bottles of
Coca Cola in $\mathcal A$", the inputs are "no coin is inserted", "a correct coin is inserted", "a wrong coin is inserted", and the outputs are "a bottle of Coca Cola is out", "no output", "a coin is output". Complete the table and the state graph.

---

## 第 9 頁（AAT009）

**Solution:**

**(I) Table of Coca Cola automaton $\mathcal A$:**

- State set $Z = \{0,1,2,3,4,5\}$, the set of the numbers of Coca Cola.
- Input set $I = \{n,c,w\}$, $n :=$ "no coin insert", $c :=$ "correct coin inserted", $w :=$ "wrong coin inserted".
- Output set $B = \{x,y,s\}$, $x :=$ "no output", $y :=$ "a coin is output", $s :=$ "a bottle of Coca Cola is output".

Transition function $\delta: Z\times I\to Z$, also called next step function:

| $\delta$（I \ Z） | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
| $c$ | 0 | 0 | 1 | 2 | 3 | 4 |
| $w$ | 0 | 1 | 2 | 3 | 4 | 5 |

Output function $\lambda: Z\times I\to B$:

| $\lambda$（I \ Z） | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $n$ | x | x | x | x | x | x |
| $c$ | y | s | s | s | s | s |
| $w$ | y | y | y | y | y | y |

$$\mathcal A = (Z, I, B, \delta, \lambda)$$

**(II) State graph of Coca Cola automaton $\mathcal A$:**

```
 每個狀態 z (z = 0,1,2,3,4,5) 都有自迴圈： n;x 與 w;y

  ┌ c;y ┐
  └─> (0) <─c;s─ (1) <─c;s─ (2) <─c;s─ (3) <─c;s─ (4) <─c;s─ (5)
```

$n$ and $w$ give identical loops $\forall z\in Z$ which must be add to the diagram, $\delta: Z\times I\to Z$ and $\lambda: Z\times I\to B$.

**Def 4.1 (Semiautomaton):** A semiautomaton $\mathcal S = (Z,I,\delta)$ containing of two nonempty sets $Z$ (the set of states) and $I$ (the set of inputs), and a function $\delta: Z\times I\to Z$ (the next-state function or the transition function).

If we need to study the outputs, we need automata rather than semiautomata.

**Def 4.2:** An automaton is a quintuple $\mathcal A = (Z,I,B,\delta,\lambda)$ where $(Z,I,\delta)$ is a semiautomaton, with set $B$ (output set or output alphabet), and $\lambda: Z\times I\to B$ (the output function).

Definition 4.1, 4.2 are rather abstract.

**Def 4.3:** An automaton (or a semiautomaton) is **finite** if $Z, I, B$ are finite. Finite automata are called **Mealy automata**. If a special state $z_0\in Z$ is fixed, the (semi)automata are called **initial** and $z_0$ is called the initial state. We write $(Z,I,\delta,z_0)$ in case to emphasize the initial state $z_0$. An automaton with $\lambda$ depending only on $z$ is a **Moore automaton**.

**Ex 4.4:**
1. Describe parts of your brain as a semiautomaton, such that the set of theorems in this lecture and $\delta$ describe "studying".
2. Could you interpret the semiautomaton in (I) as a computer?
3. What would be possible interpretation if semiautomaton in (I) should be considered as an automaton?
4. Same as (III) but with interpretation as an initial automaton.

**Solution:**
1. $I$: set of all theorems in this lecture notes. $Z = P(I)$, $z\in Z$ is the collection of theorems in $I$ "Already knows". $\delta(z,\alpha) := z\cup\{\alpha\}$: "Add theorem $\alpha$ to already known".
2. Yes. Input: "Theorems", $z$: "Theorems in the storage", $\delta(z,\alpha)$: "Add theorem $\alpha$ to the theorems $z$ in the storage".
3. $B$: list of the theorems, $\lambda(z,a)$: "Table of learned theorems" including $a$ and theorems in $z$.
4. For instance, $z_0 = \emptyset$ can mean that you know no theorems.

In computer, it would be rather artificial to consider only single input signals. Programs consist of a sequence of elements of input alphabet. Thus it is reasonable to consider the set of all finite sequences of elements of the input set $I$, including the empty sequence $\lambda$. In other words, in our study of automata **we extend the input set $I$ to a free monoid $I_*$ with $\lambda$ as an identity.**

Here we also extend $\delta: Z\times I\to Z$ to $\delta^*: Z\times I^*\to Z$ via $\delta(z,a)\longrightarrow\delta^*(z,a_1\cdots a_n)$ and $\lambda: Z\times I\to B$ to $\lambda^*: Z\times I^*\to B^*$ via $\lambda(z,a)\longrightarrow\lambda^*(z,a_1\cdots a_n)$. Thus the semiautomaton $\mathcal S = (Z,I,\delta)$ (the automaton $\mathcal A = (Z,I,B,\delta,\lambda)$) is then extended to the new semiautomaton $\mathcal S^* = (Z,I^*,\delta^*)$ (automaton $\mathcal A^* = (Z,I^*,B^*,\delta^*,\lambda^*)$).

---

## 第 10 頁（AAT010，鉛筆）

Here, one can easily describe the action of $\mathcal S$ and $\mathcal A$ if we let $z\in Z$ and $a_1,\dots,a_n\in I$:

$$\begin{aligned}
z_1 &= z\\
z_2 &:= \delta(z_1,a_1)\\
z_3 &:= \delta^*(z_1,a_1a_2) = \delta(\delta(z_1,a_1),a_2) = \delta(z_2,a_2)\\
z_4 &:= \delta(z_3,a_3)\\
&\ \ \vdots\\
z_{n+1} &:= \delta(z_n,a_n)
\end{aligned}$$

In general:
$$\delta^*(z,a_1\cdots a_n) = \delta(\delta(\cdots\delta(\delta(z,a_1),a_2)\cdots,a_{n-1}),a_n)$$
and
$$\lambda^*(z,a_1\cdots a_n) = \lambda(z_1,a_1)\cdots\lambda(z_n,a_n)$$
$\delta^*(z,\lambda) = z$, $\lambda^*(z,\lambda) = \lambda$

Here is a very famous result: **Any (semi-)automaton determines a certain monoid. Conversely, any monoid gives rise to a certain (semi-)automaton.**

> 1987–88 *Computer Program for Investigating Syntactic Nearrings of Finite Group-Semiautomaton* (1988, Bulletin of the Institute of Mathematics Academia [Sinica?], vol 16, no 4, Dec 1988), pp. 295–304

$(P(X),\Delta,\cap)$ forms a ring where $\Delta$ is symmetric difference.

**Abstract:** Let $S = (C_n, C_n, \delta)$ be a GSA (group semiautomaton) with $\delta(x,y) = x+y$ and $N(S)$ be the subnr (in fact, called the syntactic nr of GSA $S$) of the transformation nr of $(M(G),+,\circ)$.
$$N(S) = N(C_n) = \mathrm{End}\,C_n\oplus M_c(C_n)$$
Furthermore, $|N(C_n)| = n^2$.

**Introduction and preliminaries:**

**Ex:** $G = (C_2,+)$, define $(G^G,\oplus,\circ)$ in following fashion: $\forall f,g\in G^G \wedge x\in G$,
$$x(f\oplus g) = xf + xg,\qquad x(f\circ g) = (xf)g,$$
then we have the following 2 tables（id 恆等、inv 交換 0↔1、T 常數 1、F 常數 0）:

| $\oplus$ | id | inv | T | F |
|---|---|---|---|---|
| **id** | F | T | inv | id |
| **inv** | T | F | id | inv |
| **T** | inv | id | F | T |
| **F** | id | inv | T | F |

| $\circ$ | id | inv | T | F |
|---|---|---|---|---|
| **id** | id | inv | T | F |
| **inv** | inv | id | T | F |
| **T** | T | F | T | F |
| **F** | F | T | T | F |

$(G^G,\oplus)$ ab gp. $(G^G,\circ)$ non-ab sgp.

Left distribution law holds: $f_1\circ(f_2\oplus f_3) = (f_1\circ f_2)\oplus(f_1\circ f_3)$.
But right distribution law not hold in general, $(f_1\oplus f_2)\circ f_3\neq(f_1\circ f_3)\oplus(f_2\circ f_3)$:
$$(\mathrm{id}\oplus\mathrm{inv})\circ T = T\neq F = (\mathrm{id}\circ T)\oplus(\mathrm{inv}\circ T)$$

With the above example, we then give an abstract definition of what a nr.

---

## 第 11 頁（AAT011，鉛筆）

(Fastringe)

**Definition 1:** A **nearring** is a triple $(N,+,\cdot)$ with binary operations $+$ and $\cdot$ on the set $N$ such that
1. $(N,+)$ is a gp
2. $(N,\cdot)$ is a sgp
3. $\forall a,b,c\in N$, $a\cdot(b+c) = a\cdot b + a\cdot c$.

In fact, the above nr is actually called a **left nr**. If we replace (III) by (III'): $\forall a,b,c\in N$, $(a+b)\cdot c = a\cdot c + b\cdot c$, then $(N,+,\cdot)$ is called a **right nr**.

**Def 2:** For nr $(N,+,\cdot)$
1. If $(N,+,\cdot)$ satisfy (III'), then $(N,+,\cdot)$ is called a **distributive nr**.
2. If $(N,+)$ comm, then $(N,+,\cdot)$ is called **ab nr**.
3. If $(N,\cdot)$ comm, then $(N,+,\cdot)$ is called **comm nr**.
4. If both $0_N x = x 0_N = 0_N\ \forall x\in N$, then $N$ is called a **zero-symmetric nr**.
5. If $S\subseteq N\wedge(S,+,\cdot)$ forms a nr $\Rightarrow(S,+,\cdot)$ called a **subnr** of $(N,+,\cdot)$. In short, $S\le N$.
6. If $(N^*,\cdot)$ forms a gp, where $N^* = N\setminus\{0_N\}$, then $(N,+,\cdot)$ is a **left nearfield**.

**Ex:** $G = (S_3,+)$, $\mathrm{End}\,G = \{f : f\in S_3^{S_3}, (x+y)f = xf + yf\ \forall x,y\in S_3\}$
Question: What is $\mathrm{End}\,G$? hint: $|\mathrm{End}\,G| = 10$
$E(S_3) := \langle\mathrm{End}\,S_3,\oplus,\circ\rangle$ has 54 elements. $|S_3^{S_3}| = 46656$
$|\mathrm{End}\,S_4| = 58$, $|E(S_4)| = 2^{35}\cdot 3^3$ [?]

**Ex:** $(\{0,1\},+,\cdot)$ by

| + | 0 | 1 |
|---|---|---|
| **0** | 0 | 1 |
| **1** | 1 | 0 |

| · | 0 | 1 |
|---|---|---|
| **0** | 0 | 0 |
| **1** | 0 | 1 |

is a nf.

**Def:** For semiautomaton $\mathcal S = (Z,I,\delta)$, if $(Z,+)$ is gp, $\mathcal S$ is called **group semiautomaton (GSA)**. Here we write $Z = G$.

Given any $\mathcal S$, we have $\{f_a\in G^G : a\in I\}$ where $f_a: x\mapsto\delta(x,a)\ \forall x\in G$. If we extend $I$ to $I^*$, the free monoid over $I$, we therefore get $f_{ab} = f_a\circ f_b\ \forall a,b\in I$ for if $\forall x\in G$,
$$xf_{ab} = \delta^*(x,ab) = \delta(\delta(x,a),b) = \delta(xf_a,b) = (xf_a)f_b = x(f_a\circ f_b).$$
So we have the map $\theta: I^*\to M_S$ via $a\mapsto f_a$, i.e. $a\theta = f_a$, is a monoid monomorphism with $f_\lambda = \mathrm{id}_G$ where $M_S = \{f_a : a\in I^*\}$ is called the **monoid of the GSA $S$** and $\lambda$ is the empty string.

So if $G$ is a group, we can speak about the sum of $f_a$ and $f_b$ through pointwise addition, i.e. $x(f_a\oplus f_b) = xf_a + xf_b\ \forall x\in G$.

Here it is natural to consider the sums and the products of the elements in $\{f_a : a\in I^*\}\cup\{\mathrm{id}_G\}$ (or simply $\{f_a : a\in I\}\cup\{\mathrm{id}_G\}$) and the ultimate structure turns out to be left nr.

**Def:** Let $S = (G,I,\delta)$ be a GSA. The subnr $N(S)$ of $M(G)$ generated by $\{f_a : a\in I\}\cup\{\mathrm{id}_G\}$ is called the **syntactic nr**.

---

## 第 12 頁（AAT012，鉛筆，僅右欄有字）

### Structure of $N(S)$

**Def A:** Let $G, I$ be add gp and $\delta: G\times I\to G$ homo. We call $S = (G,I,\delta)$ a **homomorphic GSA**.

For
$$xf_a = \delta(x,a) = \delta((x,0)+(0,a)) = \delta(x,0)+\delta(0,a) = xf_0 + 0f_a\ \big(= x(f_0+\bar f_a)\big),\qquad 0f_a = x\bar f_a\ \ \forall x\in G$$
We get $f_a = f_0 + \bar f_a$ where $\bar f_a: x\mapsto 0f_a\ \forall x\in G$.

**Thm B** (G. Hofer and G. Pilz): Let $S = (G,I,\delta)$ be a homomorphic GSA, then
$$N(S) = \Big\{\sum\pm f_{a_i} : a_i\in I^*\Big\}$$

With the help of Theorem B, we start to detect our algorithm with the following example:

**Ex C:** Let $p\in\mathbb P\setminus\{2\}$ be the odd prime (and in particular, $p = 5$). Suppose $S = (C_p, C_p, \delta)$ with $\delta: (x,y)\mapsto x+y$.

---

## 第 13 頁（AAT013，鉛筆）

Then $M_S = \{f_0, f_1,\dots,f_{p-1}\}$ （$p=5$：$M_S = \{f_0,f_1,f_2,f_3,f_4\}$）

（$(\cdots)_c$ 為輪換 cycle 記法）
- $f_0 = (1)$
- $f_1 = (0\,1\,2\cdots(p-1))_c$
- $f_2 = (0\,2\,4\cdots(p-1)\,1\,3\cdots(p-2))_c$
- $\ \vdots$
- $f_{p-1} = (0\,(p-1)\,(p-2)\cdots 2\,1)_c$

Thus, one can easily see that $(M_S,\circ)\cong(C_p,+)$.

Now we proceed on our calculations in the following（$p=5$；不帶下標 $c$ 的五位數為一行式記法，依序表示 $0,1,2,3,4$ 的像）:

| | | |
|---|---|---|
| $a_1 = 2f_0 = (1\,2\,3\,4)_c$ [?] | $a_6 = 4f_1 = (43210)$ | $a_{11} = 3f_3 = (42031)$ |
| $a_2 = 3f_0 = (1\,3\,4\,2)_c$ | $a_7 = 2f_2 = (41302)$ | $a_{12} = 4f_3 = (21043)$ |
| $a_3 = 4f_0 = (1\,4)(2\,3)_c$ | $a_8 = 3f_2 = (14203)$ | $a_{13} = (30241)$ |
| $a_4 = 2f_1 = \binom{0\,1\,2\,3\,4}{2\,4\,1\,3\,0}$ | $a_9 = 4f_2 = (32104)$ | $a_{14} = (20314)$ |
| $a_5 = 3f_1 = \binom{0\,1\,2\,3\,4}{3\,1\,4\,2\,0}$ | $a_{10} = 2f_3 = (13024)$ | $a_{15} = (10432)$ |

（註：$a_1 = 2f_0$ 即 $x\mapsto 2x$，正確的輪換應為 $(1\,2\,4\,3)_c$；$a_{13},a_{14},a_{15}$ 分別為 $2f_4, 3f_4, 4f_4$。）

- $\theta_0 = f_0 + a_3 = (00000) = 0$
- $\theta_4 = f_0 + a_6 = (44444)$
- $\theta_3 = f_0 + a_9 = (33333)$
- $\theta_2 = f_0 + a_{12} = (22222)$
- $\theta_1 = f_0 + a_{15} = (11111)$

$M_S = \{\theta_i, f_j, a_k : i = 0,\dots,4,\ j = 0,\dots,4,\ k = 1,\dots,15\}$ is a nr and $|M_S| = p^2$.

$$N(S) = \mathrm{End}\,C_5\oplus M_c(C_5) = \mathrm{End}\,C_5 + M_c(C_5)$$

As gp, $N(S)$ is the direct sum as gp of a ring $(\mathrm{End}\,C_5,+,\circ)$ and a constant nr $(M_c(C_5),+,\circ)$.

Take $p = 3$, $S = (C_3, C_3, \delta)$, $M_S = \{f_0,f_1,f_2\}$ where $f_a := \lambda x.\delta(x,a) = \lambda x.\,x+a$.
$$N(S) = \langle M_S,\oplus,\circ\rangle = \langle M_S,\oplus\rangle$$
- $f_0 = (012) = (1)_c$, $f_1 = (120)$, $f_2 = (201)$
- $a_1 = 2f_0 = (021)$, $a_2 = 2f_1 = (210)$, $a_3 = 2f_2 = (102)$
- $\theta_0 = f_0 + a_1 = (000)$, $\theta_2 = f_0 + a_2 = (222)$, $\theta_1 = f_0 + a_3 = (111)$

$\{\theta_0, f_0, a_1\}$, $\{\theta_0,\theta_1,\theta_2\}$

$$N(S) = \mathrm{End}\,C_3 + M_c(C_3)$$

---

## 第 14 頁（AAT014，鉛筆，運算表）

> 以下運算表依筆記內容轉錄，並已用程式依定義 $x(f\oplus g) = xf+xg$、$x(f\circ g) = (xf)g$ 重新計算核對（原稿第 14 頁大 $\oplus$ 表中有幾格筆誤／塗改，此處以計算結果為準）。

$\{\theta_0, f_0, a_1\}$：

| $\oplus$ | $\theta_0$ | $f_0$ | $a_1$ |
|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $f_0$ | $a_1$ |
| **$f_0$** | $f_0$ | $a_1$ | $\theta_0$ |
| **$a_1$** | $a_1$ | $\theta_0$ | $f_0$ |

| $\circ$ | $\theta_0$ | $f_0$ | $a_1$ |
|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $\theta_0$ | $\theta_0$ |
| **$f_0$** | $\theta_0$ | $f_0$ | $a_1$ |
| **$a_1$** | $\theta_0$ | $a_1$ | $f_0$ |

$(\mathrm{End}\,C_3,\oplus,\circ)\cong(C_3,+,\cdot)$ — endomorphism ring

$\{\theta_0,\theta_1,\theta_2\}$：

| $\oplus$ | $\theta_0$ | $\theta_1$ | $\theta_2$ |
|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $\theta_1$ | $\theta_2$ |
| **$\theta_1$** | $\theta_1$ | $\theta_2$ | $\theta_0$ |
| **$\theta_2$** | $\theta_2$ | $\theta_0$ | $\theta_1$ |

| $\circ$ | $\theta_0$ | $\theta_1$ | $\theta_2$ |
|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $\theta_1$ | $\theta_2$ |
| **$\theta_1$** | $\theta_0$ | $\theta_1$ | $\theta_2$ |
| **$\theta_2$** | $\theta_0$ | $\theta_1$ | $\theta_2$ |

$M_c(C_3)$ is constant nr.

$N(S)$ 全表（9 個元素）：

| $\oplus$ | $\theta_0$ | $f_0$ | $a_1$ | $f_1$ | $f_2$ | $a_2$ | $a_3$ | $\theta_1$ | $\theta_2$ |
|---|---|---|---|---|---|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $f_0$ | $a_1$ | $f_1$ | $f_2$ | $a_2$ | $a_3$ | $\theta_1$ | $\theta_2$ |
| **$f_0$** | $f_0$ | $a_1$ | $\theta_0$ | $a_3$ | $a_2$ | $\theta_2$ | $\theta_1$ | $f_1$ | $f_2$ |
| **$a_1$** | $a_1$ | $\theta_0$ | $f_0$ | $\theta_1$ | $\theta_2$ | $f_2$ | $f_1$ | $a_3$ | $a_2$ |
| **$f_1$** | $f_1$ | $a_3$ | $\theta_1$ | $a_2$ | $a_1$ | $\theta_0$ | $\theta_2$ | $f_2$ | $f_0$ |
| **$f_2$** | $f_2$ | $a_2$ | $\theta_2$ | $a_1$ | $a_3$ | $\theta_1$ | $\theta_0$ | $f_0$ | $f_1$ |
| **$a_2$** | $a_2$ | $\theta_2$ | $f_2$ | $\theta_0$ | $\theta_1$ | $f_1$ | $f_0$ | $a_1$ | $a_3$ |
| **$a_3$** | $a_3$ | $\theta_1$ | $f_1$ | $\theta_2$ | $\theta_0$ | $f_0$ | $f_2$ | $a_2$ | $a_1$ |
| **$\theta_1$** | $\theta_1$ | $f_1$ | $a_3$ | $f_2$ | $f_0$ | $a_1$ | $a_2$ | $\theta_2$ | $\theta_0$ |
| **$\theta_2$** | $\theta_2$ | $f_2$ | $a_2$ | $f_0$ | $f_1$ | $a_3$ | $a_1$ | $\theta_0$ | $\theta_1$ |

| $\circ$ | $\theta_0$ | $f_0$ | $a_1$ | $f_1$ | $f_2$ | $a_2$ | $a_3$ | $\theta_1$ | $\theta_2$ |
|---|---|---|---|---|---|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $\theta_0$ | $\theta_0$ | $\theta_1$ | $\theta_2$ | $\theta_2$ | $\theta_1$ | $\theta_1$ | $\theta_2$ |
| **$f_0$** | $\theta_0$ | $f_0$ | $a_1$ | $f_1$ | $f_2$ | $a_2$ | $a_3$ | $\theta_1$ | $\theta_2$ |
| **$a_1$** | $\theta_0$ | $a_1$ | $f_0$ | $a_3$ | $a_2$ | $f_2$ | $f_1$ | $\theta_1$ | $\theta_2$ |
| **$f_1$** | $\theta_0$ | $f_1$ | $a_2$ | $f_2$ | $f_0$ | $a_3$ | $a_1$ | $\theta_1$ | $\theta_2$ |
| **$f_2$** | $\theta_0$ | $f_2$ | $a_3$ | $f_0$ | $f_1$ | $a_1$ | $a_2$ | $\theta_1$ | $\theta_2$ |
| **$a_2$** | $\theta_0$ | $a_2$ | $f_1$ | $a_1$ | $a_3$ | $f_0$ | $f_2$ | $\theta_1$ | $\theta_2$ |
| **$a_3$** | $\theta_0$ | $a_3$ | $f_2$ | $a_2$ | $a_1$ | $f_1$ | $f_0$ | $\theta_1$ | $\theta_2$ |
| **$\theta_1$** | $\theta_0$ | $\theta_1$ | $\theta_2$ | $\theta_2$ | $\theta_0$ | $\theta_1$ | $\theta_0$ | $\theta_1$ | $\theta_2$ |
| **$\theta_2$** | $\theta_0$ | $\theta_2$ | $\theta_1$ | $\theta_0$ | $\theta_1$ | $\theta_0$ | $\theta_2$ | $\theta_1$ | $\theta_2$ |

Let $K = (\{0,a,b,c\},+)$ be Klein-group (Vier-gruppe).
$$\mathcal K = (K, K, \delta)$$

| + | 0 | a | b | c |
|---|---|---|---|---|
| **0** | 0 | a | b | c |
| **a** | a | 0 | c | b |
| **b** | b | c | 0 | a |
| **c** | c | b | a | 0 |

$\delta(x,y) = x+y\ \forall x,y\in K$. What is $N(\mathcal K)$?

---

## 第 15 頁（AAT015，鉛筆）

**Solution:** $M_S = \{f_a: K\to K : a\in K\}$, $xf_a = \delta(x,a) := x+a\ \forall x\in K$

- $f_0 = (0abc)$, $f_a = (a0cb)$, $f_b = (bc0a)$, $f_c = (cba0)$
- $2f_0 = 2f_a = 2f_b = 2f_c = \theta_0$
- $f_0+f_a = f_b+f_c = (aaaa) = \theta_a$
- $f_0+f_b = f_a+f_c = (bbbb) = \theta_b$
- $f_0+f_c = f_a+f_b = (cccc) = \theta_c$

$$\therefore N(\mathcal K) = \{\theta_0,\theta_a,\theta_b,\theta_c,f_0,f_a,f_b,f_c\}\overset{\oplus,\circ}{\cong}(\{\theta_0,f_0\},\oplus,\circ)\oplus(M_c(K),\oplus,\circ)$$
with $M_c(K) = \{\theta_0,\theta_a,\theta_b,\theta_c\}$.

| $\oplus$ | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_0$ | $f_a$ | $f_b$ | $f_c$ |
|---|---|---|---|---|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_0$ | $f_a$ | $f_b$ | $f_c$ |
| **$\theta_a$** | $\theta_a$ | $\theta_0$ | $\theta_c$ | $\theta_b$ | $f_a$ | $f_0$ | $f_c$ | $f_b$ |
| **$\theta_b$** | $\theta_b$ | $\theta_c$ | $\theta_0$ | $\theta_a$ | $f_b$ | $f_c$ | $f_0$ | $f_a$ |
| **$\theta_c$** | $\theta_c$ | $\theta_b$ | $\theta_a$ | $\theta_0$ | $f_c$ | $f_b$ | $f_a$ | $f_0$ |
| **$f_0$** | $f_0$ | $f_a$ | $f_b$ | $f_c$ | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ |
| **$f_a$** | $f_a$ | $f_0$ | $f_c$ | $f_b$ | $\theta_a$ | $\theta_0$ | $\theta_c$ | $\theta_b$ |
| **$f_b$** | $f_b$ | $f_c$ | $f_0$ | $f_a$ | $\theta_b$ | $\theta_c$ | $\theta_0$ | $\theta_a$ |
| **$f_c$** | $f_c$ | $f_b$ | $f_a$ | $f_0$ | $\theta_c$ | $\theta_b$ | $\theta_a$ | $\theta_0$ |

| $\circ$ | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_0$ | $f_a$ | $f_b$ | $f_c$ |
|---|---|---|---|---|---|---|---|---|
| **$\theta_0$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ |
| **$\theta_a$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $\theta_a$ | $\theta_0$ | $\theta_c$ | $\theta_b$ |
| **$\theta_b$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $\theta_b$ | $\theta_c$ | $\theta_0$ | $\theta_a$ |
| **$\theta_c$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $\theta_c$ | $\theta_b$ | $\theta_a$ | $\theta_0$ |
| **$f_0$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_0$ | $f_a$ | $f_b$ | $f_c$ |
| **$f_a$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_a$ | $f_0$ | $f_c$ | $f_b$ |
| **$f_b$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_b$ | $f_c$ | $f_0$ | $f_a$ |
| **$f_c$** | $\theta_0$ | $\theta_a$ | $\theta_b$ | $\theta_c$ | $f_c$ | $f_b$ | $f_a$ | $f_0$ |

$(\mathrm{End}\,\mathbb Z_n,\oplus,\circ)\cong(\mathbb Z_n,+,\cdot)$

**Main Theorem:** Let $n\in\mathbb N$, $S = (C_n, C_n, \delta)$ with $\delta(x,y) = x+y\ \forall x,y\in C_n$. Then $N(S) = \mathrm{End}\,C_n\oplus M_c(C_n)$ is an ab nr with an identity and $|N(S)| = n^2$.

**Pf:** With hypothesis. Since $C_n$ ab and $\delta(x,y) = x+y\ \forall x,y\in C_n$, it is easy to see that $S$ is a homomorphic GSA and $N(S)$ is an ab nr with identity. Now if we let $M_S = \{f_y\in C_n^{C_n} : y\in C_n\}$ where $xf_y := \delta(x,y) = x+y\ \forall x\in C_n$. We then have $N(S) = \langle M_S,\oplus,\circ\rangle = \{\sum\pm f_a : a\in C_n\}$, by the previous result. Consider $\forall a\in C_n$ and $x\in C_n$,
$$x(f_a\oplus(n-1)f_0) = xf_a + \sum_{i=1}^{n-1}xf_0 = x+a+\sum_{i=1}^{n-1}x = a = x\theta_a.$$
So $\forall a\in C_n$, $\theta_a = (f_a\oplus(n-1)f_0)\in N(S)$ and hence $M_c(C_n) = \{\theta_a : a\in C_n\}\subseteq N(S)$.

Now, if we look at any $k\in C_n$, then $\forall x\in C_n$, we have
$$x\Big(\sum_{i=1}^k f_{a_i} - \big(f_{a_1+\cdots+a_k}\oplus(n-1)f_0\big)\Big) = \cdots = kx + a_1+\cdots+a_k - (a_1+\cdots+a_k) - x - (n-1)x = kx$$
$= x\psi_k$ where $\psi_k: C_n\to C_n$ via $x\mapsto x\psi_k = kx$.

---

## 第 16 頁（AAT016，鉛筆）

So $\forall k\in C_n$, $\psi_k\in N(S)$ and since $\psi_k\in\mathrm{End}\,C_n$, we have $\mathrm{End}\,C_n\subseteq N(S)$.
Thus we obtain $\mathrm{End}\,C_n\oplus M_c(C_n)\subseteq N(S)$.

Conversely, let $\alpha\in N(S)$, then $\exists\, a_1,\dots,a_s\in C_n$, $\varepsilon_i = \pm1$ $(i = 1,\dots,s)$ $\ni \alpha = \sum_{i=1}^s\varepsilon_i f_{a_i}$. Since
$$xf_{a_i} = \delta(x,a_i) = x+a_i = xf_0 + x\theta_{a_i} = x(f_0\oplus\theta_{a_i})\quad\forall x\in C_n,$$
and $f_0\in\mathrm{End}\,C_n$, $\theta_{a_i}\in M_c(C_n)$, we have
$$\alpha = \sum_{i=1}^s\varepsilon_i(f_0\oplus\theta_{a_i}) = \sum_{i=1}^s(\varepsilon_i f_0)\oplus(\varepsilon_i\theta_{a_i})\in\mathrm{End}\,C_n\oplus M_c(C_n).$$
Thus we obtain $N(S)\subseteq\mathrm{End}\,C_n\oplus M_c(C_n)$.
$\therefore$ We have $N(S) = \mathrm{End}\,C_n\oplus M_c(C_n)$.
$\because \mathrm{End}\,C_n\cap M_c(C_n) = \{\mathrm{id}_{C_n}\}$（註：應為零映射 $\{\theta_0\}$）
$\therefore |N(S)| = n^2$

Here we extend our previous result to ab gp.

**Theory:** Let $A$ be ab gp of order $m$ and exponent $n$ ($|A| = m$, $\forall a\in A$, $a^n = \mathrm{id}$). If $S = (A,A,\delta)$ with $\delta(x,y) = x+y\ \forall x,y\in A$, then
$$|N(S)| = mn$$
and $N(S)$ is isomorphic to an abstract affine nearring of $C_n\oplus A$ such that $A$ is an $C_n$-module.
