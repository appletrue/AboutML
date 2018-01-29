

伽玛函数  http://www.52nlp.cn/lda-math-%E7%A5%9E%E5%A5%87%E7%9A%84gamma%E5%87%BD%E6%95%B01

诞生\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt

一个长相有点奇特的Gamma函数\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt,

通过分部积分的方法，可以推导出这个函数有如下的递归性质\Gamma(x+1) = x \Gamma(x)





Gamma 函数在概率统计中频繁现身，众多的统计分布，包括常见的统计学三大分布(t 分布，χ2 分布，F 分布)、Beta分布、 Dirichlet 分布的密度公式中都有 Gamma 函数的身影；当然发生最直接联系的概率分布是直接由 Gamma 函数变换得到的 Gamma 分布。

对Gamma 函数的定义做一个变形，就可以得到如下式子\int_0^{\infty} \frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}dx = 1

于是，取积分中的函数作为概率密度，就得到一个形式最简单的Gamma 分布的密度函数Gamma(x|\alpha) = \frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}

如果做一个变换 x=βt, 就得到Gamma 分布的更一般的形式Gamma(t|\alpha, \beta) = \frac{\beta^\alpha t^{\alpha-1}e^{-\beta t}}{\Gamma(\alpha)},其中 α 称为 shape parameter, 主要决定了分布曲线的形状;而β 称为 rate parameter 或者inverse scale parameter (1/β 称为scale parameter),主要决定曲线有多陡

做积分变换 t=\beta x,得 \Gamma(\alpha,\beta)=\beta^\alpha \int_0^\infty x^{\alpha-1}e^{-x\beta}dx,从而

\frac1{\Gamma(\alpha,\beta)}\beta^\alpha\int_0^\infty x^{\alpha-1}e^{-x\beta}dx=1







γ分布

Gamma函数:\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt 是阶乘运算在实数集上延伸。它具有如下性质:

\Gamma(x+1) = x\Gamma(x) 因此有 \Gamma(n)=(n-1)!

Rickjin的《LDA数学八卦》,欧拉是研究了Beta函数B(m,n) = \int_0^1x^{m-1}(1-x)^{n-1}dx,如果Gamma函数的定义选取满足\Gamma(n) = (n-1)!,那么Beta函数会有一个很漂亮的对称形式:

B(m,n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)},而如果选取\Gamma(n) = n!的定义，则有 B'(m,n)= \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n+1)}





Beta分布

Beta分布的面试题目:

1. X∼Uniform(0,1)X∼Uniform(0,1);
2. 随机生成10个数，把这10个数排序后得到的顺序统计量是X1,X2,...,XnX1,X2,...,Xn;
3. 问第7大的数的概率分布?



我们先将之一般化，对于一般的情况XkXk的概率密度是什么呢？下面，我们尝试计算一下XkXk落在一个区间x,x+Δx的概率值

P(x≤Xk≤x+Δx)=?P(x≤Xk≤x+Δx)=?



