# 伽玛函数  

## 看$\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt$诞生

Gamma函数$\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt$，骨骼清奇，长相奇特。

通过分部积分的方法，可以推导函数的递归性质$\Gamma(x+1) = x \Gamma(x)$

很容易证明，$Γ(x)$ 函数可以当成是阶乘在实数集上的延拓，具有如下性质$\Gamma(n) = (n-1)!$

> 1728年，哥德巴赫在考虑**数列插值**问题，就是把数列的通项公式定义从整数集合延拓到实数集合，例如数列 1,4,9,16,⋯ 可以用通项公式 $n^2$ 自然的表达，即便 n 为实数的时候，这个通项公式也是良好定义的。直观的说也就是可以找到一条**平滑的曲线$y=x^2$通过所有的整数点$(n,n2)$**，从而可以把定义在整数集上的公式延拓到实数集合。
>
> 一天哥德巴赫开始处理阶乘序列 $1,2,6,24,120,720,⋯$,我们可以计算 $2!,3!$, 是否可以计算 $2.5!$呢？把最初的一些 $(n,n!)$的点画在坐标轴上，确实可以看到，容易画出一条通过这些点的平滑曲线。

![Gamma函数例图](https://github.com/appletrue/NoteML/blob/master/PICs/gamma-func.png)

> 但是哥德巴赫无法解决阶乘向实数集延拓的问题，于是写信请教尼古拉斯.贝努利和他的弟弟丹尼尔.贝努利，由于欧拉当时和丹尼尔.贝努利在一块，因此得知了这个问题。欧拉于1729 年完美的解决了这个问题，由此导致了 **$Γ$函数的诞生**，当时欧拉只有22岁。

> 首先解决n!n!的插值计算问题的是丹尼尔.贝努利，他发现，如果 m,n 都是正整数，如果 m→∞，有$\frac{1\cdot 2\cdot 3 \cdots m}{(1+n)(2+n)\cdots (m-1+n)}(m+\frac{n}{2})^{n-1} \rightarrow n!$
>
> 于是用这个无穷乘积的方式可以把n!的定义延拓到实数集合。例如，取 n=2.5 m足够大，基于上式就可以近似计算出 $2.5!$

> 欧拉也偶然的发现 n! 可以用如下的一个无穷乘积表达$`\begin{equation} \label{euler-series} \Bigl[\Bigl(\frac{2}{1}\Bigr)^n\frac{1}{n+1}\Bigr] \Bigl[\Bigl(\frac{3}{2}\Bigr)^n\frac{2}{n+2}\Bigr] \Bigl[\Bigl(\frac{4}{3}\Bigr)^n\frac{3}{n+3}\Bigr] \cdots = n! \quad  (*) \end{equation}`$
>
> 用极限形式，这个式子整理后可以写为
>
> $`\begin{equation} \label{euler-series2} \lim_{m \rightarrow \infty} \frac{1\cdot 2\cdot 3 \cdots m}{(1+n)(2+n)\cdots (m+n)}(m+1)^{n} = n! \quad  (**) \end{equation}`$
>
> 左边可以整理为
>
> $\begin{align*} & \frac{1\cdot 2\cdot 3 \cdots m}{(1+n)(2+n)\cdots (m+n)}(m+1)^{n} \\ = & 1\cdot 2\cdot 3 \cdots n \cdot \frac{(n+1)(n+2)\cdots m}{(1+n)(2+n)\cdots m } \cdot \frac{(m+1)^{n}}{(m+1)(m+2)\cdots (m+n)} \\ = & n! \frac{(m+1)^{n}}{(m+1)(m+2)\cdots (m+n)} \\ = & n!\prod_{k=1}^{n} \frac{m+1}{m+k} \rightarrow n! \qquad (m\rightarrow \infty) \end{align*}$
>
> 所以 (*)、(**)式都成立。
>
> 欧拉开始尝试从一些简单的例子开始做一些计算，看看是否有规律可循，欧拉极其擅长数学的观察与归纳。当 n=1/2 的时候，带入(*)式计算，整理后可以得到
>
> $\Bigl(\frac{1}{2}\Bigr)! = \sqrt{\frac{2\cdot4}{3\cdot3} \cdot \frac{4\cdot6}{5\cdot5}\cdot \frac{6\cdot8}{7\cdot7} \cdot \frac{8\cdot10}{9\cdot9} \cdots}$
>
> 然而右边正好和著名的 Wallis 公式关联。Wallis 在1665年使用插值方法计算半圆曲线 $y = \sqrt{x(1-x)}$ 下的面积(也就是直径为1的半圆面积)的时候，得到关于ππ的如下结果，
>
> $\frac{2\cdot4}{3\cdot3} \cdot \frac{4\cdot6}{5\cdot5}\cdot \frac{6\cdot8}{7\cdot7} \cdot \frac{8\cdot10}{9\cdot9} \cdots = \frac{\pi}{4}$
>
> 于是，欧拉利用 Wallis 公式得到了如下一个很漂亮的结果
>
> $\Bigl(\frac{1}{2}\Bigr)! = \frac{\sqrt{\pi}}{2}$

欧拉和高斯都是具有超凡直觉的数学家，但高斯是个老狐狸，数学上非常严谨，发表结果时却把思考痕迹抹去；而欧拉风格不同，通过经验直觉做大胆的猜测，他的文章中往往留下他做数学猜想的痕迹，而文章有的时候论证不够严谨。 拉普拉斯曾说过：”读读欧拉,他是所有人的老师。”波利亚在他的名著《数学与猜想》中也对欧拉做数学归纳和猜想的方式推崇备至。

>  欧拉看到$\frac12!$中居然有 π, 对数学家而言，有π 的地方必然有和圆相关的积分。由此欧拉猜测 n!一定可以表达为某种积分形式，于是欧拉开始尝试把 n!表达为积分形式。虽然Wallis 的时代微积分还没有发明出来，Wallis 是使用插值的方式做推导计算的，但是Wallis 公式的推导过程基本上就是在处理积分 $\int_0^1 x^\frac{1}{2}(1-x)^\frac{1}{2}dx$，受 Wallis 的启发，欧拉开始考虑如下的一般形式的积分
>
> $J(e,n) = \int_0^1 x^e(1-x)^ndx$,此处n 为正整数，ee 为正实数。

> 利用分部积分方法，容易得到$J(e,n) = \frac{n}{e+1}J(e+1,n-1)$
>
> 重复使用上述迭代公式，最终可以得到$J(e,n) = \frac{1\cdot2\cdots n}{(e+1)(e+2)\cdots(e+n+1)}$

> 于是欧拉得到如下一个重要的式子$n! = (e+1)(e+2)\cdots(e+n+1)\int_0^1 x^e(1-x)^ndx$
>
> 接下来，欧拉使用了一点计算技巧，取 e=f/g 并且令 f→1,g→0,然后对上式右边计算极限(极限计算的过程此处略去，推导不难，有兴趣的同学看后面的参考文献吧)，于是欧拉得到如下简洁漂亮的结果：$n! = \int_0^1 (-\log t)^ndt$
>
> 欧拉成功的把n!表达为了积分形式！如果我们做一个变换 t=e−u,就可以得到我们常见的Gamma 函数形式$n! = \int_0^{\infty} u^ne^{-u}du$
>
> 于是,利用上式把阶乘延拓到实数集上，我们就得到 Gamma 函数的一般形式
>
> $\Gamma(x) = \int_0^1 (-\log t)^{x-1}dt = \int_0^{\infty} t^{x-1}e^{-t}dt$

这样,Gamma 函数找到了.

## 为何Gamma 函数被定义为$\Gamma(n) = (n-1)!$

> 把Gamma 函数定义中的$ t^{x−1}$ 替换为 $t^x$ ,得到$\Gamma(x) = \int_0^{\infty} t^{x}e^{-t}dt$,可使$\Gamma(n) = n!$,但欧拉后续修改了 Gamma 函数的定义，使得$\Gamma(n) = (n-1)!$

有数学家猜测,修改的原因可能是欧拉研究了如下积分:

$B(m, n) = \int_0^1 x^{m-1}(1-x)^{n-1}dx$,

**这个函数现在称为Beta 函数**。如果Gamma 函数的定义选取满足$\Gamma(n)=(n-1)!$, 那么有

$B(m,n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}$,非常漂亮的对称形式。

> Rickjin的《LDA数学八卦》,欧拉是研究了Beta函数$B(m,n) = \int_0^1x^{m-1}(1-x)^{n-1}dx$,如果Gamma函数的定义选取满足$\Gamma(n) = (n-1)!$,那么Beta函数会有一个很漂亮的对称形式:
>
> $B(m,n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}$,而如果选取$\Gamma(n) = n!$的定义，则有 $B'(m,n)= \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n+1)}$

可是如果选取$\Gamma(n)=n!$,的定义，令$E(m, n) = \int_0^1 x^{m}(1-x)^{n}dx$

则有$E(m,n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n+1)}$形式显然不如 B(m,n)优美，而数学家总是很在乎数学公式的美感.

