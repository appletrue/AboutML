# 极大似然法

极大似然法（the method of maximum likelihood）也称最大似然法，它最早是由高斯提出的，后来由英国统计学家费歇尔于1912年在其一篇文章中重新提出,并且证明了这个方法的一些性质。最大似然估计这一名称也是费歇尔给的。它是建立在最大似然原理的基础上的一个统计方法。

极大似然估计，通俗理解来说，就是在假定整体模型分布已知，利用已知的样本结果信息，反推最具有可能（最大概率）导致这些样本结果出现的模型参数值！即：“模型已定，参数未知”。

![maxlike](https://github.com/appletrue/NoteML/blob/master/PICs/maxlike.png)

**基本思想**是找到最佳的模型参数，使得模型实现对样本的最大程度拟合，也就使样本集出现的可能性最大。极大似然估计中采样需满足一个重要的假设，就是所有的采样都是独立同分布的。

从“极大似然”的原文maximum likelihood来看，就会发现这个名称的原始含义就是“看起来最像”的意思。“看起来最像”，在很多情况下其实就是我们决策时的依据。一个总体往往都有若干个重要的参数。比如，对于正态总体来说，均值和方差就是两个非常重要的参数。但是在很多情况下，这些参数往往是不知道的，这就需要我们利用抽样所得的部分数据来做统计推断。

## 概率 VS 似然

以扔硬币为例

- **概率**:已经硬币的参数(如正反面),推测抛硬币的各种情况的可能性,是为概率.

- **似然**:对硬币的参数不清楚,通过抛硬币的情况去推测硬币的参数,是为似然.

## 最大似然估计的原理

给定一个概率分布 D，已知其 概率密度函数（连续分布）或 概率质量函数（离散分布）为$f_{D}$，以及一个分布参数$ \theta$，我们可以从这个分布中抽出一个具有n个值的采样${ X_{1},X_{2},\ldots ,X_{n}}$，利用$f_{D}$计算出其似然函数：

$lik(\theta \mid x_1,\dots ,x_n)=f_{\theta }(x_{1},\dots ,x_{n})$

若 D 是离散分布，$ f_{\theta}$即是在参数为$\theta$时观测到这一采样的概率。

若 D 是连续分布，$f_{\theta }$ 则为$ X_{1},X_{2},\ldots ,X_{n}$联合分布的概率密度函数在观测值处的取值。

一旦我们获得$ X_{1},X_{2},... ,X_{n}$，我们就能求得一个关于${ \theta }$的估计$ \hat \theta$。它将使得随机样本$( X_{1},X_{2},\ldots ,X_{n})$（落在我们已有样本$(x_{1},x_{2},\ldots ,x_{n})$的概率取得最大值。即选择一个${\hat \theta}$，使得

$L(\hat \theta;x_1,x_2,...,x_n) =  \underset {θ∈Θ}{ max}L{\theta}(\theta; x_1,x_2,...,x_n)$ 

> 求点估计的方法：最大似然估计法、矩估计法、最小二乘法、贝叶斯估计法。重点就是最大似然法。

从数学上来说，我们可以在${ \theta }$的所有可能取值中寻找一个值使得似然函数取到最大值。这个使可能性最大的$ \hat{\theta}$值即称为${ \theta }$的**最大似然估计**。由定义，最大似然估计是样本的函数。(确定最大似然估计量的问题就归结为微分学中的求最大值问题)

- 这里的似然函数是指$ x_{1},x_{2},\ldots ,x_{n}$不变时，关于$ \theta$的一个函数。
- 最大似然估计不一定存在，也不一定唯一。

##  求解最大似然函数

两类求解：总体X是连续型，总体X是离散型。但是差不多，连续型的求解可以变成离散型的。

已知条件：总体X属连续型，概率密度 f(x;θ)，θ∈Θ

设$X_1，X_2，··· ，X_n$是来自X的一个样本，则$，，，X_1，X_2，··· ，X_n$的联合密度为：

$f(x_1,x_2,...,x_n \mid \theta)=f(x_1 \mid \theta)f(x_2 \mid \theta)...f(x_n \mid \theta)=\prod _{i=1}^n f(x_i \mid \theta)$

 设$x_1，x_2，··· ，x_n$是相应于样本$X_1，X_2，··· ，X_n$的一个样本值，则随机点（$X_1，X_2，··· ，X_n$）落在点（$x_1，x_2，··· ，x_n$）的领域内的概率近似地为：

$\prod_{i=1}^nf(x_i,\theta)dx_i$，其值随 θ 的取值而变化。**"模型已定,参数未知",此时已知为$x_1，x_2，··· ，x_n$,未知的是$\theta$**

与离散型的情况一样，我们取θ的估计值$\hat \theta$使概率$\prod_{i=1}^nf(x_i,\theta)dx_i$取得最大值，但因子$\prod_{i=1}^ndx_i$ 不随θ而改变，故只需考虑函数：

$L(\theta) = L(x_1，x_2，··· ，x_n;\theta) = \prod_{i=1}^n f(x_i;\theta)$的最大值。这里**$L(θ)$称为样本的似然函数**。若

$L(\theta) = L(x_1，x_2，··· ，x_n;\hat \theta) =\underset {\theta \in \Theta }{max} L(x_1，x_2，··· ，x_n;\hat \theta) $

则称$\hat \theta(x_1，x_2，··· ，x_n)$为$\theta$ 的最大似然估计值,称$\hat \theta(X_1，X_2，··· ，X_n)$为θ的最大似然估计量。

到这，**确定最大似然估计量的问题就归结为微分学中的求最大值**问题。

实际应用中,常用的是两边取对数,得到:

$lnL(x_1，x_2，··· ，x_n; \theta) = \Sigma_{i=1}^n lnf(x_i\mid \theta)$

$\hat l=\dfrac {1}{n} lnL$

其中,$l(\theta)=lnL(x_1，x_2，··· ，x_n; \theta) $ 称为对数似然,而$\hat l$称为平均对数似然。

而平时所称最大似然为最大的对数平均似然，即：

$\hat \theta_{mle} = \underset{\theta \in \Theta} {argmax} \hat l(\theta \mid x_1,x_2,...,x_n)=\underset {\theta} {arg max}\prod_{i=1}^nf(x_i\mid \theta)$ 

1,未知参数只有一个（θ为标量）

在似然函数满足连续、可微的正则条件下，极大似然估计量是下面微分方程的解：

$ \frac {d} {d\theta} L(\theta) = 0$ 或者等价于 $\frac{d lnL(\theta)}{d\theta}=0$

2,未知参数有多个（θ为向量）则θ可表示为具有S个分量的未知向量：

$\theta=[\theta_1,\theta_2,...,\theta_s]^T$

记梯度算子:

$\nabla_\theta= \left [ \frac  {\partial}{\partial \theta_1},\frac  {\partial}{\partial \theta_2},...,\frac  {\partial}{\partial \theta_s}\right ]^T$

若似然函数满足连续可导的条件，则最大似然估计量就是如下方程的解。

$\nabla_\theta\prod_{i=1}^n f(x_i;\theta)=\nabla_\theta lnL(\theta)=\Sigma_{i=1}^n \nabla _\theta lnP(x_i \mid \theta)=0$

方程的解只是一个估计值，只有在样本数趋于无限多的时候，它才会接近于真实值。

> **y = f(t)** 是一般常見的函数式，如果給定一個t值，f（t）函数式會赋一個值給y。
>
> **y = max f(t)**代表：y 是f(t)函式所有的值中最大的output。
>
> **y = arg max f(t)**代表：y 是f(t)函式中，會產生最大output的那個參數t。
>
> 例子:
>
> 假設有一個函式 f(t)，t 的可能範圍是 {0,1,2}，f(t=0) = 10 ; f(t=1) = 20 ; f(t=2) = 7，那分別對應的y如下：
>
> y = max f(t) = 20; y= arg max f(t) = 1
>
> 实现：
>
> | [**ArgMax**](http://cache.baidu.com/mathematica/ref/ArgMax.html)[f, x] | 给出 f 最大化的坐标 xmax                       |
> | ---------------------------------------- | -------------------------------------- |
> | [**ArgMax**](http://cache.baidu.com/mathematica/ref/ArgMax.html)[f, {x, y, ...}] | 给出 f 最大化的坐标 {xmax, ymax, ...}          |
> | [**ArgMax**](http://cache.baidu.com/mathematica/ref/ArgMax.html)[{f, cons}, {x, y, ...}] | 给出约束条件 cons 下 f 最大化的坐标                 |
> | [**ArgMax**](http://cache.baidu.com/mathematica/ref/ArgMax.html)[{f, cons}, {x, y, ...}, dom] | 给出域 dom 上 f 最大化的坐标，通常 Reals 或 Integers |

> [引自Blog](http://blog.sina.com.cn/s/blog_5f62d0dd0100ir59.html)

## 总结

求最大似然估计量 $\hat \theta$ 的一般步骤：

（1）写出似然函数；

（2）对似然函数取对数，并整理；

（3）求导数；

（4）解似然方程。

最大似然估计的特点：

1.比其他估计方法更加简单；

2.收敛性：无偏或者渐近无偏，当样本数目增加时，收敛性质会更好；

3.如果假设的类条件概率模型正确，则通常能获得较好的结果。但如果假设模型出现偏差，将导致非常差的估计结果。

![eg1-likehood](https://github.com/appletrue/NoteML/blob/master/PICs/eg1-likehood.png)

![eg2-likehood](https://github.com/appletrue/NoteML/blob/master/PICs/eg2-likehood.png)
