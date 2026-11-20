# AAT 課程筆記（中文版）

> 本版為原文筆記（英文手寫）的中文翻譯，數學式與原文相同。原稿為手寫掃描檔 `AAT001.jpg`～`AAT016.jpg`。
> 縮寫：sgp = 半群（semigroup）、gp = 群（group）、homo = 同態（homomorphism）、nr = 近環（nearring）。
> 翻譯中的 `[?]` 表示原稿無法辨識之處；「（註：…）」為轉錄時加上的說明。

---

## 第 1 頁（AAT001）

**定義：** 半群 $(S,\mu)$ 是一個集合 $S$ 配上一個結合的運算 $\mu$。所謂結合，是指

$$\mu(a,\mu(b,c)) = \mu(\mu(a,b),c)\quad \forall a,b,c\in S$$

或簡寫為：$a\mu(b\mu c) = (a\mu b)\mu c$。

設 $S$ 為集合，$*$ 為 $S$ 上**不具結合性**的二元運算，那麼 $n$ 個元素用 $*$ 組合，共有幾種不同的組合方式？

- $a*b*c$：2 種 — $((a*b)*c)$、$(a*(b*c))$
- $a*b*c*d$：5 種 — $(((a*b)*c)*d)$、$((a*(b*c))*d)$、$((a*b)*(c*d))$、$(a*(b*(c*d)))$、$(a*((b*c)*d))$

（註：此即 Catalan 數。）

**例：** $(\mathbb N,+), (\mathbb Z,+), (\mathbb R,\cdot), (\mathbb C,\cdot),\dots$ 都是半群。
$S$ 為集合，$(P(S),\cup)$、$(P(S),\cap)$ 是半群；$(P(S),\Delta)$ 構成交換群。

$x(g\circ f) = (xg)f$（右作用記法）

### 簡史

- 半群：1900 年以後。
- 近幾十年來，半群理論與自動機理論互相豐富、彼此促進。
- L.A. de Séguier，1904，《Éléments de la Théorie des Groupes Abstraits》（抽象群論基礎）
- 第一篇研究：K. Suschkewitsch，1928：每個有限半群都含有一個單純理想（simple ideal）。
- 參考書：Petrich 1973、✡ Howie 1976、Lallement 1979、Grillet 1995。
- 自動機理論：A. Turing（圖靈機）

**例：** $(\mathbb R,\max)$，其中 $x \max y := \max\{x,y\}\ \forall x,y\in\mathbb R$。
$(M_n(\mathbb R),\cdot)$ 是么半群，$(M_n(\mathbb R),+)$ 是交換群，$(\mathbb R[x],+)$ 是交換群，$(\mathbb R[x],\cdot)$ 是么半群，$(\mathbb R[x],\circ)$ 是么半群。
$S\neq\emptyset$ 為集合，則 $(S^S,\circ)$ 是么半群。
$(S,+)$ 是群 $\Rightarrow (S^S,+,\circ)$ 是近環。
$\|\mathbb N\| = \aleph_0$（阿列夫零），$\|\mathbb R\| = \aleph_1$（阿列夫一）。

**定義：** 設 $(S,\circ)$ 為半群，$x\in S$。

1. 若 $x\circ t = t\circ x = x\ \forall t\in S$，稱 $x$ 為 $S$ 的**零元**。
2. 若 $x\circ t = t\circ x = t\ \forall t\in S$，稱 $x$ 為 $S$ 的**單位元**。
3. 若 $x\circ x = x$，稱 $x$ 為**冪等元**。
4. 若 $(S,\circ)$ 有單位元，則稱 $(S,\circ)$ 為**么半群（monoid）**。
5. 若 $(S,\circ)$ 為么半群，且 $\exists!\, y\in S$ 使 $x\circ y = $ 單位元，則稱 $x$ **可逆**（可逆元）。
6. 若 $(S,\circ)$ 為么半群，且 $\forall s\in S\ \exists!\, t\in S$ 使 $s\circ t = t\circ s = $ 單位元，則 $(S,\circ)$ 構成**群**。

**定義：** 設 $(M,\circ)$ 為么半群，則 $G_M := \{x\in S : x \text{ 可逆}\}$ 稱為 $(M,\circ)$ 的**群核**（單位群）。

**定理：** $(G_M,\circ)$ 是 $(S,\circ)$ 之中的一個群。

若 $x,y\in G_M$，則 $x\circ y$ 的反元素為 $y^{-1}\circ x^{-1}$，故 $x\circ y\in G_M$。
因為 $1_M\circ 1_M = 1_M$，所以 $1_M\in G_M$。
若 $x\in G_M$，則 $x\circ x^{-1} = 1_M = x^{-1}\circ x \Rightarrow x^{-1}\in G_M$。
因此 $(G_M,\circ)$ 構成群。

**例：**

| 么半群 | 群核 |
|---|---|
| $(\mathbb N_0,+)$ | $\{0\}$ |
| $(\mathbb N,\cdot)$ | $\{1\}$ |
| $(\mathbb Z,\cdot)$ | $\{1,-1\}$ |
| $(\mathbb Q,\cdot)$ | $\mathbb Q\setminus\{0\}$ |
| $(M_n(\mathbb R),\cdot)$ | $GL(n,\mathbb R)$ |
| $(S^S,\circ)$ | $\{f\in S^S : f: S\to S \text{ 為雙射}\}$ |
| $(P(X),\Delta)$ | $P(X)$ |
| $(G,\cdot)$ | $G$ |

**註：** 群核越大，么半群就越接近一個群。

問題：$(\mathbb Z/n\mathbb Z,\cdot)$ 的群核是什麼？

---

## 第 2 頁（AAT002）

（群核中）$x$ 的反元素可這樣求：把 $1$ 寫成 $1 = xa + nb$（$a,b\in\mathbb Z$ 適當選取），
$\Rightarrow [1] = [x]\cdot[a] + [n][b] = [x]\cdot[a]$

## 第二章：子半群與同態

一個半群可以有較小的半群作為其子結構（子半群）。$(\mathbb N,\cdot) < (\mathbb Z,\cdot)$

**定義：** 設 $(S,\circ)$ 為半群，$A,B\subseteq S$，定義 $A\circ B := \{a\circ b : a\in A, b\in B\}$。
$A\circ A, A\circ A\circ A,\dots$ 分別記為 $A^2, A^3,\dots$，並記 $\{a\}\circ B := a\circ B := aB$。

**定義：** 設 $(S,\circ)$ 為半群，$\emptyset\neq U\subseteq S$。若 $U^2\subseteq U$，則稱 $U$ 為 $S$ 的**子半群**。
以下記 $(U,\circ)\le(S,\circ)$；運算明確時簡記 $U\le S$，表示 $U$ 是 $S$ 的子半群。