Gamma函数:$\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt$ 是阶乘运算在实数集上延伸，首先它也有和 Stirling 公式类似的一个结论$\Gamma(x) \sim \sqrt{2\pi}e^{-x}x^{x-\frac{1}{2}}$

它不但使得 $\frac12!$ 的计算有意义，还能扩展很多其他的数学概念。比如导数，我们原来只能定义一阶、二阶等整数阶导数，有了Gamma 函数我们可以把函数导数的定义延拓到实数集，从而可以计算 1/2 阶导数,同样的积分作为导数的逆运算也可以有分数阶。

k阶导数可以用阶乘表达，于是我们用Gamma 函数表达为$\frac{\Gamma{(n+1)}}{\Gamma{(n-k+1)}} x^{n-k}$

基于上式，我们可以把导数的阶从整数延拓到实数集。例如，取$n=1, k=\frac{1}{2}$可以计算 xx 的 1212阶导数为$\frac{\Gamma{(1+1)}}{\Gamma{(1-1/2+1)}} x^{1-1/2} = \frac{2\sqrt{x}}{\sqrt{\pi}}$

对于一般的函数 f(x)通过 Taylor 级数展开可以表达为幂级数，于是借用 $x^n$ 的分数阶导数，以尝试定义出任意函数的分数阶导数。这种定义方法并非良定义的，不是对所有函数都适用，但思想却是被数学家广泛采纳了，并由此发展了数学分析中的一个研究课题：Fractional Calculus,在这种微积分中，分数阶的导数和积分都具有良定义，而这都依赖于 Gamma 函数。

