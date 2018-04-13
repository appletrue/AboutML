## 线性回归

回归分析常用于分析两个变量 X 和 Y 之间的关系。

分类将预测结果离散为类别。如（吴恩达-房价预测实例）。

假设我们有某个地区住房面积和相应房价的数据集合(训练数据)，对于这样的给定的数据，目的是要利用已有的信息，来对房价建立预测模型，当新来一个面积数据时，可以自动预测出销售价格。

线性回归，学出来的不一定是一条直线，只有在变量x是一维的时候才是直线，高维的时候是超平面。

- **特征（feature）**：xi， 比如，房屋的面积，卧室数量都算房屋的特征

- **特征向量（输入）**：通常习惯用$X=(x_1, x_2, ...,x_n)^T \in \mathbb{R}^{n\times p}$ 表示数据矩阵，其中$x_i \in \mathbb{R}^p$表示一个p维度长的数据样本；

- **输出向量**：y，y(i) 表示了第 i 个输入所对应的输出,$Y=(y_1, y_2, ...,y_n)^T \in \mathbb{R}^{n}$表示数据的label

- **假设（hypothesis）**：也称为预测函数，比如一个线性预测函数是：

  $h_\theta(x)=\theta_0+\theta_1x_1+\theta_2x_2+\dots+\theta_nx_n=\theta^Tx$,表达式也称之为**回归方程（regression equation）**，θ 为回归系数，它是我们预测准度的基石。

对于一个样本xi，它的输出值是其特征的线性组合： $\begin{equation}f(x_i) = \sum_{m=1}^{p}w_m x_{im}+w_0={w}^T{x_i}\end{equation}$

- 损失函数：误差评估的函数在机器学习中也称为**代价函数（cost function）**

评估我们的学习效果，即评估各个真实值 y(i) 与预测值 hθ(x(i))之间的差异。最常见的，我们通过**最小均方（Least Mean Square）**来描述误差：

$J(\theta)=\dfrac{1}{2m}\sum\limits_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$, m为样本数

矩阵表达为：$J(\theta)=\dfrac{1}{2m}(X\theta-y)^T(X\theta-y)$

![882565](https://github.com/appletrue/NoteML/blob/master/PICs/882565.jpg)

图中直观理解一下线性回归优化的目标——线段距离（平方）的平均值，也就是最小化到分割面的距离和。 即最小二乘；线性回归是convex的目标函数，并且有解析解：

$\begin{equation}\hat{w}=(X^{T}X)^{-1}X^{T}y\end{equation}$

线性回归到这里就训练完成了，对每一个样本点的预测值是$f(x_i)=\hat{y_i}=\hat{w}^{T}x_i$,所以

$\begin{equation}\hat{y} = X\hat{w} = X(X^{T}X)^{-1}X^{T}y\end{equation}$

寻找到的预测值的一个几何解释：从上面的解析解$\hat{w}=(X^{T}X)^{-1}X^{T}y$,可得 $X^T(\hat{y}-y)=0$（垂直的向量相乘=0），因此实际上$\hat{y}$是y在平面X（由列向量x1和x2，假设只有两维）上的投影。

![2X](https://github.com/appletrue/NoteML/blob/master/PICs/2X.jpg)

记样本为$(x^{(i)},y^{(i)})$,对样本预测为$\hat y^{(i)}|_θ $，该记法表示该预测依赖于参数 θ 的选取。

$y=\hat y^{(i)}|_θ + ε$，其中，ε 是一个误差函数，通常认为其服从正态分布，ε ～ $N(0,σ^2) $

因此：$y - \hat y| _θ $～$N(0,σ^2) $       $ y$～$N(\hat y| _θ,σ^2) $   

------------备注---------------

假设观察值yi都是不相关的，并且方差都是σ2，并且样本点是已知（且是中心化过了的，均值为0）的。推出协方差矩阵 $\begin{equation}Var(\hat{\beta}) = (X^{T}X)^{-1}\sigma^2\end{equation}$

证明：$\begin{equation}Var(\hat{\beta}) = (X^{T}X)^{-1}X^{T}yy^{t}X(X^{T}X)^{-1}=(X^{T}X)^{-1}\sigma^2\end{equation}$

估计方差σ2，可以用

$\begin{equation}\hat{\sigma}^2=\dfrac{1}{n-p-1}\sum_{	i=1}^{n}(y_i-\hat{y}_i)^2\end{equation}$

和一般的方差的形式看起来不同，分母是n−p−1而不是n，是因为这样的估计才是σ2的无偏估计。

$））\begin{equation}\begin{array}{cc}E(\hat{\sigma}^2)=E(\dfrac{1}{n-p-1}\sum_{	i=1}^{n}(y_i-\hat{y}_i)^2)\\=E(\dfrac{1}{n-p-1}[y-X(X^{T}X)^{-1}X^{T}y]^T[y-X(X^{T}X)^{-1}X^{T}y]）\\=E(\dfrac{1}{n-p-1}y^T[I_{n}-X(X^{T}X)^{-1}X^{T}]y）\\=\dfrac{n\sigma^2}{n-p-1}-\dfrac{1}{n-p-1}\text{tr}(X(X^TX)^{-1}X^Tyy^T) \\=\dfrac{n\sigma^2}{n-p-1}-\dfrac{\sigma^2}{n-p-1}\text{tr}(X(X^TX)^{-1}X^T) \\=\dfrac{n\sigma^2}{n-p-1}-\dfrac{(p+1)\sigma^2}{n-p-1} \\=\sigma^2\\\end{array}\end{equation}$

高维度带来的问题不止是在计算量上。例如在许多生物相关的问题中，数据的维度 非常高，但是由于收集数据需要昂贵的实验，因此可用的训练数据却相当少，这样的问题通常称为“small n, large P problem”——我们一般用 n 表示数据点的个数，用 p  表示变量的个数，即数据维度。当p>= n  的时候，不做任何其他假设或者限制的话，学习问题基本上是没法进行的。因为如果用上所有变量的话， p越大，通常会导致模型越复杂，但是反过来 n 有很小，于是就会出现很严重的 overfitting 问题。



参考：

[](https://blog.csdn.net/xbinworld/article/details/43919445)

[Sparsity and Some Basics of L1 Regularization](http://freemind.pluskid.org/machine-learning/sparsity-and-some-basics-of-l1-regularization/)

[概念](https://yoyoyohamapi.gitbooks.io/mit-ml/content/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/articles/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%E4%B8%8E%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.html)