**例：** $(\mathbb N,\cdot)\lneq(\mathbb Z,\cdot)$，$(\mathbb N,+)\lneq(\mathbb Z,+)$，$(\mathbb N,+)\not\le(\mathbb Z,\cdot)$

立刻可以看出：么半群 $S$ 的子半群 $U$ 一般而言不一定是么半群。
**例：** $(\mathbb N,+) < (\mathbb N\cup\{0\},+)$

要特別注意：即使 $U$ 是么半群 $S$ 的子么半群，$U$ 的單位元也不一定等於 $S$ 的單位元。
**例：** $(\{0\},\cdot)\lneq(\mathbb Z,\cdot)$

**定理 2.4：** 半群的子半群之非空交集仍是子半群。

設 $x,y\in\bigcap_{i\in I}S_i$，其中 $S_i\le S$，$I\subseteq\mathbb N$，$i\in I$。
$\Rightarrow x,y\in S_i\ \forall i\in I$。因 $S_i\le S\ \forall i\in I$，得 $x\circ y\in S_i\ \forall i\in I \Rightarrow x\circ y\in\bigcap_{i\in I}S_i$
$\therefore \bigcap_{i\in I}S_i\le S$

**註：** 子半群的聯集一般而言不一定是子半群。
**反例：** $(\mathbb N,+)\lneq(\mathbb Z,+)$，$(\langle 2\rangle,+)\lneq(\mathbb Z,+)$，但 $(\langle 2\rangle\cup\mathbb N,+)\not\le(\mathbb Z,+)$

若 $S\in SGP := \{S : S \text{ 為半群}\}$ 且 $S\neq\emptyset\neq T\subseteq S$，則所有包含 $T$ 的子半群之交集是一個子半群。由定理 2.4，此子半群是包含 $T$ 的最小子半群，記為 $\langle T\rangle$。

由於 $S$ 的子半群（連同 $\emptyset$）構成一個歸納 Moore 系統，因此可以談「生成的子半群」。

**定義 2.5：** $\langle T\rangle$ 稱為由 $T$ **生成**的 $S$ 之子半群。

**註：** 若 $T=\{y\}$，記 $\langle y\rangle$ 代替 $\langle\{y\}\rangle$。顯然 $T$ 是子半群 $\Leftrightarrow \langle T\rangle = T$。

**定理 2.6：** $\forall\, T\subseteq S\in SGP$，$T\neq\emptyset$，
$$\langle T\rangle = \bigcup_{n\in\mathbb N}T^n = \Big\{\prod_{i=1}^m t_i : \{t_i\}_{i=1}^m\subseteq T,\ m\in\mathbb N\Big\}$$

---

## 第 3 頁（AAT003）

$\bigcup_{n\in\mathbb N}T^n\le(S,\circ)$，且由封閉性，任何包含 $T$ 的子半群都包含 $\bigcup_{n\in\mathbb N}T^n$，所以 $\bigcup_{n\in\mathbb N}T^n$ 是 $(S,\circ)$ 中包含 $T$ 的最小子半群。
$\therefore \bigcup_{n\in\mathbb N}T^n = \langle T\rangle$

$T\subseteq V\subseteq S$，$\langle T\rangle = S \Rightarrow \langle V\rangle = S$

我們想找出盡可能小的生成系。

**定義：** 設 $S$ 為半群，若 $\exists\, T\subseteq S$ 使 $|T|<\aleph_0$ 且 $\langle T\rangle = S$，則稱 $S$ 為**有限生成**。

**例：**
- $(\mathbb N,+) = \langle 1\rangle$ 是循環的
- $(\mathbb N,\cdot) = \langle\{1\}\cup\mathbb P\rangle$ 不是有限生成
- $(\mathbb N_0,+) = \langle\{0,1\}\rangle$

**Vorobev 定理：** 有限集 $X$ 上的所有雙射，再加上一個「單純」的非滿射，即可生成 $X^X$：

**定理 2.9：** 設 $X$ 為集合，$|X|\in\mathbb N\setminus\{1\}$，$f\in X^X$ 且 $|f(X)| = |X|-1$。則 $\langle S_X\cup\{f\}\rangle = X^X$。

> Clifford 與 Preston，1953，《Theory of Semigroups》，AMS，第 7 頁習題 10(c)

