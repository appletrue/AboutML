` 以下文档在markdown 本地文档中生效,在github 页面不现实渲染效果.`

# **如何在Markdown中书写数学公式**

一般一些扩展的`Markdown`语法支持采用`LaTex`语法写数学公式，而在网页中使用`Mathjax`插件来显示数学公式。

## 插入数学公式

在Markdown中插入数学公式的语法是`$数学公式$`和`$$数学公式$$`。

**行内公式**是可以让公式在文中与文字或其他东西混编，不独占一行。

- **示例**

  ```
  质能方程$E = mc^2$
  ```

- **显示**

  > 质能方程$E=mc^2E=mc^2$

**独立公式**使公式单独占一行，不与文中其他文字等混编。

- **示例**

  ```
  质能方程$$E = mc^2$$
  $${\color{Blue}x^2}+{\color{YellowOrange}2x}-{\color{OliveGreen}1}$$
  ```

- **显示**

  > 质能方程
  > $$E = mc^2$$
  > $${\color{Blue}x^2}+{\color{YellowOrange}2x}-{\color{OliveGreen}1}$$

### 普通公式

普通的加减乘除数学公式的输入方法与平常的书写一样。

- **示例**

  ```
  $$x = 100 * y + z - 10 / 33 + 10 % 3$$
  ```

- **显示**

  > x=100∗y+z−10/33+10x=100∗y+z−10/33+10

### 上下标

使用`^`来表示上标，`_`来表示下标，同时如果上下标的内容多于一个字符，可以使用`{}`来将这些内容括起来当做一个整体。
与此同时，上下标是可以嵌套的。

- **示例**
  ```
  $$x = a_{1}^n + a_{2}^n + a_{3}^n$$
  ```
- **显示**
  >$x = a_{1}^n + a_{2}^n + a_{3}^n$

如果希望左右两边都能有上下标，可以使用`\sideset`语法

- **示例**

  ```
  $$\sideset{^1_2}{^3_4}A$$
  ```
- **显示**
  > $\sideset{^1_2}{^3_4}A$

### 括号

`()`，`[]`和`|`都表示它们自己，但是`{}`因为有特殊作用因此当需要显示大括号时一般使用`\lbrace \rbrace`来表示。

- **示例**
  ```
  $$f(x, y) = 100 * \lbrace[(x + y) * 3] - 5\rbrace$$
  ```
- **显示**

  >  $$f(x, y) = 100 * \lbrace[(x + y) * 3] - 5\rbrace$$

###  分数

分数使用`\frac{分母}{分子}`这样的语法，不过推荐使用`\cfrac`来代替`\frac`，显示公式不会太挤。

- **示例**

  ```
  $$\frac{1}{3} 与 \cfrac{1}{3}$$
  ```

- **显示**

  >  $$\frac{1}{3} 与 \cfrac{1}{3}$$

### 开方

开方使用`\sqrt[次数]{被开方数}`这样的语法

- **示例**

  ```
  $$\sqrt[3]{X}$$
  $$\sqrt{5 - x}$$
  ```

- **显示**

 > 
 >  $$\sqrt[3]{X}$$
 >  $$\sqrt{5 - x}$$

## 希腊字母

| 代码       | 大写  | 代码       | 小写 |
| ---------- | ---- | ---------- | ---- |
| `A`        | AA   | `\alpha`   | αα   |
| `B`        | BB   | `\beta`    | ββ   |
| `\Gamma`   | ΓΓ   | `\gamma`   | γγ   |
| `\Delta`   | ΔΔ   | `\delta`   | δδ   |
| `E`        | EE   | `\epsilon` | ϵϵ   |
| `Z`        | ZZ   | `\zeta`    | ζζ   |
| `H`        | HH   | `\eta`     | ηη   |
| `\Theta`   | ΘΘ   | `\theta`   | θθ   |
| `I`        | II   | `\iota`    | ιι   |
| `K`        | KK   | `\kappa`   | κκ   |
| `\Lambda`  | ΛΛ   | `\lambda`  | λλ   |
| `M`        | MM   | `\mu`      | μμ   |
| `N`        | NN   | `\nu`      | νν   |
| `\Xi`      | ΞΞ   | `\xi`      | ξξ   |
| `O`        | OO   | `\omicron` | οο   |
| `\Pi`      | ΠΠ   | `\pi`      | ππ   |
| `P`        | PP   | `\rho`     | ρρ   |
| `\Sigma`   | ΣΣ   | `\sigma`   | σσ   |
| `T`        | TT   | `\tau`     | ττ   |
| `\Upsilon` | ΥΥ   | `\upsilon` | υυ   |
| `\Phi`     | ΦΦ   | `\phi`     | ϕϕ   |
| `X`        | XX   | `\chi`     | χχ   |
| `\Psi`     | ΨΨ   | `\psi`     | ψψ   |
| `\Omega`   | ΩΩ   | `\omega`   | ωω   |

