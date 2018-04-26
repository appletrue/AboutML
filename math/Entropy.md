## 信息熵，相对熵，交叉熵



### 香农信息量

香农信息量$=log\dfrac1p=−logp$ (以2为底)，信息量可以理解为不确定性的多少。香农信息量的单位是比特(bit)。

p越小，则不确定性越大，包含的信息量就越多。比如32支球队，在无任何先验信息的前提下，用二分法猜冠军队伍，最多猜5次，也就是$log\frac1{32}=5$。

### 信息熵(Entropy)

香农提出了“信息熵”概念，解决了对信息的量化质量问题，香农用“信息熵”来描述信源的不确定性。

“信息熵”（Information Entropy）是度量样本集合纯度最常用的一种指标，假定当前样本集合D中第K类样本所占的比例为pi(k=1,2,..,|γ|)，则D的信息熵定义为

$Ent(D)=-\sum^{|γ|}_{i=1}p_i log_2 p_i$

Ent(D)的值越小，D的纯度越高。对于二分类任务，|γ|=2

假设已知衡量不确定性大小的这个量已经存在，则这个“信息量”：

- 不会是负数
- 不确定性函数f 是概率P的单调递减函数
- 可加性：两个独立符号所产生的不确定性等于各自不确定性之和，即 $f(p_1Xp_2)=f(p_1)+f(p_2)$

同时满足这3个条件的函数 f 是负的对数函数，即 $f(p_i)=log \frac{1}{p_i} =-log p_i$

一个时间的信息量就是该事件发生的概率的负对数。

信息熵是跟所有事件的可能性有关的，是平均而言发生一个事件得到的信息量大小。所以信息熵其实是信息量的期望。

$E[-log p_i] =-\sum^n_{i=1}p_i logp_i$   ( $H(X)=−∑_{x∈X}p(x)logp(x)$))

若一事件有k 种结果，对应的概率为$P_i$,则此事件发生后所得信息量I （视为Entropy）为：

$（I =-（p_1log_2(p_1)+p_2log_2(p_2)+...+p_klog_2(p_k))

信息熵的一种解释是，它表示的是最短的平均编码长度。同样的，不确定性越大，熵就越大。

### 信息增益

熵的变化可以看做是信息增益，

设D为用（输出）类别对训练元组进行的划分，假定当前样本集合D中第i 类样本所占的比例为pi则D的熵表示为：$Entropy(D)=-\sum^{m}_{i=1}p_i log_2 p_i$

一般用这个类别的样本数量占总量的占比来作为概率的估计；

熵的实际意义表示是D中元组的类标号所需要的平均信息量。

如果将训练元组D按属性A进行划分，则A对D划分的期望信息为： 

$Gain(D,A)-Entropy(D)=\Sigma _{j=1}^v  \dfrac{D_j}{D}Entropy(D_j)$

于是，信息增益即两者的差值：$SplitInformation(D,A)=Entropy(D)-Entropy(D,A)$

### 相对熵(Relative Enrtopy)

又叫KL散度(Kullback-Leibler Divergence)

$KL(f(x)||g(X))=∑_{x∈X}f(x)⋅log\frac {f(x)}{g(x)}$

它用来衡量两个数值为**正数**的函数的相似性。

很容易证明，有三个结论：

> (1) 两函数完全相同时，KL=0
>
> (2) KL越大，差异越大
>
> (3) 对概率分布或者概率密度函数(>0), KL可用来衡量两个随机变量分布的差异性

注意，KL散度是不对称的，因此琴生和香农提出以下计算方法：

$JS(f(x)||g(x))=\frac{1}{2}[KL(f(x)||g(x)+KL(g(x)||f(x)))]$

### 交叉熵(Cross-Entropy)

对一随机事件，其真实概率分布为p(i)p(i)，从数据中得到的概率分布为q(i)q(i)，则我们定义，交叉熵为：

$H(p,q)= \sum_{i}p(i)\frac{1}{logq(i)}=-\sum_{i}p(i)log{q(i)}$

理解：

我们用p来衡量识别一个样本的信息量，也就是最小编码长度：$H(p)=∑plog\frac1p$

我们用q来估计真实分布为p的样本的信息量：$H(p,q)=∑plog\frac1q$

则估算多出来的冗余信息量$D(p||q)=H(p,q)−H(p)=∑plog\frac pq$（正好就是KL散度啊）

在机器学习中，p通常设定为真实标记的分布，q设定为训练后模型预测标记的分布。

很容易发现：

$H(p,q)=H(p)+D_{KL}(p||q)$

即：**交叉熵=信息熵+KL散度（相对熵）**

由于信息熵H(p)H(p)是固定不变的，因此我们在机器学习中就用交叉熵作为损失函数。常见的做法是先用Softmax函数将神经网络的结果转换为概率分布，然后用交叉熵刻画估算的概率分布与真实的概率分布的“距离”。

显然，$H(p,q)≥H(p)$

可由吉布斯不等式证明得到：

x>0时，有$lnx \le x-1$

因此，$\sum p log {p \over q}=-\sum p log{q \over p} \ge -\sum p({q \over p} -1)=0$

等号当且仅当在p和q分布完全一致时成立$(p_i=q_i)$



------

参考资料：

[《数学之美–吴军》](https://book.douban.com/subject/10750155/)

[Wikipedia: Information theory](https://en.wikipedia.org/wiki/Information_theory)

[Wikipedia: Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy)

[Wikipedia: Gibbs’s inequality](https://en.wikipedia.org/wiki/Gibbs%27_inequality)