**定義 2.10：** $(S,\circ),(S',*)\in Sgp$，若 $\forall x,y\in S$，$f(x\circ y) = f(x)*f(y)$，則稱 $f: S\to S'$ 為**同態**。

- 單射同態：**單同態（mono）**
- 滿射同態：**滿同態（epi）**
- 雙射同態：**同構（iso）**

**例：** $f,p: (\mathbb Z,\cdot)\to(\mathbb N_0,\cdot)$，$x\overset{f}{\mapsto}|x|$，$x\overset{p}{\mapsto}0$

$(P(\{1,2,3\}),\cap) \hookrightarrow\!\!\!\!\to (P(\{a,b,c\}),\cap)$ — 同構的半群

---

## 第 4 頁（AAT004，第 3 頁內容的放大重寫版）

**定理 2.9**（Cayley 嵌入；$S_n$：母群，$S^S$：母半群）
$X\in Set$，$|X| = n > 1$，$f\in X^X$ 且 $|f(X)| = n-1$
$$\Rightarrow (X^X,\circ) = \langle S_X\cup\{f\}\rangle$$
（旁註：Wallis formula）

$(12)(23) = (132)$

> 1953 Clifford 與 Preston，《Theory of Semigroups》，AMS 第 7 頁習題 10(c)

**定義 2.10：** $(S,\circ),(S',*)\in Sgp$。若 $\forall x,y\in S$，$f(x\circ y) = f(x)*f(y)$，則稱 $f: S\to S'$ 為同態。

- 單射同態：mono
- 滿射同態：epi
- 雙射同態：iso

**例：** $f: (\mathbb Z,\cdot)\to(\mathbb N_0,\cdot)$，$x\overset{f}{\mapsto}|x|$；$p: (\mathbb Z,\cdot)\to(\mathbb N_0,\cdot)$，$x\overset{p}{\mapsto}0$
$(P(\{1,2,3\}),\cap) \hookrightarrow\!\!\!\!\to (P(\{a,b,c\}),\cap)$

同構的半群可以視為「本質上相同」。

**定義 2.12：** $(S,\circ)\in Sgp$，$\sim$ 為 $S$ 上的等價關係。若
$$a\sim a' \text{ 且 } b\sim b' \Rightarrow a\circ b\sim a'\circ b'$$
則稱 $\sim$ 為 $(S,\circ)$ 上的**同餘關係**。

（習題）求 $|\mathrm{End}(V_4)|$，$V_4 = \mathbb Z_2\times\mathbb Z_2$。

對 $(S,\circ)$ 上的同餘關係 $\sim$，我們在商集 $S/\!\sim$ 上定義二元運算 $\odot$（「分裂」）：
$$[a]\odot[b] = [a\circ b].$$
此定義是良定義的（well-defined）：

---

## 第 5 頁（AAT005）

若 $[a]=[a']$，$[b]=[b']$
$\Rightarrow a\sim a'$，$b\sim b'$
因此 $a\circ b\sim a'\circ b'$
從而 $[a\circ b] = [a'\circ b']$
$\Rightarrow [a]\odot[b] = [a']\odot[b']$

**定義：** 設 $\sim$ 為半群 $(S,\circ)$ 上的同餘關係。$(S/\!\sim,\odot)$ 是一個半群，稱為 $(S,\circ)$ 關於 $\sim$ 的**商半群**（factor sgp / quotient sgp）。

**定理（2.13）：** 給定半群 $(S,\circ)$ 上的同餘關係 $\sim$，映射 $\pi: S\to S/\!\sim$，$x\mapsto[x]$ 是一個滿同態，稱為**典範（自然）滿同態**。

$\odot$ 良定義 $\Rightarrow \forall [a],[b],[c]\in S/\!\sim$，有 $([a]\odot[b])\odot[c] = [a]\odot([b]\odot[c])$
$\therefore (S/\!\sim,\odot)$ 是半群。
$\pi$ 顯然是滿射。
$\pi(a\circ b) = [a\circ b] = [a]\odot[b] = \pi(a)\odot\pi(b)$
$\therefore \pi$ 是同態 $\Rightarrow \pi$ 是滿同態。

**定理 2.14（同態定理）：** $f: (S,\circ)\to(T,*)$ 為滿同態。則由 $a\sim b\Leftrightarrow f(a)=f(b)$ 定義的 $\sim$ 是 $(S,\circ)$ 上的同餘關係，且 $(S/\!\sim,\odot)\cong(T,*)$。

**證明：** 同餘關係：
1. $\forall s\in S$，$f(s)=f(s)\Rightarrow s\sim s$
2. $\forall a,b\in S$，$a\sim b$：$f(a)=f(b)\Leftrightarrow f(b)=f(a)\Leftrightarrow b\sim a$
3. $\forall a,b,c\in S$，$a\sim b\wedge b\sim c\Leftrightarrow f(a)=f(b)\wedge f(b)=f(c)\Rightarrow f(a)=f(c)\Leftrightarrow a\sim c$

由 2.13，存在典範滿同態 $\pi: S\twoheadrightarrow S/\!\sim$，$x\mapsto[x]$，且 $(S/\!\sim,\odot)$ 是商半群。
定義 $\mu: S/\!\sim\ \to T$，$\mu([x]) = f(x)\ \forall x\in S$。
良定義：$[x]=[y]\Rightarrow x\sim y\Rightarrow \mu([x]) = f(x) = f(y) = \mu([y])$
$\forall [x],[y]\in S/\!\sim$，$\mu([x]\odot[y]) = \mu([x\circ y]) = f(x\circ y) = f(x)*f(y) = \mu([x])*\mu([y])$
$\therefore \mu$ 是半群同態，且顯然是滿同態。
$\mu([x]) = \mu([y])\Leftrightarrow x\sim y$
$\therefore \mu$ 是同構。

**定理 2.22（嵌入定理）：** 對任意半群 $(X,\cdot)$，存在 $S$ 使 $(X,\cdot)\hookrightarrow(S^S,\circ)$。

若 $(X,\cdot)$ 是么半群，可取 $S = X$；否則構造 $X^{(1)} := X\cup\{1_X\}$，使 $(X^{(1)},\cdot)$ 成為以 $1_X$ 為單位元的么半群，取 $S = X^{(1)}$。
對 $x\in X$，定義 $f_x: S\to S$，$f_x(a) = x\cdot a\ \forall a\in S$，則 $f_x\in S^S$。
令 $\phi: X\to S^S$，$\phi(x) = f_x\ \forall x\in X$。需證明 $\phi$ 是單同態。
$x,x'\in X$，$\phi(x\cdot x') = f_{xx'} = f_x\circ f_{x'} = \phi(x)\circ\phi(x')$，$\therefore \phi$ 是同態。
$\phi(x) = \phi(x')\Rightarrow f_x = f_{x'}\overset{1_S}{\Rightarrow} x = x'$（代入 $1_S$），$\therefore \phi$ 是單同態。

---

## 第 6 頁（AAT006）

**註：** 我們可以說任何半群都是某個變換（映射、函數）半群的子半群。但這個性質通常既不特別有用，也不自然。很少人會把 $(\mathbb N,+)$ 看成 $(\mathbb N_0^{\mathbb N_0},\circ)$ 的子半群。

## 第三章：自由半群

在線性代數中，常用到一個重要結果：向量空間 $V$ 的基底 $\beta$ 到向量空間 $W$ 的任何映射，都能唯一地延拓為 $V$ 到 $W$ 的線性映射。對半群（以及其他結構）也可以這麼做。具有「基底」$B$ 的半群稱為「$B$ 上的自由半群」。

（旁註：數學有「元素」嗎？）

- $\langle a\rangle$：自由半群
- $\langle a\rangle^* = \{\lambda\}\cup\langle a\rangle$：自由么半群
- $\{a\}$ 為自由基底。$\langle\emptyset\rangle = \{1\} = \{\lambda\}$

**定義 3.1：** 設 $\mathcal S$ 為所有半群構成的類，$F\in\mathcal S$，$\emptyset\neq\beta\subseteq F$。若每個映射 $f: \beta\to S\in\mathcal S$ 都能延拓為唯一的半群同態 $h_f: F\to S$，則稱 $F$ 為 **$\beta$ 上的自由半群**，$\beta$ 稱為 $F$ 的**基底**。$F = F_\beta$。

嚴格來說應寫 $(F,\cdot)$，但以下暫時省略，之後再回來談。定義 3.1 可以形式化地重述如下：

**定義 3.1'：** 設 $F\in\mathcal S$。若 $\forall S\in\mathcal S$，$f\in S^B$，$\exists!\, h\in\mathrm{Hom}(F,S)$ 使 $h|_B = f$，則稱 $F$ 為基底（生成集）$B\subseteq F$ 上的自由半群。對應右邊的交換圖：

```
  B ──ι──> F
   \       |
  f \      | h        f = h∘ι
     ↘     ↓
         S
```

為了更好理解（因為用泛性質語言給出的自由半群抽象定義對初學者相當困難），我們在此稍停，用組合的方式給出自由半群更具體的概念。

**定義 3.1''：** 設 $X\in Set\setminus\{\emptyset\}$，且
$$X^+ := \{(a_1,\dots,a_n) : a_i\in X, 1\le i\le n, n\in\mathbb N\} := \{a_1\cdots a_n : a_i\in X, 1\le i\le n, n\in\mathbb N\}\ \text{（編碼語言的寫法）}$$
在 $X^+$ 上定義**串接**（concatenation）$*$：$a_1\cdots a_n * b_1\cdots b_m := a_1\cdots a_n b_1\cdots b_m$，則 $(X^+,*)$ 是半群，稱為 **$X$ 上的自由半群**。若在 $X$ 中加入空字 $\Lambda$（空字串），就得到 $X$ 上的自由（字）么半群 $X^*$。

**附註 3.2：**
1. $X = \{a\}\Rightarrow (X^+,*)\cong(\mathbb N,+)$
2. $|X|>1\Rightarrow (X^+,*)$ 不可交換。
3. $X^+$ 永遠是無限的。
4. 除了 $\langle\emptyset\rangle$ 之外，沒有有限半群是自由的；因此除了 $\{\lambda\} = \langle\emptyset\rangle$ 之外，沒有有限半群具有（自由）基底。

---

## 第 7 頁（AAT007）

因此自由半群相當「稀少」，但仍然很多，因為每個半群都是某個自由半群的同態像。

現在回到用泛性質語言描述的自由半群理論。許多問題隨即出現：
每個半群都有基底嗎？若有，有幾個？所有基底的基數都相同嗎？
我們可以證明並非每個半群都有基底。但若有基底，則所有基底的基數都相同。

**定理 3.3：** 設 $F$ 為以 $B$ 為基底的自由半群，則 $F = \langle B\rangle$。

因 $B\subseteq F$，考慮交換圖 $B\overset{\iota}{\hookrightarrow}F$，$f: B\to S = \langle B\rangle$（$b\mapsto b$），$h: F\to S$。由自由半群的定義，$\exists!\, h: F\to S$ 把 $f$ 延拓為同態。再考慮另一個交換圖：$\mathrm{id}_F$ 也延拓了 $B\hookrightarrow F$（$\iota$）。因此 $h = \mathrm{id}_F$，且 $F = \langle B\rangle$。

現在正是時候：從一個集合 $B$ 出發，嘗試找一個半群 $F$，使 $B$ 成為 $F$ 的基底。

**定理 3.4：** 對任意集合 $B\neq\emptyset$，存在以 $B$ 為自由基底的半群 $F$。

設 $\emptyset\neq B\in Set$，$F = \{\prod_{i=1}^n b_i : b_i\in B, i=1,\dots,n, n\in\mathbb N\}$，規定
$$\prod_{i=1}^n b_i = \prod_{j=1}^m b'_j \Leftrightarrow n=m \wedge b_t = b'_t,\ t\in\{1,\dots,n\}.$$
對 $x = \prod_{i=1}^n b_i$，$y = \prod_{i=1}^m c_i$（$x,y\in F$，$b_i,c_j\in B$）定義
$$x*y := \prod_{i=1}^n b_i\cdot\prod_{i=1}^m c_i$$
序列上的運算 $*$ 就是把兩個序列並排寫在一起（稱為**串接**或**並置**）。
$(F,*)$ 顯然是半群。需證 $F$ 滿足定義 3.1' 的條件：$B\hookrightarrow F$，$f: B\to S$，其中 $S$ 為半群、$f$ 為任意映射。
定義 $h: F\to S$，$h: \prod_{i=1}^n b_i\mapsto\prod_{i=1}^n f(b_i)$，則 $h|_B = f$ 且 $h\in\mathrm{Hom}(F,S)$。若 $h'\in\mathrm{Hom}(F,S)$ 是 $f$ 的另一個延拓，則
$$h'\Big(\prod_{i=1}^n b_i\Big) = \prod_{i=1}^n h'(b_i) = \prod_{i=1}^n f(b_i)$$
$\therefore h' = h$

**定理 3.5：** 設 $F$、$F'$ 分別為 $B$、$B'$ 上的自由半群，則 $F\cong F'\Leftrightarrow |B| = |B'|$。

「$\Rightarrow$」：設 $h: F\to F'$ 為同構。對 $b\in B$，$h(b) = b'_1\cdots b'_n\in F'$，$b'_i\in B'$，$i=1,\dots,n$。
則 $b = h^{-1}(b'_1\cdots b'_n) = h^{-1}(b'_1)\cdot h^{-1}(b'_2)\cdots h^{-1}(b'_n)$。
故 $n=1$。由表示法的唯一性，$h|_B$ 是 $B$ 到 $B'$ 的雙射，$|B| = |B'|$。

「$\Leftarrow$」：逆向論證即得。

（旁註：8 階的群有幾個？$\mathbb Z_8$、$\mathbb Z_4\times\mathbb Z_2$、$\mathbb Z_2^3$、$V_4\times\mathbb Z_2$、$D_8$）

**推論 3.6：** 若 $F$、$F'$ 都是 $B$ 上的自由半群，則 $F\cong F'$。所以可以說「那個」$B$ 上的自由半群。此外，

**推論 3.7：** 若 $F$ 有兩個基底 $B$ 與 $B'$，則 $|B| = |B'|$。因此自由半群的所有基底都有相同的基數。

---

## 第 8 頁（AAT008）

所以對任意基數 $\alpha$，都存在一個自由半群 $F_\alpha$，其基底 $B$ 滿足 $|B| = \alpha$。由此回到附註 3.2 (iv)。

**定理 3.8：** 設 $S\in Sgp$，$S = \langle E\rangle$，其中 $E$ 是生成系（不一定是 $S$ 的基底）。則 $S$ 是 $F_{|E|}\ (=F_E)$ 的同態像。

考慮交換圖 $E\overset{\text{典範}}{\hookrightarrow}F_E$，$\iota: E\to\langle E\rangle$，$h: F_E\to\langle E\rangle$。則 $h: F_E\to S$ 是 $\iota$ 的延拓。
$\therefore E = \iota(E) = h(E)\subseteq h(F_E)\le\langle E\rangle = S$，因而 $S = \langle E\rangle\subseteq h(F_E)$
$\therefore h(F_E) = S$，$\therefore h$ 是滿同態。

另一個證明：
令 $h: E^*\to S$，$h: x_1\cdots x_n\mapsto x_1\circ x_2\circ\cdots\circ x_n$。
則 $h$ 是半群同態，且 $E = h(E)\subseteq h(E^*)\le S$，因此 $S = \langle E\rangle\subseteq h(E^*)$
$\therefore h(E^*) = S$，$\therefore h$ 是滿同態。

這完整解釋了「自由半群」$F_E$（或 $E^*$）之所以「自由」：它不受任何限制關係（例如交換律）約束。透過「加入」這類關係，可以得到任何半群。$F_{|E|}$ 是由大小為 $\alpha$ 的生成集（生成系）所能得到的最一般的半群。定理 3.8 讓我們能用生成集與關係來描述半群。

**定義 3.9：** 設 $S\in Sgp$ 由 $X$ 生成，$R$ 為 $F_X = X^*$ 上的關係。若
$$(X:R) := F_X/\!\sim_R\ = X^*/\!\sim_R\ \cong S,$$
則稱 $(X:R)$ 為 $S$ 的一個**表現**（presentation），通常記為 $S = (X:R)$。

**例：** $(\{x,y\} : \{(x^2,1),(y^3,1),(xy^2,yx)\})\cong S_3$

$R$ 的元素稱為**定義關係**，儘管它們根本不是關係。定理 3.8 保證每個半群都有表現。注意一個半群可以有許多不同的表現。

**例 3.10：** 設 $(S,\circ) = (\mathbb Z_4,\cdot)$，$X = \{x_1,x_2\}$，
$$R = \{(x_1x_2, x_2x_1), (x_2x_2x_1, x_1), (x_2x_2x_2, x_2), (x_1x_1x_1, x_1x_1), (x_1x_2, x_1)\}$$
考慮等價類 $a_0 := [x_1]$、$a_1 := [x_2]$、$a_2 := [x_1x_1]$、$a_3 := [x_2x_2]\in F_X/\!\sim_R$，運算為 $*$。
這些類之間的運算如下：

| $*$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ |
|---|---|---|---|---|
| $a_0$ | $a_2$ | $a_0$ | $a_2$ | $a_0$ |
| $a_1$ | $a_0$ | $a_3$ | $a_2$ | $a_1$ |
| $a_2$ | $a_2$ | $a_2$ | $a_2$ | $a_2$ |
| $a_3$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ |

$a_0*a_0 = [x_1]*[x_1] = [x_1x_1] = a_2$
$a_0*a_1 = [x_1]*[x_2] = [x_1x_2] = [x_1] = a_0$
以此類推，得 $F_X/\!\sim_R\ \cong S$，同構為 $\varphi: a_0\mapsto 2$，$a_1\mapsto 3$，$a_2\mapsto 0$，$a_3\mapsto 1$。

以上做法同樣適用於么半群、群、交換群、模、代數等類別，分別得到自由么半群、自由群、自由交換群、自由模、自由代數等。
以 $X$ 為基底的自由么半群記為 $X_* = X^*\cup\{\lambda\}$，只是多加一個「空字（空字串）」$\lambda$。
再次指出：自由半群 $X^* = \{a\}^*\cong(\mathbb N,+)$，自由么半群 $X_* = \{a\}_*\cong(\mathbb N_0,+)$，而 $X = \{a\}$ 上的自由（交換）群同構於 $(\mathbb Z,+)$。

（註：此處記號與定義 3.1'' 不同——這裡 $X^*$ 指自由半群，$X_*$ 指自由么半群。）

表現通常是描述半群最簡潔的方式，也是在電腦上研究半群與群的方法。

## 第四章：半群與自動機

自動機與機器出現在各種領域，例如計算機、電腦、換錢機、電話交換機、電梯開關控制等。我們可以用一個「黑盒子」來表示所有一般自動機的共同之處。

**例：** 可口可樂自動販賣機 $\mathcal A$：
可容納 5 瓶可口可樂。把它定義成自動機：狀態 $z$ 表示「$\mathcal A$ 裡有 $z$ 瓶可口可樂」；輸入為「沒有投幣」、「投入正確硬幣」、「投入錯誤硬幣」；輸出為「掉出一瓶可口可樂」、「無輸出」、「退出硬幣」。完成狀態表與狀態圖。

---

## 第 9 頁（AAT009）

**解：**

**(I) 可口可樂自動機 $\mathcal A$ 的表：**

- 狀態集 $Z = \{0,1,2,3,4,5\}$，即可樂瓶數的集合。
- 輸入集 $I = \{n,c,w\}$，$n :=$「沒有投幣」，$c :=$「投入正確硬幣」，$w :=$「投入錯誤硬幣」。
- 輸出集 $B = \{x,y,s\}$，$x :=$「無輸出」，$y :=$「退出硬幣」，$s :=$「掉出一瓶可口可樂」。

轉移函數 $\delta: Z\times I\to Z$（又稱下一步函數）：

| $\delta$（I \ Z） | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
| $c$ | 0 | 0 | 1 | 2 | 3 | 4 |
| $w$ | 0 | 1 | 2 | 3 | 4 | 5 |

輸出函數 $\lambda: Z\times I\to B$：

| $\lambda$（I \ Z） | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $n$ | x | x | x | x | x | x |
| $c$ | y | s | s | s | s | s |
| $w$ | y | y | y | y | y | y |

$$\mathcal A = (Z, I, B, \delta, \lambda)$$

**(II) 可口可樂自動機 $\mathcal A$ 的狀態圖：**

```
 每個狀態 z (z = 0,1,2,3,4,5) 都有自迴圈： n;x 與 w;y

  ┌ c;y ┐
  └─> (0) <─c;s─ (1) <─c;s─ (2) <─c;s─ (3) <─c;s─ (4) <─c;s─ (5)
```

$n$ 與 $w$ 在每個 $z\in Z$ 都形成相同的自迴圈，必須加到圖上；$\delta: Z\times I\to Z$，$\lambda: Z\times I\to B$。

**定義 4.1（半自動機）：** 半自動機 $\mathcal S = (Z,I,\delta)$ 由兩個非空集合 $Z$（狀態集）、$I$（輸入集）及函數 $\delta: Z\times I\to Z$（下一狀態函數，或稱轉移函數）組成。

若需要研究輸出，就需要自動機而非半自動機。

**定義 4.2：** 自動機是一個五元組 $\mathcal A = (Z,I,B,\delta,\lambda)$，其中 $(Z,I,\delta)$ 是半自動機，$B$ 為輸出集（輸出字母表），$\lambda: Z\times I\to B$ 為輸出函數。

定義 4.1、4.2 相當抽象。

**定義 4.3：** 若 $Z, I, B$ 都是有限集，則稱自動機（或半自動機）為**有限的**。有限自動機稱為 **Mealy 自動機**。若固定一個特殊狀態 $z_0\in Z$，則稱此（半）自動機為**有初始狀態的**，$z_0$ 稱為初始狀態；要強調初始狀態時記為 $(Z,I,\delta,z_0)$。若 $\lambda$ 只依賴於 $z$，則稱為 **Moore 自動機**。

**例 4.4：**
1. 把你大腦的一部分描述成一個半自動機，使本課程的定理集合與 $\delta$ 描述「讀書」。
2. 你能把 (I) 的半自動機解釋成一台電腦嗎？
3. 若把 (I) 的半自動機視為自動機，可能的解釋為何？
4. 同 (III)，但解釋為有初始狀態的自動機。

**解：**
1. $I$：本講義所有定理的集合。$Z = P(I)$，$z\in Z$ 為 $I$ 中「已經知道」的定理之集合。$\delta(z,\alpha) := z\cup\{\alpha\}$：「把定理 $\alpha$ 加入已知」。
2. 可以。輸入：「定理」，$z$：「儲存中的定理」，$\delta(z,\alpha)$：「把定理 $\alpha$ 加入儲存中的定理 $z$」。
3. $B$：定理的清單，$\lambda(z,a)$：「已學定理表」，包含 $a$ 與 $z$ 中的定理。
4. 例如 $z_0 = \emptyset$ 可表示你一個定理都不知道。

在電腦中，只考慮單一輸入訊號是相當不自然的。程式是由輸入字母表中的元素組成的序列。因此合理的做法是考慮輸入集 $I$ 中元素所有有限序列（包含空序列 $\lambda$）的集合。換句話說，在自動機的研究中，**我們把輸入集 $I$ 擴充為以 $\lambda$ 為單位元的自由么半群 $I_*$。**

同時也把 $\delta: Z\times I\to Z$ 擴充為 $\delta^*: Z\times I^*\to Z$：$\delta(z,a)\longrightarrow\delta^*(z,a_1\cdots a_n)$；把 $\lambda: Z\times I\to B$ 擴充為 $\lambda^*: Z\times I^*\to B^*$：$\lambda(z,a)\longrightarrow\lambda^*(z,a_1\cdots a_n)$。於是半自動機 $\mathcal S = (Z,I,\delta)$（自動機 $\mathcal A = (Z,I,B,\delta,\lambda)$）擴充為新的半自動機 $\mathcal S^* = (Z,I^*,\delta^*)$（自動機 $\mathcal A^* = (Z,I^*,B^*,\delta^*,\lambda^*)$）。

---

## 第 10 頁（AAT010，鉛筆）

設 $z\in Z$，$a_1,\dots,a_n\in I$，就能輕易描述 $\mathcal S$ 與 $\mathcal A$ 的作用：

$$\begin{aligned}
z_1 &= z\\
z_2 &:= \delta(z_1,a_1)\\
z_3 &:= \delta^*(z_1,a_1a_2) = \delta(\delta(z_1,a_1),a_2) = \delta(z_2,a_2)\\
z_4 &:= \delta(z_3,a_3)\\
&\ \ \vdots\\
z_{n+1} &:= \delta(z_n,a_n)
\end{aligned}$$

一般而言：
$$\delta^*(z,a_1\cdots a_n) = \delta(\delta(\cdots\delta(\delta(z,a_1),a_2)\cdots,a_{n-1}),a_n)$$
以及
$$\lambda^*(z,a_1\cdots a_n) = \lambda(z_1,a_1)\cdots\lambda(z_n,a_n)$$
$\delta^*(z,\lambda) = z$，$\lambda^*(z,\lambda) = \lambda$

一個非常有名的結果：**任何（半）自動機都決定一個么半群；反之，任何么半群都能產生一個（半）自動機。**

> 1987–88《Computer Program for Investigating Syntactic Nearrings of Finite Group-Semiautomaton》（研究有限群半自動機之句法近環的電腦程式），1988，Bulletin of the Institute of Mathematics Academia [Sinica?]，vol 16, no 4, Dec 1988，pp. 295–304

$(P(X),\Delta,\cap)$ 構成環，其中 $\Delta$ 為對稱差。

**摘要：** 設 $S = (C_n, C_n, \delta)$ 為群半自動機（GSA），$\delta(x,y) = x+y$；$N(S)$ 為變換近環 $(M(G),+,\circ)$ 的子近環（事實上稱為 GSA $S$ 的句法近環）。
$$N(S) = N(C_n) = \mathrm{End}\,C_n\oplus M_c(C_n)$$
此外，$|N(C_n)| = n^2$。

**引言與預備知識：**

**例：** $G = (C_2,+)$，以如下方式定義 $(G^G,\oplus,\circ)$：$\forall f,g\in G^G$，$x\in G$，
$$x(f\oplus g) = xf + xg,\qquad x(f\circ g) = (xf)g,$$
得到以下兩張表（id 恆等、inv 交換 0↔1、T 常數 1、F 常數 0）：

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

$(G^G,\oplus)$ 是交換群，$(G^G,\circ)$ 是不可交換半群。

左分配律成立：$f_1\circ(f_2\oplus f_3) = (f_1\circ f_2)\oplus(f_1\circ f_3)$。
但右分配律一般不成立，$(f_1\oplus f_2)\circ f_3\neq(f_1\circ f_3)\oplus(f_2\circ f_3)$：
$$(\mathrm{id}\oplus\mathrm{inv})\circ T = T\neq F = (\mathrm{id}\circ T)\oplus(\mathrm{inv}\circ T)$$

藉由上例，接著給出近環的抽象定義。

---

## 第 11 頁（AAT011，鉛筆）

（Fastringe，德文「近環」）

**定義 1：** **近環**是一個三元組 $(N,+,\cdot)$，$+$ 與 $\cdot$ 為集合 $N$ 上的二元運算，滿足
1. $(N,+)$ 是群
2. $(N,\cdot)$ 是半群
3. $\forall a,b,c\in N$，$a\cdot(b+c) = a\cdot b + a\cdot c$。

事實上，上述近環稱為**左近環**。若把 (III) 換成 (III')：$\forall a,b,c\in N$，$(a+b)\cdot c = a\cdot c + b\cdot c$，則稱 $(N,+,\cdot)$ 為**右近環**。

**定義 2：** 對近環 $(N,+,\cdot)$
1. 若 $(N,+,\cdot)$ 滿足 (III')，則稱為**分配近環**。
2. 若 $(N,+)$ 可交換，則稱為**交換（加法）近環**。
3. 若 $(N,\cdot)$ 可交換，則稱為**可交換近環**。
4. 若 $0_N x = x 0_N = 0_N\ \forall x\in N$，則稱 $N$ 為**零對稱近環**。
5. 若 $S\subseteq N$ 且 $(S,+,\cdot)$ 構成近環，則稱 $(S,+,\cdot)$ 為 $(N,+,\cdot)$ 的**子近環**，簡記 $S\le N$。
6. 若 $(N^*,\cdot)$ 構成群，其中 $N^* = N\setminus\{0_N\}$，則稱 $(N,+,\cdot)$ 為**左近體**（left nearfield）。

**例：** $G = (S_3,+)$，$\mathrm{End}\,G = \{f : f\in S_3^{S_3}, (x+y)f = xf + yf\ \forall x,y\in S_3\}$
問題：$\mathrm{End}\,G$ 是什麼？提示：$|\mathrm{End}\,G| = 10$
$E(S_3) := \langle\mathrm{End}\,S_3,\oplus,\circ\rangle$ 有 54 個元素。$|S_3^{S_3}| = 46656$
$|\mathrm{End}\,S_4| = 58$，$|E(S_4)| = 2^{35}\cdot 3^3$ [?]

**例：** $(\{0,1\},+,\cdot)$，運算表為

| + | 0 | 1 |
|---|---|---|
| **0** | 0 | 1 |
| **1** | 1 | 0 |

| · | 0 | 1 |
|---|---|---|
| **0** | 0 | 0 |
| **1** | 0 | 1 |

是一個近體。

**定義：** 對半自動機 $\mathcal S = (Z,I,\delta)$，若 $(Z,+)$ 是群，則稱 $\mathcal S$ 為**群半自動機（GSA）**，此時記 $Z = G$。

給定任一 $\mathcal S$，有 $\{f_a\in G^G : a\in I\}$，其中 $f_a: x\mapsto\delta(x,a)\ \forall x\in G$。若把 $I$ 擴充為 $I$ 上的自由么半群 $I^*$，則得到 $f_{ab} = f_a\circ f_b\ \forall a,b\in I$，因為 $\forall x\in G$，
$$xf_{ab} = \delta^*(x,ab) = \delta(\delta(x,a),b) = \delta(xf_a,b) = (xf_a)f_b = x(f_a\circ f_b).$$
因此映射 $\theta: I^*\to M_S$，$a\mapsto f_a$（即 $a\theta = f_a$）是么半群同態（原稿寫「單同態」），且 $f_\lambda = \mathrm{id}_G$，其中 $M_S = \{f_a : a\in I^*\}$ 稱為 **GSA $S$ 的么半群**，$\lambda$ 為空字串。

所以當 $G$ 是群時，可以用逐點加法談 $f_a$ 與 $f_b$ 的和，即 $x(f_a\oplus f_b) = xf_a + xf_b\ \forall x\in G$。

很自然地，可以考慮 $\{f_a : a\in I^*\}\cup\{\mathrm{id}_G\}$（或簡單地 $\{f_a : a\in I\}\cup\{\mathrm{id}_G\}$）中元素的和與積，最終得到的結構是左近環。

**定義：** 設 $S = (G,I,\delta)$ 為 GSA。由 $\{f_a : a\in I\}\cup\{\mathrm{id}_G\}$ 生成的 $M(G)$ 之子近環 $N(S)$，稱為**句法近環**（syntactic nearring）。

---

## 第 12 頁（AAT012，鉛筆，僅右欄有字）

### $N(S)$ 的結構

**定義 A：** 設 $G, I$ 為加法群，$\delta: G\times I\to G$ 為同態，則稱 $S = (G,I,\delta)$ 為**同態群半自動機**（homomorphic GSA）。

因為
$$xf_a = \delta(x,a) = \delta((x,0)+(0,a)) = \delta(x,0)+\delta(0,a) = xf_0 + 0f_a\ \big(= x(f_0+\bar f_a)\big),\qquad 0f_a = x\bar f_a\ \ \forall x\in G$$
得到 $f_a = f_0 + \bar f_a$，其中 $\bar f_a: x\mapsto 0f_a\ \forall x\in G$（常數映射）。

**定理 B**（G. Hofer 與 G. Pilz）：設 $S = (G,I,\delta)$ 為同態群半自動機，則
$$N(S) = \Big\{\sum\pm f_{a_i} : a_i\in I^*\Big\}$$

藉助定理 B，我們以下面的例子開始探討我們的演算法：

**例 C：** 設 $p\in\mathbb P\setminus\{2\}$ 為奇質數（特別取 $p = 5$）。設 $S = (C_p, C_p, \delta)$，$\delta: (x,y)\mapsto x+y$。

---

## 第 13 頁（AAT013，鉛筆）

則 $M_S = \{f_0, f_1,\dots,f_{p-1}\}$（$p=5$：$M_S = \{f_0,f_1,f_2,f_3,f_4\}$）

（$(\cdots)_c$ 為輪換記法）
- $f_0 = (1)$
- $f_1 = (0\,1\,2\cdots(p-1))_c$
- $f_2 = (0\,2\,4\cdots(p-1)\,1\,3\cdots(p-2))_c$
- $\ \vdots$
- $f_{p-1} = (0\,(p-1)\,(p-2)\cdots 2\,1)_c$

因此很容易看出 $(M_S,\circ)\cong(C_p,+)$。

接著進行以下計算（$p=5$；不帶下標 $c$ 的五位數為一行式記法，依序表示 $0,1,2,3,4$ 的像）：

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

$M_S = \{\theta_i, f_j, a_k : i = 0,\dots,4,\ j = 0,\dots,4,\ k = 1,\dots,15\}$ 是近環，且 $|M_S| = p^2$。

$$N(S) = \mathrm{End}\,C_5\oplus M_c(C_5) = \mathrm{End}\,C_5 + M_c(C_5)$$

作為群，$N(S)$ 是環 $(\mathrm{End}\,C_5,+,\circ)$ 與常數近環 $(M_c(C_5),+,\circ)$ 的直和。

取 $p = 3$，$S = (C_3, C_3, \delta)$，$M_S = \{f_0,f_1,f_2\}$，其中 $f_a := \lambda x.\delta(x,a) = \lambda x.\,x+a$。
$$N(S) = \langle M_S,\oplus,\circ\rangle = \langle M_S,\oplus\rangle$$
- $f_0 = (012) = (1)_c$，$f_1 = (120)$，$f_2 = (201)$
- $a_1 = 2f_0 = (021)$，$a_2 = 2f_1 = (210)$，$a_3 = 2f_2 = (102)$
- $\theta_0 = f_0 + a_1 = (000)$，$\theta_2 = f_0 + a_2 = (222)$，$\theta_1 = f_0 + a_3 = (111)$

$\{\theta_0, f_0, a_1\}$，$\{\theta_0,\theta_1,\theta_2\}$

$$N(S) = \mathrm{End}\,C_3 + M_c(C_3)$$

---

## 第 14 頁（AAT014，鉛筆，運算表）

本頁全是運算表（$\{\theta_0,f_0,a_1\}$、$\{\theta_0,\theta_1,\theta_2\}$ 以及 9 個元素的 $N(S)$ 全表），**表格內容與原文版相同，請切換到「原文」檢視。**

重點：
- $(\mathrm{End}\,C_3,\oplus,\circ)\cong(C_3,+,\cdot)$ — 自同態環
- $M_c(C_3)$ 是常數近環

設 $K = (\{0,a,b,c\},+)$ 為 Klein 四元群（Vierergruppe）。
$$\mathcal K = (K, K, \delta)$$

| + | 0 | a | b | c |
|---|---|---|---|---|
| **0** | 0 | a | b | c |
| **a** | a | 0 | c | b |
| **b** | b | c | 0 | a |
| **c** | c | b | a | 0 |

$\delta(x,y) = x+y\ \forall x,y\in K$。$N(\mathcal K)$ 是什麼？

---

## 第 15 頁（AAT015，鉛筆）

**解：** $M_S = \{f_a: K\to K : a\in K\}$，$xf_a = \delta(x,a) := x+a\ \forall x\in K$

- $f_0 = (0abc)$，$f_a = (a0cb)$，$f_b = (bc0a)$，$f_c = (cba0)$
- $2f_0 = 2f_a = 2f_b = 2f_c = \theta_0$
- $f_0+f_a = f_b+f_c = (aaaa) = \theta_a$
- $f_0+f_b = f_a+f_c = (bbbb) = \theta_b$
- $f_0+f_c = f_a+f_b = (cccc) = \theta_c$

$$\therefore N(\mathcal K) = \{\theta_0,\theta_a,\theta_b,\theta_c,f_0,f_a,f_b,f_c\}\overset{\oplus,\circ}{\cong}(\{\theta_0,f_0\},\oplus,\circ)\oplus(M_c(K),\oplus,\circ)$$
其中 $M_c(K) = \{\theta_0,\theta_a,\theta_b,\theta_c\}$。

（$\oplus$ 與 $\circ$ 運算表與原文版相同，請切換到「原文」檢視。）

$(\mathrm{End}\,\mathbb Z_n,\oplus,\circ)\cong(\mathbb Z_n,+,\cdot)$

**主定理：** 設 $n\in\mathbb N$，$S = (C_n, C_n, \delta)$，$\delta(x,y) = x+y\ \forall x,y\in C_n$。則 $N(S) = \mathrm{End}\,C_n\oplus M_c(C_n)$ 是具單位元的交換（加法）近環，且 $|N(S)| = n^2$。

**證明：** 依假設，因 $C_n$ 是交換群且 $\delta(x,y) = x+y\ \forall x,y\in C_n$，容易看出 $S$ 是同態群半自動機，且 $N(S)$ 是具單位元的交換近環。令 $M_S = \{f_y\in C_n^{C_n} : y\in C_n\}$，其中 $xf_y := \delta(x,y) = x+y\ \forall x\in C_n$。由前面的結果（定理 B），$N(S) = \langle M_S,\oplus,\circ\rangle = \{\sum\pm f_a : a\in C_n\}$。對任意 $a\in C_n$ 與 $x\in C_n$，
$$x(f_a\oplus(n-1)f_0) = xf_a + \sum_{i=1}^{n-1}xf_0 = x+a+\sum_{i=1}^{n-1}x = a = x\theta_a.$$
所以 $\forall a\in C_n$，$\theta_a = (f_a\oplus(n-1)f_0)\in N(S)$，因此 $M_c(C_n) = \{\theta_a : a\in C_n\}\subseteq N(S)$。

接著看任意 $k\in C_n$，則 $\forall x\in C_n$，
$$x\Big(\sum_{i=1}^k f_{a_i} - \big(f_{a_1+\cdots+a_k}\oplus(n-1)f_0\big)\Big) = \cdots = kx + a_1+\cdots+a_k - (a_1+\cdots+a_k) - x - (n-1)x = kx$$
$= x\psi_k$，其中 $\psi_k: C_n\to C_n$，$x\mapsto x\psi_k = kx$。

---

## 第 16 頁（AAT016，鉛筆）

所以 $\forall k\in C_n$，$\psi_k\in N(S)$；又因 $\psi_k\in\mathrm{End}\,C_n$，得 $\mathrm{End}\,C_n\subseteq N(S)$。
於是 $\mathrm{End}\,C_n\oplus M_c(C_n)\subseteq N(S)$。

反之，設 $\alpha\in N(S)$，則存在 $a_1,\dots,a_s\in C_n$，$\varepsilon_i = \pm1$（$i = 1,\dots,s$），使 $\alpha = \sum_{i=1}^s\varepsilon_i f_{a_i}$。因為
$$xf_{a_i} = \delta(x,a_i) = x+a_i = xf_0 + x\theta_{a_i} = x(f_0\oplus\theta_{a_i})\quad\forall x\in C_n,$$
且 $f_0\in\mathrm{End}\,C_n$，$\theta_{a_i}\in M_c(C_n)$，得
$$\alpha = \sum_{i=1}^s\varepsilon_i(f_0\oplus\theta_{a_i}) = \sum_{i=1}^s(\varepsilon_i f_0)\oplus(\varepsilon_i\theta_{a_i})\in\mathrm{End}\,C_n\oplus M_c(C_n).$$
於是 $N(S)\subseteq\mathrm{End}\,C_n\oplus M_c(C_n)$。
$\therefore N(S) = \mathrm{End}\,C_n\oplus M_c(C_n)$。
$\because \mathrm{End}\,C_n\cap M_c(C_n) = \{\mathrm{id}_{C_n}\}$（註：應為零映射 $\{\theta_0\}$）
$\therefore |N(S)| = n^2$

以下把前面的結果推廣到交換群。

**定理：** 設 $A$ 為階 $m$、指數（exponent）$n$ 的交換群（$|A| = m$，$\forall a\in A$，$a^n = \mathrm{id}$）。若 $S = (A,A,\delta)$，$\delta(x,y) = x+y\ \forall x,y\in A$，則
$$|N(S)| = mn$$
且 $N(S)$ 同構於 $C_n\oplus A$ 上的一個抽象仿射近環，其中 $A$ 為 $C_n$-模。
