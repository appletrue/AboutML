# Gamma函数&Lovers

Gamma 函数在概率统计中频繁现身，众多的统计分布，包括常见的统计学三大分布(t 分布，χ2 分布，F 分布)、Beta分布、 Dirichlet 分布的密度公式中都有 Gamma 函数的身影；当然发生最直接联系的概率分布是直接由 Gamma 函数变换得到的 Gamma 分布。

Gamma函数:$\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}dt$ 是阶乘运算在实数集上延伸。它具有如下性质:

$\Gamma(x+1) = x\Gamma(x)$ 因此有 $\Gamma(n)=(n-1)!$

## Gamma分布 VS 二项分布

对Gamma 函数的定义做一个变形，就可以得到如下式子$\int_0^{\infty} \frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}dx = 1$

于是，取积分中的函数作为概率密度，就得到一个形式最简单的Gamma 分布的密度函数$Gamma(x|\alpha) = \frac{x^{\alpha-1}e^{-x}}{\Gamma(\alpha)}$

如果做一个变换 x=βt, 就得到Gamma 分布的更一般的形式$Gamma(t|\alpha, \beta) = \frac{\beta^\alpha t^{\alpha-1}e^{-\beta t}}{\Gamma(\alpha)}$,其中 α 称为 shape parameter, 主要决定了分布曲线的形状;而β 称为 rate parameter 或者inverse scale parameter (1/β 称为scale parameter),主要决定曲线有多陡