## 其他字符

### 关系运算符

| 符号   | 代码        |符号   | 代码|符号   | 代码|
| ---- | ------------|------|------|------|------|
| ±±   | `\pm`       | ××   | `\times`     |  ∐∐   | `\coprod`    |
| ÷÷   | `\div`      | ∑∑   | `\sum`       |∏∏   | `\prod`      |
| ∣∣  | `\mid`     | ≡≡   | `\equiv`     | ∤∤   | `\nmid`      |
|  ≈≈   | `\approx`  | ⋅⋅   | `\cdot`      |≠≠   | `\neq`       |
| ∘∘   | `\circ`      |≤≤   | `\leq`       | ≥≥   | `\geq`       |
| ∗∗   | `\ast`   | ⨀⨀   | `\bigodot`   |⨁⨁   | `\bigoplus`  |
| ⨂⨂   | `\bigotimes` || | | | 

### 集合运算符

| 符号   | 代码   |  符号   | 代码   |   符号   | 代码   |
| ---- | ----------- |---- | ----------- |---- | ----------- |
| ∅∅   | `\emptyset` | ∈∈ | `\in`     | ∉∉   | `\notin`  |  
| ⊂⊂   | `\subset`   | ⊃⊃  | `\supset` | ⊆⊆   | `\subseteq` |
| ⊇⊇   | `\supseteq` | ⋂⋂  | `\bigcap` | ⋃⋃   | `\bigcup`   |
| ⋁⋁   | `\bigvee`   | ⋀⋀   | `\bigwedge` | ⨄⨄   | `\biguplus` |
| ⨆⨆   | `\bigsqcup` |||||

### 对数运算符

| 符号     | 代码     |
| ------ | ------ |
| loglog | `\log` |
| lglg   | `\lg`  |
| lnln   | `\ln`  |

### 三角运算符

| 符号     | 代码    |符号   | 代码     |
| ------ | -------- |------ | -------- |
| ⊥⊥     | `\bot` | ∠∠   | `\angle` |
| sinsin | `\sin`   | coscos | `\cos`   |
| tantan | `\tan`   | cotcot | `\cot`   |
| secsec | `\sec`   | csccsc | `\csc`   |

### 微积分运算符

| 符号     | 代码     |符号     | 代码     |
| ------ | ------------ |------ | ------------ |
| ′′     | `\prime`     | ∫∫     | `\int`       |
| ∬∬     | `\iint`    | ∭∭     | `\iiint`  |
| ∬∬⨌   | `\iiiint` | ∮∮     | `\oint`    |
| limlim | `\lim`       | ∞∞     | `\infty`     |
| ∇∇     | `\nabla`     | dd     | `\mathrm{d}` |

## 大型运算符

## 下标、上标、积分