如上图所示，我们把[0,1]区间分成三段0,x),[x,x+Δx],(x+Δx,1,(x+Δx,1]三段。我们假定，ΔxΔx足够小，只能够容纳一个点,则由排列组合理论可得

P(x≤Xk≤x+Δx)=(n1)Δx(n−1k−1)xk−1(1−x−Δx)n−kP(x≤Xk≤x+Δx)=(n1)Δx(n−1k−1)xk−1(1−x−Δx)n−k

所以我们可以得到XkXk的概率密度函数为

f(x)=limx→0P(x≤Xk≤x+Δx)Δx=(n1)(n−1k−1)xk−1(1−x)n−k=n!(k−1)!(n−k)!xk−1(1−x)n−k=Γ(n+1)Γ(k)Γ(n−k+1)xk−1(1−x)n−kf(x)=limx→0P(x≤Xk≤x+Δx)Δx=(n1)(n−1k−1)xk−1(1−x)n−k=n!(k−1)!(n−k)!xk−1(1−x)n−k=Γ(n+1)Γ(k)Γ(n−k+1)xk−1(1−x)n−k

我们取α=k,β=n−k+1α=k,β=n−k+1,于是

f(x)=Γ(α+β)Γ(α)Γ(β)xα−1(1−x)β−1f(x)=Γ(α+β)Γ(α)Γ(β)xα−1(1−x)β−1

这就是Beta分布！

回到上面那个面试题，把n=10,k=7n=10,k=7带入其中，得到密度函数

f(x)=10!6!×3!x6(1−x)3,x∈[0,1]



---

alpha （一般为整数）代表一件事发生的次数；beta代表它发生一次的概率（或者叫速率）。那么gamma 分布就代表这么一件事发生alpha 次所需要时间的分布。

例如alpha=1 就是指数分布

从意义来看：指数分布解决的问题是“要等到一个随机事件发生，需要经历多久时间”，伽玛分布解决的问题是“要等到n个随机事件都发生，需要经历多久时间”。

所以，伽玛分布可以看作是n个指数分布的独立随机变量的加总，即，n个Exponential(λ)random variables--->Gamma(n,λ）

从熵最大化的角度来看，如果一个事物既满足算术平均值是固定值，又满足几何平均值是固定值的，这种分布最可能的分布为分布。

也就是说，分布可以用来模拟我们经常用来作为思想实验的事物，总数是不变的同时，其增长率也是固定的。这种事物是不存在的，但是我们可以给出他存在的概率。这种思考问题的方式确实真实存在，例如我们经常讲人民币每年升值20%，均衡汇率为6.5。例如风速，我们也可以认为其总量是不变的，同时增速也是固定的。但是我们必须要注意，因为分布更多的用来描述汇率、速率这样的变量，所以他是没有量纲的量，也就是说与正态分布最大的不同，2X就是2倍风速的意思，不能是改变单位的意思。

---





Beta-Binomial共轭

上边的面试题还有几个衍化版本，我们先看第一个衍化版本：

1. X∼Uniform(0,1)X∼Uniform(0,1);
2. 随机生成n个数,由小到大排序后为X1,X2,...,XnX1,X2,...,Xn,我们要猜测第k大的数p=Xkp=Xk;
3. 我们再生成m个数，Y1,Y2,...,Ym∼Uniform(0,1)Y1,Y2,...,Ym∼Uniform(0,1), 其中有mimi个数比p小，m2m2比p大；
4. 求P(p∥Y1,Y2,...,Ym)P(p‖Y1,Y2,...,Ym)的分布是什么。

容易看出，我们一共生成了m+nm+n个数，而p=Xkp=Xk在最终生成的m+n个数中，是第k+m1k+m1大的。按照我们之前讲过的Beta分布的逻辑，p其实应该服从α=k+m1,β=n−k+1+m2α=k+m1,β=n−k+1+m2的Beta分布。我们知道贝叶斯学派进行参数估计的基本过程是

先验分布 + 后验数据 = 后验分布

对应到Beta分布，后验数据其实相当于是做了m次Bernoulli实验，其中m1m1次比p小，m2m2次比p大，相当于

Beta(p∥α,β)+BinomCount(m1,m2)=Beta(p∥α+m1,β+m2)Beta(p‖α,β)+BinomCount(m1,m2)=Beta(p‖α+m1,β+m2)

上面这个式子描述的就是Beta−Bonomial共轭Beta−Bonomial共轭.

共轭的意思是，参数的先验分布和后验分布都能保持Beta分布的形式，这样的好处是，我们能够在先验分布中赋予参数明确的物理意义，并且这个物理意义可以通过后验数据，延续到后验分布中进行解释。

由上边的解释可知，Beta分布重的参数α,βα,β其实都可以理解为物理技术，这两个参数也经常被称为伪计数（pseudo-count)。所以，Beta(α,β)Beta(α,β)也可以理解为

Beta(α,β)=Beta(1,1)+BinomCount(α−1,β−1)Beta(α,β)=Beta(1,1)+BinomCount(α−1,β−1)

其中

Beta(1,1)=Γ(1+1)Γ(1)Γ(1)x1−1(1−x)1−1=1Beta(1,1)=Γ(1+1)Γ(1)Γ(1)x1−1(1−x)1−1=1

这恰好就是均匀分布Uniform(0,1)Uniform(0,1)。

贝叶斯学派和频率学派的不同

>假设有一个不均匀的硬币，抛出正面的概率为p，抛掷mm次后，出现正面和翻面的次数分别为m1m1和m2m2，那么按照传统频率学派的观点，p的估计值应该为p^=m1mp^=m1m,而从贝叶斯学派的观点来看，开始对硬币不均匀性一无所知，所以应该假设p服从均匀分布Uniform(0,1)Uniform(0,1),也就是Beta(1,1)Beta(1,1),于是在有了后验数据之后，我们得出p其实应该服从Beta(p|m1+1,m2+1)Beta(p|m1+1,m2+1).

百变星君Beta分布



Beta分布的概率密度如上图，α,βα,β的不同，他可以是凹的、凸的、单调上升的、单调下降的，可以是曲线也可以是直线； 而且，如前所述，均匀分布也是Beta分布的一种特殊形式。正是由于Beta分布能够你和如何之多的形状，因此他经常被贝叶斯学派用作先验分布。

Dirichlet-Multinomial共轭：Beta分布的高维推广

更一步的问题

1. X∼Uniform(0,1)X∼Uniform(0,1);
2. 随机生成n个数，排序后为X1,X2,...,XnX1,X2,...,Xn;
3. 求(Xk1,Xk2)(Xk1,Xk2)的联合分布。

同推导Beta分布类似,我们取ΔxΔx足够小，只能容纳一个点.



由于ΔxΔx足够小，我们有x1+x2+x3=1x1+x2+x3=1.

P(Xk1∈(x1,x1+Δx),Xk1+k2∈(x2,x2+Δx))=(n1)(n−11)(n−2k1−1,k2−1)xk1−11xk2−12xn−k1−k23(Δx)2P(Xk1∈(x1,x1+Δx),Xk1+k2∈(x2,x2+Δx))=(n1)(n−11)(n−2k1−1,k2−1)x1k1−1x2k2−1x3n−k1−k2(Δx)2

于是我们得到(Xk1,Xk2)(Xk1,Xk2)的联合分布为

f(x1,x2,x3)=n!(k1−1)!(k2−1)!(n−k1−k2)!xk1−11x2k2−1xn−k1−k23=Gamma(n+1)Γ(k1)Γ(k2)Γ(n−k1−k2+1)xk1−11xk2−12xn−k1−k23f(x1,x2,x3)=n!(k1−1)!(k2−1)!(n−k1−k2)!x1k1−1x2k2−1x3n−k1−k2=Gamma(n+1)Γ(k1)Γ(k2)Γ(n−k1−k2+1)x1k1−1x2k2−1x3n−k1−k2

令α1=k1,α2=k2,α3=n−k1−k2+1α1=k1,α2=k2,α3=n−k1−k2+1,我们得到

f(x1,x2,x3)=Γ(α1+α2+α3)Γ(α1)Γ(α2)Γ(α3)xα1−11xα2−12xα3−13f(x1,x2,x3)=Γ(α1+α2+α3)Γ(α1)Γ(α2)Γ(α3)x1α1−1x2α2−1x3α3−1

上边这个分布其实就是一个三维形式的Dirichlet分布Dir(α1,α2,α3)Dir(α1,α2,α3).同Beta分布类似，Dirichlet分布也是一个百变星君，下图为不同αα值时Dirichlet分布的图像。



一般形式的Dirichlet分布定义如下

Dir(p⃗ ∥α⃗ )=Γ(∑Kk=1αk)∏k=1KΓ(αk)∏k=1Kpαk−1kDir(p→‖α→)=Γ(∑k=1Kαk)∏k=1KΓ(αk)∏k=1Kpkαk−1

Dirichlet分布也是Binomial共轭的

Dir(p⃗ ∥α⃗ )+MultCount(m⃗ )=Dir(p⃗ ∥α⃗ +m⃗ )Dir(p→‖α→)+MultCount(m→)=Dir(p→‖α→+m→)

我们同样也有

Dir(p⃗ ∥α⃗ )=Dir(p⃗ ∥1⃗ )+MultCount(m⃗ −1⃗ )Dir(p→‖α→)=Dir(p→‖1→)+MultCount(m→−1→)

Beta分布和Dirichlet分布的性质

如果p∼Beta(t∥α,β)p∼Beta(t‖α,β),则

E(p)=∫10t∗Beta(t∥α,β)dt=∫10t∗Γ(α+β)Γ(α)Γ(β)tα−1(1−t)β−1dt=Γ(α+β)Γ(α)Γ(β)∫10tα(1−t)β−1dtE(p)=∫01t∗Beta(t‖α,β)dt=∫01t∗Γ(α+β)Γ(α)Γ(β)tα−1(1−t)β−1dt=Γ(α+β)Γ(α)Γ(β)∫01tα(1−t)β−1dt

上式右边的积分对应到概率分布Beta(t∥α+1,β)Beta(t‖α+1,β)

Beta(t∥α+1,β)=∫10t∗Γ(α+β+1)Γ(α+1)Γ(β)tα(1−t)β−1dtBeta(t‖α+1,β)=∫01t∗Γ(α+β+1)Γ(α+1)Γ(β)tα(1−t)β−1dt

而且我们有

∫10Beta(t∥α+1,β)dt=1∫01Beta(t‖α+1,β)dt=1

所以我们有

∫10tα(1−t)β−1dt=Γ(α+1)Γ(β)Γ(α+β+1)∫01tα(1−t)β−1dt=Γ(α+1)Γ(β)Γ(α+β+1)

把上式带入E(p)中得

E(p)=Γ(α+β)Γ(α)Γ(β)⋅Γ(α+1)Γ(β)Γ(α+β+1)=αα+βE(p)=Γ(α+β)Γ(α)Γ(β)⋅Γ(α+1)Γ(β)Γ(α+β+1)=αα+β

同样的，对于Dirichlet分布我们可以得到

E(p⃗ )=(α1∑i=1Kαi,α2∑i=1Kαi,...,αK∑i=1Kαi)





Gamma分布即为多个独立且相同分布（iid）的指数分布变量的和的分布。

（最新修改，希望能够行文布局更有逻辑）

——————泊松过程——————

指数分布和泊松分布的关系十分密切，是统计学中应用极大的两种分布。

其中泊松过程是一个显著应用。

泊松过程是一个计数过程，通常用于模拟一个（非连续）事件在连续时间中发生的次数。

为一个泊松过程，则其满足三个性质：

①（t=0时什么都没发生）

②（增量）之间互相独立：

扩展补充：与互相独立，且在计数过程中





这是因为







③

即

根据增量独立性，易知其成立。

——————泊松→指数——————

假设为第次事件与第次事件的间隔时间。



所以



所以

即泊松过程的事件间隔时间为指数分布。

——————指数→Gamma—————

再令，即从头开始到第次事件的发生的时间，该随机变量分布即为Gamma分布。

即。

Gamma分布即为多个独立且相同分布（iid）的指数分布变量的和的分布。

——————证明——————

假设且互相独立

①Moment Generating Function（MGF）：

MGF的定义为

则

其性质为

下证：





则

为Gamma分布的MGF。

MGF:Moment-generating function

②数学归纳法：

已知

所以当时成立。

假设时成立

当时，



其中













为的pdf。证毕。



Gamma 分布在概率统计领域也是一个万人迷，众多统计分布和它有密切关系。指数分布和χ2χ2 分布都是特殊的Gamma 分布。另外Gamma 分布作为先验分布是很强大的，在贝叶斯统计分析中被广泛的用作其它分布的先验。如果把统计分布中的共轭关系类比为人类生活中的情侣关系的话，那指数分布、Poission分布、正态分布、对数正态分布都可以是 Gamma 分布的情人。接下来的内容中中我们主要关注β=1β=1的简单形式的 Gamma 分布。

Gamma 分布首先和 Poisson 分布、Poisson 过程发生密切的联系。我们容易发现Gamma 分布的概率密度和 Poisson 分布在数学形式上具有高度的一致性。参数为λλ的Poisson 分布，概率写为

Poisson(X=k|λ)=λke−λk!Poisson(X=k|λ)=λke−λk!

在 Gamma 分布的密度中取 α=k+1α=k+1 得到

Gamma(x|α=k+1)=xke−xΓ(k+1)=xke−xk!Gamma(x|α=k+1)=xke−xΓ(k+1)=xke−xk!

所以这两个分布数学形式上是一致的，只是 Poisson 分布是离散的，Gamma 分布是连续的，可以直观的认为 Gamma 分布是 Poisson 分布在正实数集上的连续化版本。

这种数学上的一致性是偶然的吗？这个问题我个人曾经思考了很久，终于想明白了从二项分布出发能把 Gamma 分布和 Poisson 分布紧密联系起来。我们在概率统计中都学过 Poisson(λ)Poisson(λ) 分布可以看成是二项分布 B(n,p)B(n,p) 在 np=λ,n→∞np=λ,n→∞ 条件下的极限分布。如果你对二项分布关注的足够多，可能会知道二项分布的随机变量X∼B(n,p)X∼B(n,p)满足如下一个很奇妙的恒等式

P(X≤k)=n!k!(n−k−1)!∫1ptk(1−t)n−k−1dt(∗)P(X≤k)=n!k!(n−k−1)!∫p1tk(1−t)n−k−1dt(∗)

这个等式反应的是二项分布和 Beta 分布之间的关系，证明并不难，它可以用一个物理模型直观的做概率解释，而不需要使用复杂的数学分析的方法做证明。由于这个解释和 Beta 分布有紧密的联系，所以这个直观的概率解释我们放到下一个章节，讲解 Beta/Dirichlet 分布的时候进行。此处我们暂时先承认(*)这个等式成立。我们在等式右侧做一个变换t=xnt=xn,得到

P(X≤k)=n!k!(n−k−1)!∫1ptk(1−t)n−k−1dt=n!k!(n−k−1)!∫nnp(xn)k(1−xn)n−k−1dxn=(n−1)!k!(n−k−1)!∫nnp(xn)k(1−xn)n−k−1dx=∫nnp(n−1k)(xn)k(1−xn)n−k−1dx=∫nnpBinomial(Y=k|n−1,xn)dxP(X≤k)=n!k!(n−k−1)!∫p1tk(1−t)n−k−1dt=n!k!(n−k−1)!∫npn(xn)k(1−xn)n−k−1dxn=(n−1)!k!(n−k−1)!∫npn(xn)k(1−xn)n−k−1dx=∫npn(n−1k)(xn)k(1−xn)n−k−1dx=∫npnBinomial(Y=k|n−1,xn)dx

 

B(n,p)B(n,p)

 

B(n−1,xn)B(n−1,xn)

Binomial(X≤k|n,p)=∫nnpBinomial(Y=k|n−1,xn)dxBinomial(X≤k|n,p)=∫npnBinomial(Y=k|n−1,xn)dx

np=λ,n→∞np=λ,n→∞

 

 

B(n,p)→Poisson(λ)B(n,p)→Poisson(λ)

B(n−1,xn)→Poisson(x)B(n−1,xn)→Poisson(x)

Poisson(X≤k|λ)=∫∞λPoisson(Y=k|x)dxPoisson(X≤k|λ)=∫λ∞Poisson(Y=k|x)dx

Poisson(X≤k|λ)=∫∞λPoisson(Y=k|x)dx=∫∞λxke−xk!dxPoisson(X≤k|λ)=∫λ∞Poisson(Y=k|x)dx=∫λ∞xke−xk!dx

Poisson(X≤k|λ)=∫∞λxke−xk!dx(∗∗)Poisson(X≤k|λ)=∫λ∞xke−xk!dx(∗∗)

接下来我们继续玩点好玩的，对上边的等式两边在 λ→0λ→0 下取极限，左侧Poisson分布是要至少发生k个事件的概率， λ→0λ→0 的时候就不可能有事件发生了，所以 P(X≤k)→1P(X≤k)→1, 于是我们得到

1=limλ→0∫∞λxke−xk!dx<br/>=∫∞0xke−xk!dx1=limλ→0∫λ∞xke−xk!dx<br/>=∫0∞xke−xk!dx

在这个积分式子说明 f(x)=xke−xk!f(x)=xke−xk!在正实数集上是一个概率分布函数，而这个函数恰好就是Gamma 分布。我们继续把上式右边中的 k!k! 移到左边，于是得到

k!=∫∞0xke−xdxk!=∫0∞xke−xdx

于是我们得到了 k!k! 表示为积分的方法。

看，我们从二项分布的一个等式出发, 同时利用二项分布的极限是Possion 分布这个性质，基于比较简单的逻辑，推导出了 Gamma 分布，同时把 k!k! 表达为 Gamma 函数了！实际上以上推导过程是给出了另外一种相对简单的发现 Gamma 函数的途径。

回过头我们看看()式,非常有意思，它反应了Possion 分布和 Gamma 分布的关系，这个和(*)式中中反应的二项分布和Beta 分布的关系具有完全相同的结构。把()式变形一下得到

Poisson(X≤k|λ)+∫λ0xke−xk!dx=1Poisson(X≤k|λ)+∫0λxke−xk!dx=1

我们可以看到，Poisson分布的概率累积函数和Gamma 分布的概率累积函数有互补的关系。

其实(*)和(**)这两个式子都是陈希儒院士的《概率论与数理统计》这本书第二章的课后习题，不过陈老师习题答案中给的证明思路是纯粹数学分析的证明方法，虽然能证明等式成立，但是看完证明后无法明白这两个等式是如何被发现的。上诉的论述过程说明，从二项分布出发，这两个等式都有可以很好的从概率角度进行理解。希望以上的推导过程能给大家带来一些对 Gamma 函数和 Gamma 分布的新的理解，让Gamma 分布不再神秘。





















------------
[beta分布-iVoid's Blog](http://xinsong.github.io/2014/04/29/beta/)