![gamma-distribution](https://github.com/appletrue/NoteML/blob/master/PICs/gamma-distribution.png)

## **Gamma 分布 VS Poisson分布**

伽玛分布的概率密度和泊松分布在数学形式上具有高度的一致性。参数为λ的泊松分布，概率写为

$Poisson(X=k|\lambda) = \frac{\lambda^k e^{-\lambda}}{k!}$

在伽玛分布的密度中取 α=k+1 得到 

$Gamma(\lambda|\alpha=k+1) = \frac{\lambda^ke^{-\lambda}}{\Gamma(k+1)}= \frac{\lambda^k e^{-\lambda}}{k!}$

所以这**两个分布的数学形式具有高度的一致性**，只是**泊松分布是离散**的，**伽玛分布是连续**的。

这种数学上的一致性是偶然的吗？ 事实上，从泊松分布出发，可以利用一个简单的概率物理模型对伽玛分布的密度函数给出清晰的解释。

泊松分布可以用于描述一段时间内事件发生次数的统计性质，譬如接到的电话的次数。假设我们关心的不是一段有限的时间，而是 (0,∞) 整个时间轴上接到电话的统计性质，应该如何来描述呢？我们可以假设接到的电话满足如下性质

1.  概率在时间轴是独立均匀分布的，即每个等长的时间区间上是否接到电话是独立的，并且概率分布一样；每一个长度为h的充分小的时间片上接到一个电话的概率正比于时间片的长度；
2.  每一个充分小时间片上最多只能接到一个电话；
3.  平均而言，假设每个长度为1的单位时间片上接到电话个数是1。

如果我们考察 [0,λ] 这个时间区间，那么平均而言，这个长度为 λ 的时间片上应该接到 λ 个电话，把这个时间区间分成 n 个独立的小片，那么每个时间片上接到一个电话的概率恰好是 p=λ/n。当n 足够大的时候，每个时间片上只能是接到一个电话或者没有接到电话，恰好对应于成功概率为p 的一个贝努利实验，于是n 个时间片对应于n 个独立的贝努利实验，所以 [0,λ]这个时间区间上接到的电话总数X 应该符合二项分布

$p(X=k) = \binom{n}{k} p^k(1-p)^{n-k} .$

由于 np=λ, 于是 n 趋向于无穷的时候，电话个数X将满足参数为λ 的泊松分布

$p(X=k) = \frac{\lambda^k e^{-\lambda}}{k!} .$

熟悉随机过程理论的读者马上会发现以上模型实际上是参数为1 的泊松过程。 我们关心的问题是：什么时候会接到第k+1 个电话？或者说接到第k+1 个电话的时间点$ Y_k+1$ 会是什么概率分布？ 形式化的描述就是如何计算如下的概率？

$P(\lambda < Y_{k+1} \le \lambda + d\lambda) = ?$

上式表明第k+1 个电话落在长度为 dλ 的区间 (λ,λ+dλ] 内，这个概率事件可以分解为两个独立事件

1.  区间 (λ,λ+dλ] 内接到一个电话，这个概率是 dλ
2.  区间 [0,λ] 内接到了前k 个电话，这个概率是 

$p(X=k) = \frac{\lambda^k e^{-\lambda}}{k!} .$

于是所求的概率是以上两个事件概率相乘，即

$P(\lambda < Y_{k+1} \le \lambda + d\lambda) = p(X=k) \cdot d \lambda .$

由于第k+1 个电话必然出现在时间轴上某处，所以把时间轴所有无穷小区间上的概率累加起来，正好对应于必然事件的概率1，所以有

 $\int_0^\infty p(X=k) \cdot d \lambda = 1$

把P(X=k) 带入上式即可得到

$\int_0^\infty \frac{\lambda^k e^{-\lambda}}{k!} d \lambda = 1$

$k! = \int_0^\infty \lambda^k e^{-\lambda} d \lambda$

上述两式整好就对应于伽玛分布和伽玛函数。所以$Y_{k+1} 恰好符合伽玛分布。 我们其实从泊松分布出发，完全基于概率物理模型，推导出了伽玛函数，而推导的过程也同时给伽玛分布的密度函数提供了物理解释。

如果我们把伽玛函数和eλ的泰勒展开式对照写成如下形式:

$\begin{align} e^\lambda & = \sum_{k=0}^{\infty} {\lambda^k \over k!}--------- (3)\\ k! & = \int_0^{\infty} {\lambda^k \over e^\lambda}\ d\lambda. -------(4)\end{align}$

我们发现这两个式子形式上具有对偶关系。由于 ∑ 和∫ 都表示求和， 几乎可以认为从第一个式子只是把 $e^λ$ 和 k! 交换一下就得到了第二个式子。 这两个式子之间有更多的内在联系吗？事实上有如下一个奇妙的等式成立

$`\begin{equation} \label{gamma-e-taylor} \frac{1}{k!} \int_0^\lambda \frac{\lambda^k}{e^\lambda} d\lambda + \frac{1}{e^\lambda} \sum_{n=0}^k \frac{\lambda^n}{n!} = 1 \end{equation}`$(5)

用上面描述的泊松过程的物理模型，可以很容易的证明这个等式。我们把数轴分成 (0,λ] 和 (λ,∞) 这两个区间，考察第k+1 个电话接到时间 $Y_{k+1}$ 分别落在这两个区间的概率，当然有

 $P(Y_{k+1} \le \lambda) + P(Y_{k+1} > \lambda) = 1$

按照上述的物理模型，显然第k+1 个电话的时间落入(0,λ] 的概率为

$P(Y_{k+1} \le \lambda) = \int_0^\lambda \frac{\lambda^k e^{-\lambda}}{k!} d \lambda$

如果第k+1 个电话的时间点落入 (λ,∞)，这个事件等价地可以理解为 (0,λ]上的电话个数不能超过 k 个，由于(0,λ] 这个有限时间区间上的电话次数符合参数为λ 的泊松分布， 所以这个概率为

$P(Y_{k+1} > \lambda) = \sum_{n=0}^k \frac{\lambda^n e^{-\lambda} }{n!}$ 

得到 $`\begin{equation} \label{poisson-gamma-dual} \int_0^\lambda \frac{\lambda^k e^{-\lambda}}{k!}d\lambda + \sum_{n=0}^k \frac{\lambda^n e^{-\lambda}}{n!} = 1 \end{equation}`$ (6)这个式子俗称泊松-伽玛对偶

由于泊松分布可以看做是二项分布的极限分布，所以我们也可以从二项分布的角度对伽马分布进行解释。由于

$e^{-\lambda} = \lim_{n\rightarrow \infty} (1- \frac{\lambda}{n}) ^n$

所以伽马分布的概率密度可以重写为

$`\begin{align*} \frac{\lambda^k e^{-\lambda}}{k!} & = \lim_{n\rightarrow \infty} \frac{\lambda^k (1-\frac{\lambda}{n}) ^n}{k!} \\ & = \lim_{n\rightarrow \infty} \frac{ n! n^k (\frac{\lambda}{n})^k (1-\frac{\lambda}{n}) ^n}{k! \cdot n!} \\ & = \lim_{n\rightarrow \infty} \frac{(n+k)!}{k!\cdot n!} (\frac{\lambda}{n})^k (1-\frac{\lambda}{n}) ^n \\ & = \lim_{n\rightarrow \infty} \binom{n+k}{k} (\frac{\lambda}{n})^k (1-\frac{\lambda}{n}) ^n \end{align*}`$

显然上式具有明确的二项分布的物理含义。事实上，二项分布和贝塔分布之间也存在完全类似(6) 的一个等式：

$`\begin{equation} \label{binomial-beta-dual} \frac{n!}{k!(n-k-1)!} \int_0^p t^k(1-t)^{n-k-1} dt + \sum_{v=0}^k \binom{n}{v} p^v(1-p)^{n-v} = 1 \end{equation}`$ (7)

如果我们知道n→∞时上式中二项分布的极限是泊松分布，而贝塔分布的极限是伽玛分布，那么就很容易理解(6) 其实可以看做是 (7)的极限形式

## Gamma函数到Beta分布

Beta分布是指一组定义在(0,1)区间的连续概率分布，Beta分布有α和β两个参数 α,β>0，其中α为成功次数加1，β为失败次数加1。

为了引入Beta分布，考虑如下问题

$X_1, X_2, X_3, …, X_n \stackrel{i.i.d.}{\sim}Uniform(0,1)$

把这 n 个统计变量从小到大排列，问第 k 个变量 X(k) 的分布是什么?
在概率论中有这么个看法,几乎所有的重要的分布都可以从均匀分布中生成, 例如[Box-Muller变换](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform), 该变换能从均匀分布变换到正态分布。 

考虑的概率密度函数是:$f_{X_{(k)}}(x)=\lim_{\Delta x \rightarrow 0} \frac{P( x \le X_{(k)} \le x+\Delta x)}{\Delta x}$

即在均匀分布的 [0,1]的区间内, 有 k−1k−1 个落在了 [0,x]的区间内,有1个落在了 [x+Δx]区间内, 剩下的落在了其他区间( 即 [x+Δx,1)] )内. (其实现在就可以隐隐约约看出二项分布与均匀分布的关系.)