Gamma 函数和欧拉常数γ 有密切关系，可以发现

$\gamma = -\frac{d\Gamma(x)}{dx}|_{x=1} =\lim_{n\rightarrow \infty}(1+\frac{1}{2} + \frac{1}{3}+\cdots+\frac{1}{n} - \log n)$

进一步还可以发现 Gamma 函数和黎曼函数ζ(s)ζ(s)有密切联系，

$\zeta(s) = 1+\frac{1}{2^s} + \frac{1}{2^s} + \cdots$,而ζ 函数涉及了数学中著名的黎曼猜想和素数的分布定理。

从Gamma 函数的图像我们可以看到它是一个凸函数, 不仅如此, logΓ(x)也是一个凸函数，

------

**[Bohr-Mullerup定理]**  如果$ f:(0,∞)→(0,∞)$,且满足

1.  f(1)=1
2.  f(x+1)=xf(x)
3.  logf(x) 是凸函数

那么$ f(x)=Γ(x)$, 也就是$ Γ(x)$是唯一满足以上条件的函数。

------

如下函数被称为 Digamma 函数，$\Psi(x) = \frac{d\log\Gamma(x)}{dx}$,这也是一个很重要的函数，在涉及求Dirichlet 分布相关的参数的极大似然估计时，往往需要使用到这个函数。

Digamma 函数具有如下一个漂亮的性质 $\Psi(x+1) = \Psi(x) + \frac{1}{x}$

函数Ψ(x)和欧拉常数γ 以及 ζ 函数都有密切关系，令 $\Psi_n(x) = \frac{d^{n+1}\log\Gamma(x)}{dx^{n+1}}$

则 $Ψ_0(x)=Ψ(x)$,可以证明 

$\Psi(1) = -\gamma,$              $\Psi(2) = 1-\gamma$,

$\Psi_1(1) = \zeta(2) = \frac{\pi^2}{6}$,$ \Psi_2(1) = -2\zeta(3)$

------------
[伽玛函数](http://www.52nlp.cn/lda-math-%E7%A5%9E%E5%A5%87%E7%9A%84gamma%E5%87%BD%E6%95%B01)