| 功能                                       | 语法                                | 渲染                                 |
| ---------------------------------------- | ---------------------------------------- | -------------------------------- |
| 上标                                     | `a^2`                                   | $a^2$                           |
| 下标                                     | `a_2`                                   | $a_2$                          |
| 分组                                     | `a^{2+2}`                               | $a^{2+2}$                       |
|                                          | `a_{i,j}`                                | $a_{i,j}$                        |
| 组合上下标                                | `x_2^3`                                  | $x_2^3$                          |
|                                          | `{x_2}^3`                                | ${x_2}^3$                        |
|                                          | `10^{10^{8}}`                            | $10^{10^{8}}$                    |
| Preceding and/or Additional sub & super  | `_nP_k`                                  | $ _{n}P_{k}$                     |
| \sideset                                 | `\sideset{_1^2}{_3^4}\prod_a^b`          | $\sideset{_1^2}{_3^4}\prod_a^b$  |
|                                          | `{}_1^2\!\Omega_3^4`                     | $ {}_1^2\!\Omega_3^4$            |
| 堆叠                                 | `\overset{\alpha}{\omega}`               | $\overset{\alpha}{\omega}$           |
|                                  | `\underset{\alpha}{\omega}`              | $\underset{\alpha}{\omega}$              |
|                            | `\overset{\alpha}{\underset{\gamma}{\omega}}` | $\overset{\alpha}{\underset{\gamma}{\omega}}$ |
|                                          | `\stackrel{\alpha}{\omega}`              | $\stackrel{\alpha}{\omega}$              |
| 导数                                       | `x', y'', f', f''`                       | $x', y'', f', f''$                       |
|                                          | `x^\prime, y^{\prime\prime}`             | $x^\prime, y^{\prime\prime}$             |
| Derivative dots                          | `\dot{x}, \ddot{x}`                      | $\dot{x}, \ddot{x}$                      |
| Underlines, overlines, vectors           | `\hat a \ \bar b \ \vec c`               | $\hat a \ \bar b \ \vec c$               |
| 向量                                       | `\overrightarrow{a b} \ \overleftarrow{c d} \ \widehat{d e f}` | $ \overrightarrow{a b} \ \overleftarrow{c d} \ \widehat{d e f}$ |
| 上下划线                                     | `\overline{g h i} \ \underline{j k l}`   | $ \overline{g h i}$ \ $\underline{j k l}$ |
| 删除线                                      | `\not 1 \ \cancel{123}`                  | $ \not 1 \ \cancel{123}$                 |
| Arrows箭头                                 | `A \xleftarrow{n+\mu-1} B \xrightarrow[T]{n\pm i-1} C` | $ A \xleftarrow{n+\mu-1} B \xrightarrow[T]{n\pm i-1} C$ |
| Overbraces    上大括号                       | `\overbrace{ 1+2+\cdots+100 }^{\text{sum}\,=\,5050}` | $ \overbrace{ 1+2+\cdots+100 }^{\text{sum}\,=\,5050}$ |
| Underbraces下大括号                          | `\underbrace{ a+b+\cdots+z }_{26\text{ terms}}` | $ \underbrace{ a+b+\cdots+z }_{26\text{ terms}}$ |
| 总和                                       | `\sum_{k=1}^N k^2`                       | $\sum_{k=1}^N k^2$              |
| Sum (force `\textstyle`)                 | `\textstyle \sum_{k=1}^N k^2`            | $\textstyle \sum_{k=1}^N k^2$      |
| 求积                                       | `\prod_{i=1}^N x_i`                      | $\prod_{i=1}^N x_i$             |
| (force `\textstyle`)                     | `\textstyle \prod_{i=1}^N x_i            | $\textstyle \prod_{i=1}^N x_i$       |
| Coproduct                                | `\coprod_{i=1}^N x_i`                    | $\coprod_{i=1}^N x_i$                   |
| Coproduct (force `\textstyle`)           | `\textstyle \coprod_{i=1}^N x_i`         | $\textstyle \coprod_{i=1}^N x_i$        |
| 极限                                       | `\lim_{n \to \infty}x_n`                 | $\lim_{n \to \infty}x_n$                |
| 限制 (force `\textstyle`)                  | `\textstyle \lim_{n \to \infty}x_n       | $\textstyle \lim_{n \to \infty}x_n$     |
| 积分                           | `\int\limits_{1}^{3}\frac{e^3/x}{x^2}\, dx` | $ \int\limits_{1}^{3}\frac{e^3/x}{x^2}\, dx$ |
| Integral (alternate limits style)        | `\int_{1}^{3}\frac{e^3/x}{x^2}\, dx`     | $ \int_{1}^{3}\frac{e^3/x}{x^2}\, dx$    |
| Integral (force `\textstyle`)            | `\textstyle \int\limits_{-N}^{N} e^x\, dx` | $ \textstyle \int\limits_{-N}^{N} e^x\, dx$ |
| Integral (force `\textstyle`, alternate limits style) | `\textstyle \int_{-N}^{N} e^x\, dx`| $\textstyle \int_{-N}^{N} e^x\, dx$  |
| Double integral二重积分                      | `\iint\limits_D \, dx\,dy`               | $ \iint\limits_D \, dx\,dy$        |
| Triple integral三重积分                      | `\iiint\limits_E \, dx\,dy\,dz`          | $ \iiint\limits_E \, dx\,dy\,dz$         |
| Quadruple integral  四倍积分                 | `\iiiint\limits_F \, dx\,dy\,dz\,dt`     | $ \iiiint\limits_F \, dx\,dy\,dz\,dt$    |
| Line or path integral  行或路径积分            | `\int_C x^3\, dx + 4y^2\, dy`            | $ \int_C x^3\, dx + 4y^2\, dy$           |
| Closed line or path integral  闭合线或路径积分 | `\oint_C x^3\, dx + 4y^2\, dy`   | $ \oint_C x^3\, dx + 4y^2\, dy$   |
| Intersections交集                          | `\bigcap_1^n p`                          | $ \bigcap_1^n p$                         |
| Unions并集                                 | `\bigcup_1^k p`                          | $ \bigcup_1^k p$                         |