![betajpg](https://github.com/appletrue/NoteML/blob/master/PICs/betajpg.jpg)

由于这 n 个变量都是独立同分布,服从均匀分布, 那么我们会得到:

$`\begin{align*} f_{X_{(k)}}(x) &= \lim_{\Delta x \rightarrow 0} \frac{n\times\Delta x\times C_{(n-1)}^{(k-1)}\times x^{k-1}\times(1-x-\Delta x)^{n-k}}{\Delta x}\\ \\ &=nC_{n-1}^{k-1}x^{k-1}(1-x)^{n-k}\\ \\ &=\frac{\Gamma(n+1)}{\Gamma(k) \Gamma(n-k+1)}x^{k-1}(1-x)^{n-k} \end{align*}`$

令 α=k,β=n−k−1 ,于是我们可以得到了一般意义上的Beta分布.

$\begin{equation} f(x) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1} \end{equation}$

## 共轭先验

- **定义**：在贝叶斯概率理论中，如果后验概率和先验概率满足同样的分布律，那么，先验分布和后验分布被叫做共轭分布，同时，先验分布叫做似然函数的共轭先验分布。

贝叶斯学派和频率学派一个重要的区别就是，频率学派认为模型的参数是客观存在且不变的，虽然不知道，但可以通过大量的样本估计得到；

而贝叶斯学派认为模型的参数也是一个随机变量，满足一定的分布，这也是共轭先验产生的源头。

对于某个分布，当我们对参数没有任何先验知识时，可以认为参数满足一个均匀分布（熵最大，风险最小原则）。或者我们可以把似然函数的共轭先验分布作为参数的分布。这样做有两点好处，第一由于先验是似然的共轭先验分布，所以后验和先验是共轭分布，符合直观的理解；第二对于得到的后验分布，可以作为下一轮的先验分布，形成对参数的估计链。

推广上述:如果有另外 m 个随机变量 $Y_1, Y_2, Y_3, …, Y_m \stackrel{i.i.d.}{\sim}Uniform(0,1)$， 其中有 m1 个比 X(k)小, 有 m2 个比 X(k) 大 (m1+m2=m), 那么求现在 X(k)的分布是什么?

现在的问题等价于：$X_1, X_2, X_3, …, X_n, Y_1, Y_2, Y_3, …, Y_m \stackrel{i.i.d.}{\sim}Uniform(0,1)$

把这 n+m个统计变量从小到大排列，问第 k+m1个变量 $X_{(k+m_1)}$的分布是什么? 

结论: $Beta(p|k,n-k+1) + Count(m_1,m_2) = Beta(p|k+m_1,n-k+1+m_2)$

描述的其实是体现**贝叶斯思想**的内容, 即__先验的知识 + 观测的数据 = 后验的分布__.即**为模型参数构建一个分布，然后用超参数（先验分布的参数）来控制模型的参数！**

观测的数据是 $Y_i∼B(n,p)$, 其中$ p=X_(k)$, 而观测到的数据有$ m_1/(m_1+m_2)$ 的几率落入第一个区间，$ m_2/(m_1+m_2)$ 的几率落入第二个区间. 也就是说

