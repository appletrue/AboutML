古代数学中，单单无穷小、无穷大的概念就讨论了近200年，而后才由无限发展到极限的概念。

## 极限Limit

极限分为两部分：数列的极限和函数的极限。

**数列的极限**

定义  如果数列$\{x_n\}$与常a 有下列关系:对于任意给定的正数e (不论它多么小), 总存在正整数N , 使得对于n >N 时的一切$x_n$, 不等式$ |x_n-a |<e$都成立, 则称常数a 是数列$\{x_n\}$的极限, 或者称数列$\{x_n\}$收敛于a , 记为

$\lim_{n \to \infty}x_n = a $或  $ x_n \to a (n \to \infty) $,即

$当时有\lim_{n \to \infty}x_n = a \Leftrightarrow \forall \xi >0,\exists N \in N^+ ,当 n>N时, 有|x_n -a |< \xi . $

**函数的极限**

设函数f(x)在点$x_0$的某一去心邻域内有定义，如果存在常数A, 对于任意给定的正数e (不论它多么小), 总存在正数d, 使得当x满足不等式$0<|x-x_0|<d$ 时, 对应的函数值f(x)都满足不等式  |f(x)-A|<e , 那么常数A就叫做函数$在f(x) 在x \to x_0$ 时的极限, 记为

$或当\lim_{n \to x_0} f(x) = A 或  f(x) \to A (当 x \to x_0 ) $

即 $当时\lim_{n \to x_0 }= A \Leftrightarrow \forall \xi >0,\exists \delta >0 ,当0<|x-x_0|< \delta 时, |f(x) -A |< \xi . $

## 导数

设有定义域和取值都在实数域中的函数y=f(x)，若f(x) 在点 $x_0$ 的某个邻域内有定义,则当自变量x 在$x_0$ 处取得增量$\Delta x$(点$x_0+ \Delta x $仍在该邻域内)时,相应地函数 y 取得增量 $\Delta y = f(x_0+ \Delta x) - f(x_0) $; 如果 $与\Delta y 与 \Delta x$ 之比当 $\Delta x \to 0$时的极限存在,则称函数 $在点y=f(x) 在点 x_0$处可导,并称这个极限为函数 y = f(x) 在点 $x_0$处的导数,记为 $f'(x_0)$.

$f'(x_0) = lim_{\Delta x \to 0 } \frac {\Delta y}{\Delta x} = lim_{\Delta x \to 0 } \frac { f(x_0+ \Delta x) - f(x_0) }{\Delta x} $

也可以记为:  $或y'|_{x-x_0}, \frac{dy}{dx}|_{x-x_0} 或 \frac {df(x)}{dx}|_{x-x0}$

## 微分

设函数 y=f(x) 在某区间 z 内有定义.对于 z 内一点 $x_0 $,当 $x_0 $变动到附近的$x_0+ \Delta x$($x_0+ \Delta x$也在此区间内)时,如果函数的增量   $\Delta y = f(x_0+ \Delta x) - f(x_0) $可表示为  $\Delta y = A \Delta x + O(\Delta x) $ ,(其中A 是不依赖于 $\Delta x$的常数),而 $O(\Delta x) $是比$\Delta x$高阶的无穷小,那么称函数 f(x) 在点 $x_0$是可微的,且$A \Delta x$称作函数在点$x_0$想应于自变量增量$\Delta x$的微分,记$dy$,即$\Delta y = A \Delta x $,$是dy 是\Delta y $的线性主部。通常把自变量x 的增量 $\Delta x$称为自变量的微分,记作$dx$,即 $dx=\Delta x$

微积分则是在导数$f'(x_0)$基础上加后缀 $\Delta x$,即为 : $dy=f'(x_0)\Delta x$

## 积分

积分是微积分学与数学分析里的一个核心概念。通常分为定积分和不定积分两种。

### **不定积分**

一个函数 f(x) 的不定积分，也称为原函数或反导数，是一个导数等于 f 的函数 F ,即

$\int f(x)dx = F(x) +c$

不定积分有换元积分法,分部积分法等求法.

** **备注** **:

**原函数:** 已知函数f(x)是一个定义在某区间的函数，如果存在可导函数F(x)，使得在该区间内的任一点都有dF(x)=f(x)dx，则在该区间内就称函数F(x)为函数f(x)的原函数.

典型原函数:  

$ \int sinxdx = -cosx +c ; \int cosxdx = sinx +c ; $

$\int sec dx = ln|secx+tanx|+c ; \int cscdx = ln|cscx-cotx|+c$

$\int a^xdx = \frac {a^x}{ln a} +c ; \int x^a dx=\frac {x^{a+1}}{a+1} +c $

$\int lnxdx = x(lnx-1) +c$

$\int e^xdx = {e^x} +c ;  \int \frac 1 x dx=ln|x| +c $

### **定积分**

直观地说，对于一个给定的正实值函数 f(x) ,在一个实数区间 [a,b] 上的定积分:$\int ^b_a f(x)dx$.

定积分与不定积分区别在于不定积分便是不给定区间，即式子中，积分符号没有a、b。

**积分中值定理**

如果函数f(x)在闭区间[a,b]上连续, 则在积分区间[a,b]上至少存在一个点$\xi$ 使下式成立：

$\int ^b_a f(x)dx = f(\xi)(b-a)$. 该公式为积分中值公式。

**牛顿-莱布尼茨公式**

如果函数F (x)是连续函数f(x)在区间[a, b]上的一个原函数, 则$）\int ^b_a f(x)dx = F(b）-F(a)$

此公式称为牛顿-莱布尼茨公式, 也称为微积分基本公式,公式由此便打通了原函数与定积分之间的联系。表明：一个连续函数在区间[a, b]上的定积分等于它的任一个原函数在区间[a, b]上的增量，如此，便给定积分提供了一个有效而极为简单的计算方法，大大简化了定积分的计算手续。

例：如何通过原函数求取定积分

计算$\int _0^1 x^2dx $, 因 $是\frac 1 3 x^3 是 x^2$的一个原函数,所以 $\int _0^1 x^2dx =[\frac 1 3 x^3]_0^1 =\frac 1 3 1^3-\frac 1 3 0^3 = \frac1 3$

## 偏导数

对于二元函数z = f(x，y) 如果只有自变量x 变化，而自变量y固定，这时它就是x的一元函数，这函数对x的导数，就称为二元函数z = f(x，y)对于x的偏导数。

设函数z = f(x，y)在点$，(x_0，y_0)$的某一邻域内有定义，当y固定在$y_0$而x在$x_0$处有增量$\Delta x$时，相应地函数有增量$f(x_0+ \Delta x, y_0) - f(x_0,y_0)$,如果极限 $lim_{\Delta x \to 0} \frac {f(x_0+ \Delta x, y_0) - f(x_0,y_0)}{\Delta x}$ 存在,则称此极限为函数 $z = f(x,y) $在点$(x_0,y_0)$处对x 的偏导数,记作:

$或 \frac {\partial Z}{\partial x}|_{x=x_0,y=y_0},\frac {\partial f}{\partial x}|_{x=x_0,y=y_0} ,Z_x|_{x=x_0,y=y_0},或 f_x(x_0,y_0)$

例如: $f_x(x_0,y_0) = lim_{\Delta x \to 0}\frac {f(x_0+ \Delta x, y_0) - f(x_0,y_0)}{\Delta x}$,类似, 二元函数对y 求偏导,则把 x 当做常量。



------

参考书目：

《高等数学》

《微积分概念发展史》