### 分数、矩阵、多线

| 功能                                       | 语法                                       | 渲染                                       |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Fractions                                | `\frac{1}{2}=0.5`                        | $ \frac{1}{2}=0.5$                       |
| Small ("text style") fractions           | `\tfrac{1}{2} = 0.5`                     | $ \tfrac{1}{2} = 0.5$                    |
| Large ("display style") fractions        | `\dfrac{k}{k-1} = 0.5`                   | $ \dfrac{k}{k-1} = 0.5$                  |
| Mixture of large and small fractions     | `\dfrac{ \tfrac{1}{2}[1-(\tfrac{1}{2})^n] }{ 1-\tfrac{1}{2} } = s_n` | $ \dfrac{ \tfrac{1}{2}[1-(\tfrac{1}{2})^n] }{ 1-\tfrac{1}{2} } = s_n$ |
| Continued fractions (note the difference in formatting) | `\cfrac{2}{ c + \cfrac{2}{ d + \cfrac{1}{2} } } = a\qquad\dfrac{2}{ c + \dfrac{2}{ d + \dfrac{1}{2} } } = a` | $\cfrac{2}{ c + \cfrac{2}{ d + \cfrac{1}{2} } } = a \qquad \dfrac{2}{ c + \dfrac{2}{ d + \dfrac{1}{2} } } = a$ |
| Binomial coefficients      | `\binom{n}{k}`        | $ \binom{n}{k}$         |
| Small ("text style") binomial coefficients | `\tbinom{n}{k}`      | $ \tbinom{n}{k}$     |
| Large ("display style") binomial coefficients | `\dbinom{n}{k}`      | $ \dbinom{n}{k}$      |
| 矩阵  | `\begin{matrix}x & y \\z & v \end{matrix}` | $\begin{matrix} x & y \\ z & v  \end{matrix}$ |
|   | `\begin{vmatrix}x & y \\z & v \end{vmatrix}` | $\begin{vmatrix} x & y \\ z & v  \end{vmatrix}$ |
|   | `\begin{Vmatrix}x & y \\z & v\end{Vmatrix}` | $\begin{Vmatrix} x & y \\ z & v \end{Vmatrix}$ |
|    | `\begin{bmatrix} 0& \cdots & 0\\ \vdots & \ddots & \vdots \\0& \cdots & 0 \end{bmatrix}` | $\begin{bmatrix}0&\cdots&0\\\vdots & \ddots & \vdots \\  0      & \cdots & 0 \end{bmatrix}$ |
|    | `\begin{Bmatrix} x & y \\ z & v \end{Bmatrix}` | $\begin{Bmatrix} x & y \\ z & v \end{Bmatrix}$ |
|  | `\begin{pmatrix} x & y \\ z & v  \end{pmatrix}` | $\begin{pmatrix} x & y \\ z & v  \end{pmatrix}$ |
|  | `\bigl( \begin{smallmatrix} a&b\\ c&d \end{smallmatrix} \bigr)` | $\bigl( \begin{smallmatrix} a&b\\ c&d \end{smallmatrix} \bigr)$ |
| 数组  | `\begin{array}{|c|c||c|} a & b & S \\ \hline 0&0&1\\ 0&1&1\\ 1&0&1\\ 1&1&0 \end{array}` | $\begin{array}{|c|c||c|} a & b & S \\ \hline 0&0&1\\ 0&1&1\\ 1&0&1\\ 1&1&0 \end{array}$ |
| Cases   | `f(n) = \begin{cases} n/2,  & \mbox{if }n\mbox{ is even} \\3n+1, & \mbox{if }n\mbox{ is odd} \end{cases}` | $f(n) =  \begin{cases}  n/2,  & \mbox{if }n\mbox{ is even} \\ 3n+1, & \mbox{if }n\mbox{ is odd}  \end{cases}$ |
| System of equations | `\begin{cases}3x + 5y +  z &= 1 \\7x - 2y + 4z &= 2 \\-6x + 3y + 2z &= 3\end{cases}` | $\begin{cases} 3x + 5y +  z &= 1 \\ 7x - 2y + 4z &= 2 \\ -6x + 3y + 2z &= 3 \end{cases}$ |
| Breaking up a long expression so it wraps when necessary | `<math>f(x) = \sum_{n=0}^\infty a_n x^n</math><math>= a_0 + a_1x + a_2x^2 + \cdots</math>` | $f(x) = \sum_{n=0}^\infty a_n x^n\\= a_0 + a_1x + a_2x^2 + \cdots$ |
| Multiline equations | `\begin{align}f(x) & = (a+b)^2 \\& = a^2+2ab+b^2\end{align}` | $\begin{align} f(x) & = (a+b)^2 \\ & = a^2+2ab+b^2 \end{align}$ |
|  | `\begin{alignat}{2}f(x) & = (a-b)^2 \\& = a^2-2ab+b^2\end{alignat}` | $\begin{alignat}{2} f(x) & = (a-b)^2 \\ & = a^2-2ab+b^2 \end{alignat}$ |
| Multiline equations with aligment specified (left, center, right) | `\begin{array}{lcl}z&=&a\\f(x,y,z) & = & x + y + z  \end{array}` | $\begin{array}{lcl} z& = & a\\ f(x,y,z) & = & x + y + z   \end{array}$ |
|   | `\begin{array}{lcr}z&=&a\\f(x,y,z) & = & x + y + z\end{array}` | $\begin{array}{lcr} z& =&a\\f(x,y,z) & = & x + y + z      \end{array}$ |