当**先验的知识服从Beta分布**, **观测到的数据服从二项分布**, 最终得到的后验分布依旧是 Beta分布, 这所描述的就是**Beta-Binomial共轭**.



贝塔分布中的参数可以理解为伪计数，伯努利分布的似然函数可以表示为，表示一次事件发生的概率，它为贝塔有相同的形式，因此可以用贝塔分布作为其先验分布。

变量x仅能出现于0到1之间。空气中含有的气体状态的水分。表示这种水分的一种办法就是相对湿度, 即现在的含水量与空气的最大含水量（饱和含水量）的比值。

我们听到的天气预告用语中就经常使用相对湿度这个名词。 相对湿度的值显然仅能出现于0到1之间（经常用百分比表示）。冬季塔里木盆地的日最大相对湿度和夏季日最小相对湿度。证实它们都符合贝塔分布.

------

值得提出的是, 在**Beta分布**中, 如果**α=β=1 , Beta分布即是在[0,1]之间的均匀分布**. 

我们对于参数的假设一般是从均匀分布开始, 如果数据都是服从二项分布, 所以在**后验分布 = 参数分布 + 第一批数据 + 第二批数据 +… + 第n批数据**中,对于任意的n, 最终的后验分布也一定是Beta分布.

------
## **Dirichlet分布** :

Dirichlet分布是多项分布的共轭先验分布，是Beta分布在高维上的推广！

$f(x_1,...,x_k;\alpha_1,...\alpha_k)=\frac{\Gamma(\sum \alpha_i)} {\prod \Gamma(\alpha_i)} x_1^{\alpha_1-1}*...x_k^{\alpha_k -1}$

与Beta分布和二项分布的关系一样，Dirichlet分布是多项分布的共轭先验，他们在形式上也非常接近，多项分布中的参数是底数，而Dirichlet分布的变量是底数。是超参数，用来控制二项分布的参数。

同样的内容推广到高维, 即求出$X_{(k)}, X_{(k+1)}, …, X_{(k+l)}$的联合分布, $Y_i$ 中有 $m_1$ 个比 $X_{(k)}$ 小, $m_2$ 个比$ X_(k+1)$ 小, … , $m_l$ 个比 $X_{(k+l)} $小, 那么得到 $X_{(k)},X_{(k+1)},…,X_{(k+l)} $的联合分布是高维的Beta分布, 即Dirichlet分布, $Y_i$ 服从多项分布, 最后的后验的分布依然是Dirichlet分布. 以上贝叶斯分析过程的简单直观的表述就是:

$Dir(\overrightarrow{p}|\overrightarrow{\alpha}) + MultCount(\overrightarrow{m}) = Dir(p|\overrightarrow{\alpha}+\overrightarrow{m})$

一般形式的**Dirichlet**分布定义为:

$\begin{equation} \displaystyle Dir(\overrightarrow{p}|\overrightarrow{\alpha}) = \displaystyle \frac{\Gamma(\sum_{k=1}^K\alpha_k)} {\prod_{k=1}^K\Gamma(\alpha_k)} \prod_{k=1}^K p_k^{\alpha_k-1} \end{equation}$

记 Δ(α)为Dir因子: $\Delta(\alpha) = \frac{\Gamma(\sum_{k=1}^K\alpha_k)} {\prod_{k=1}^K\Gamma(\alpha_k)}$

其中, 对于给定的 p→和 N ,多项分布定义为:$\begin{equation} \displaystyle Mult(\overrightarrow{n} |\overrightarrow{p},N) = \binom{N}{\overrightarrow{n}}\prod_{k=1}^K p_k^{n_k} \end{equation}$

------

二项分布的随机变量X∼B(n,p)满足如下一个很奇妙的恒等式$`\begin{equation} \label{binomial-beta} P(X \le k) = \frac{n!}{k!(n-k-1)!} \int_p^1 t^k(1-t)^{n-k-1} dt  \quad  (*) \end{equation}`$ <二项分布和 Beta 分布之间的关系>

Poisson(λ)分布可以看成是二项分布 B(n,p)在 np=λ,n→∞ 条件下的极限分布。Poisson分布的概率累积函数和Gamma 分布的概率累积函数有互补的关系

α=β=1 , Beta分布即是在[0,1]之间的均匀分布

Gamma函数令 α=k,β=n−k−1 ,于是我们可以得到了一般意义上的Beta分布

指数分布和χ2分布都是特殊的Gamma 分布。


------参考网址：--------

[voidcn.com](http://www.voidcn.com/article/p-xkxhkmjq-we.html)