### 为大表达式加括号、线条等

| 功能   | 语法                             | 渲染                  |
| ---- | ------------------------------ | ------------------------------- |
| 不良   | `( \frac{1}{2} )`               | $ ( \frac{1}{2} )$              |
| 良好   | `\left ( \frac{1}{2} \right )` | $ \left ( \frac{1}{2} \right )$ |

You can use various delimiters with `\left` and `\right`: , 区别于语法调用,好似没太大区别

| 功能                                       | 语法                                       | 渲染                                       |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| 圆括号                                      | `\left ( \frac{a}{b} \right )`            | $ \left ( \frac{a}{b} \right )$          |
| 方括号                                      | `\left [ \frac{a}{b} \right ] \quad \left \lbrack \frac{a}{b} \right \rbrack` | $ \left [ \frac{a}{b} \right ] \quad \left \lbrack \frac{a}{b} \right \rbrack$ |
| 花括号 (note the backslash before the braces in the code) | `\left \{ \frac{a}{b} \right \} \quad \left \lbrace \frac{a}{b} \right \rbrace` | $ \left \{ \frac{a}{b} \right \} \quad \left \lbrace \frac{a}{b} \right \rbrace$ |
| Angle brackets                           | `\left \langle \frac{a}{b} \right \rangle` | $ \left \langle \frac{a}{b} \right \rangle$ |
| Bars and double bars (note: "bars" provide the absolute value function) | `\left | \frac{a}{b} \right \vert \left \Vert \frac{c}{d} \right \|` | $ \left | \frac{a}{b} \right \vert \left \Vert \frac{c}{d} \right \|$ |
| Floor and ceiling functions:             | `\left \lfloor \frac{a}{b} \right \rfloor \left \lceil \frac{c}{d} \right \rceil` | $ \left \lfloor \frac{a}{b} \right \rfloor \left \lceil \frac{c}{d} \right \rceil$ |
| Slashes and backslashes                  | `\left / \frac{a}{b} \right \backslash`  | $ \left / \frac{a}{b} \right \backslash$ |
| Up, down and up-down arrows              | `\left \uparrow \frac{a}{b} \right \downarrow \quad \left \Uparrow \frac{a}{b} \right \Downarrow \quad \left \updownarrow \frac{a}{b} \right \Updownarrow` | $ \left \uparrow \frac{a}{b} \right \downarrow \quad \left \Uparrow \frac{a}{b} \right \Downarrow \quad \left \updownarrow \frac{a}{b} \right \Updownarrow$ |
| Delimiters can be mixed, as long as `\left` and `\right` are both used | `\left [ 0,1 \right )``\left \langle \psi \right |` | $ `\left [ 0,1 \right )``\left \langle \psi \right |`$ |
| Use `\left.` or `\right.` if you don't want a delimiter to appear: | `\left . \frac{A}{B} \right \} \to X`    | $ \left . \frac{A}{B} \right \} \to X$   |
| Size of the delimiters    | `\big( \Big( \bigg( \Bigg( \dots \Bigg] \bigg] \Big] \big]` | $ \big( \Big( \bigg( \Bigg( \dots \Bigg] \bigg] \Big] \big]$ |
| 大括号                                      | `\big\{ \Big\{ \bigg\{ \Bigg\{ \dots \Bigg\rangle \bigg\rangle \Big\rangle \big\rangle` | $ \big\{ \Big\{ \bigg\{ \Bigg\{ \dots \Bigg\rangle \bigg\rangle \Big\rangle \big\rangle$ |
|                                          | ` \big| \Big| \bigg| \Bigg| \dots \Bigg\| \bigg\| \Big\| \big\|` | $ \big| \Big| \bigg| \Bigg| \dots \Bigg\| \bigg\| \Big\| \big\|$ |
|                                          | ` \big\lfloor \Big\lfloor \bigg\lfloor \Bigg\lfloor \dots \Bigg\rceil \bigg\rceil \Big\rceil \big\rceil` | $ \big\lfloor \Big\lfloor \bigg\lfloor \Bigg\lfloor \dots \Bigg\rceil \bigg\rceil \Big\rceil \big\rceil$ |
|                                          | ` \big\uparrow \Big\uparrow \bigg\uparrow \Bigg\uparrow \dots \Bigg\Downarrow \bigg\Downarrow \Big\Downarrow \big\Downarrow` | $ \big\uparrow \Big\uparrow \bigg\uparrow \Bigg\uparrow \dots \Bigg\Downarrow \bigg\Downarrow \Big\Downarrow \big\Downarrow$ |
|          | ` \big\updownarrow \Big\updownarrow \bigg\updownarrow \Bigg\updownarrow \dots \Bigg\Updownarrow \bigg\Updownarrow \Big\Updownarrow \big\Updownarrow` | $ \big\updownarrow \Big\updownarrow \bigg\updownarrow \Bigg\updownarrow \dots \Bigg\Updownarrow \bigg\Updownarrow \Big\Updownarrow \big\Updownarrow$ |
|       | ` \big / \Big / \bigg / \Bigg / \dots \Bigg\backslash \bigg\backslash \Big\backslash \big\backslash` | $ \big / \Big / \bigg / \Bigg / \dots \Bigg\backslash \bigg\backslash \Big\backslash \big\backslash$ |

## 颜色

公式可以有颜色：

```
  {\color{Blue}x^2}+{\color{YellowOrange}2x}-{\color{OliveGreen}1}
```
```
  x_{1,2}=\frac{-b\pm\sqrt{\color{Red}b^2-4ac}}{2a}
```


自从[r59550](https://www.mediawiki.org/wiki/Special:Code/MediaWiki/59550)版本后，公式的背景颜色也可以修改了。显示如下

>  ${\color{Blue}x^2}+{\color{YellowOrange}2x}-{\color{OliveGreen}1}$
>
> $x_{1,2}=\frac{-b\pm\sqrt{\color{Red}b^2-4ac}}{2a}$


| 背景色  | 源代码                 | 效果                     |
| ---- | ------------------------ | ------------------------ |
| 白色   | `e^{i \pi} + 1 = 0`                      | $ e^{i \pi} + 1 = 0$                     |
|      | `**\definecolor{orange}{RGB}{255,165,0}\pagecolor{orange}**e^{i \pi} + 1 = 0` | $ **\definecolor{orange}{RGB}{255,165,0}\pagecolor{orange}**e^{i \pi} + 1 = 0$ |
| 桔黄色  | `e^{i \pi} + 1 = 0`                      | $ e^{i \pi} + 1 = 0$                     |
|      | `**\definecolor{orange}{RGB}{255,165,0}\pagecolor{orange}**e^{i \pi} + 1 = 0` | $ **\definecolor{orange}{RGB}{255,165,0}\pagecolor{orange}**e^{i \pi} + 1 = 0$ |

貌似,背景色没有生效........

所有的已命名颜色可以在[这里](http://oregonstate.edu/~peterseb/tex/samples/docs/color-package-demo.pdf)找到。


-----------
[Latex语法](https://zh.wikipedia.org/wiki/Markdown)     
[github显示数学公式插件](https://github.com/orsharir/github-mathjax)     
[参考网址:在markdown中输入数学公式](https://github.com/JZQT/jzqt.github.io/blob/master/2015/06/30/Markdown%E4%B8%AD%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F/index.html)
