## 线性回归

回归分析适用于有监督学习的连续型场景，如果因变量转变为离散型变量，将转换为分类问题。如分类将预测结果离散为类别。如（吴恩达-房价预测实例）。线性回归的两个变种岭回归以及Lasso回归。

常用于分析两个变量 X 和 Y 之间的关系。假设我们有某个地区住房面积和相应房价的数据集合(训练数据)，对于这样的给定的数据，目的是要利用已有的信息，来对房价建立预测模型，当新来一个面积数据时，可以自动预测出销售价格。

线性回归，学出来的不一定是一条直线，只有在变量x是一维的时候才是直线，高维的时候是超平面。

- **特征（feature）**：xi， 比如，房屋的面积，卧室数量都算房屋的特征，（向量）

- **特征向量（输入）**：通常习惯用$X=(x_1, x_2, ...,x_n)^T \in \mathbb{R}^{n\times p}$ 表示数据矩阵，其中$x_i \in \mathbb{R}^p$表示一个p维度长的数据样本；

- **输出向量**：y，y(i) 表示了第 i 个输入所对应的输出,$Y=(y_1, y_2, ...,y_n)^T \in \mathbb{R}^{n}$表示数据的label

- **假设（hypothesis）**：也称为预测函数，比如一个线性预测函数是：

  $h_\theta(x)=\theta_0+\theta_1x_1+\theta_2x_2+\dots+\theta_nx_n=\theta^Tx$,表达式也称之为**回归方程（regression equation）**，θ 为回归系数，它是我们预测准度的基石。

对于一个样本xi，它的输出值是其特征的线性组合： $\begin{equation}f(x_i) = \sum_{m=1}^{p}w_m x_{im}+w_0={w}^T{x_i}\end{equation}$

- **损失函数：**误差评估的函数在机器学习中也称为**代价函数（cost function）**

评估我们的学习效果，即评估各个真实值 y(i) 与预测值 hθ(x(i))之间的差异。最常见的，我们通过**最小均方（Least Mean Square）**来描述误差：

$J(\theta)=\dfrac{1}{2m}\sum\limits_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$, m为样本数。

目标：求出min J(θ）时的 θ 值即可。

#### **几何和矩阵形式理解**

矩阵表达为：$J(\theta)=\dfrac{1}{2m}(X\theta-y)^T(X\theta-y)$

![882565](https://github.com/appletrue/NoteML/blob/master/PICs/882565.jpg)

图中直观理解一下线性回归优化的目标——线段距离（平方）的平均值，也就是最小化到分割面的距离和。 即最小二乘；线性回归是convex的目标函数，并且有解析解：

$\begin{equation}\hat{w}=(X^{T}X)^{-1}X^{T}y\end{equation}$

线性回归到这里就训练完成了，对每一个样本点的预测值是$f(x_i)=\hat{y_i}=\hat{w}^{T}x_i$,所以

$\begin{equation}\hat{y} = X\hat{w} = X(X^{T}X)^{-1}X^{T}y\end{equation}$

寻找到的预测值的一个几何解释：从上面的解析解$\hat{w}=(X^{T}X)^{-1}X^{T}y$,可得 $X^T(\hat{y}-y)=0$（垂直的向量相乘=0），因此实际上$\hat{y}$是y在平面X（由列向量x1和x2，假设只有两维）上的投影。

![2X](https://github.com/appletrue/NoteML/blob/master/PICs/2X.jpg)

#### ------ 矩阵推导：---------

令矩阵A是系数矩阵,且A的列线性独立，一般A的第一列或最后一列是1，用于表示截距。y是目标结果。现在需要计算一个权重向量 ，使得差的平方错误最小，记作:

$\begin{equation*}\begin{aligned}& \underset{x}{\text{min}} && J(\theta) \\& \text{s.t.} && J(\theta)=|A\theta-y|^2\end{aligned}\end{equation*}$

对$J(\theta)$做相关变化

$\nabla J(\theta) = \nabla \frac {1}{2}(A\theta-y)^T(A\theta-y)$

$ = (\theta^TA^T-y^T)(A\theta-y) = \theta^TA^TA\theta - \theta^TA^Ty - y^TA\theta + y^Ty $

$= \theta^TA^TA\theta - y^TA\theta- y^TA\theta + y^Ty = \theta^TA^TA\theta - 2y^TA\theta + y^Ty $

E(0)是个凸函数，最小值在所有偏导为0的地方，$\dfrac{\partial J(\theta)}{\partial \theta} = 2A^TA\theta - 2A^Ty = 0$

由于A的列线性独立，所以$A^TA$ 可逆，化简上述公式，求驻点，

$2A^TA\theta - 2A^Ty = 0 $  $\Rightarrow A^TA\theta = A^Ty $

$\Rightarrow 0 = (A^TA)^{-1}A^Ty $

线性回归的本质是找到一个线性组合w，使得因变量y被由自变量A的列的线性组合表示。但实际情况，绝大多数是无法找到这种完美的解。那么采取C(A)中与b最近的向量作为其近似解。这个最近的向量，通过上面的推导，就是投影系数。可以想象一下三维空间中，直线投影到平面，通过三角关系，可以发现最近的向量是垂直的投影向量。

#### 代数形式求解：

记样本为$(x^{(i)},y^{(i)})$,对样本预测为$\hat y^{(i)}|_θ$，该记法表示该预测依赖于参数 θ 的选取。

$y=\hat y^{(i)}|_θ + ε$，其中，ε 是一个误差函数，通常认为其服从正态分布，ε ～ $N(0,σ^2) $

因此：$y - \hat y| _θ $～$N(0,σ^2) $  -------- $ y$～$N(\hat y| _θ,σ^2) $   

$l(θ) = logL(θ) = log \prod_{i=1}^m \dfrac 1{\sqrt{2 π} \sigma}exp \big( - \dfrac{(y^{(i)} - θ^T x^{(i)})^2}{2\sigma^2}\big) $

$=  \Sigma_{i=1}^m log\dfrac 1{\sqrt{2 π} \sigma}exp \big( - \dfrac{(y^{(i)} - θ^T x^{(i)})^2}{2\sigma^2}\big) $

$=m  log\dfrac 1{\sqrt{2 π} \sigma}- \dfrac{1}{\sigma^2}*\dfrac{1}{2} \Sigma^m_{i=1}{(y^{(i)} - θ^T x^{(i)})^2}$

转换为求极值的问题：

 **代数形式：Y= ax+b**

→导数/偏导数→ 在偏导数为0的地方能取到极值，且也是最值。分别对 a和b 求偏导数得到以下表达式：

$\dfrac {\partial} {\partial a} = \Sigma_{i=1}^n 2x_i (ax_i+b-y_i)$

$\dfrac {\partial} {\partial b} = \Sigma_{i=1}^n 2(ax_i+b-y_i)$

通过对二元一次方程组 进行求解

$ \Sigma_{i=1}^n 2x_i (ax_i+b-y_i) =0$

$ \Sigma_{i=1}^n 2(ax_i+b-y_i) =0$

得到：

$a = \dfrac {n\Sigma_{i=1}^n x_i y_i - \Sigma_{i=1}^n x_i  \Sigma _{i=1}^n y_i }{n\Sigma_{i=1}^n x_i^2 - (\Sigma_{i=1}^n x_i)^2 }$

$b = \dfrac {\Sigma_{i=1}^n x_i^2 \Sigma_{i=1}^ny_i - \Sigma_{i=1}^n x_i  \Sigma _{i=1}^n x_i y_i }{n\Sigma_{i=1}^n x_i^2 - (\Sigma_{i=1}^n x_i)^2 }$

------------**备注**---------------

假设观察值yi都是不相关的，并且方差都是σ2，并且样本点是已知（且是中心化过了的，均值为0）的。推出协方差矩阵 $\begin{equation}Var(\hat{\beta}) = (X^{T}X)^{-1}\sigma^2\end{equation}$

证明：$\begin{equation}Var(\hat{\beta}) = (X^{T}X)^{-1}X^{T}yy^{t}X(X^{T}X)^{-1}=(X^{T}X)^{-1}\sigma^2\end{equation}$

估计方差σ2，可以用

$\begin{equation}\hat{\sigma}^2=\dfrac{1}{n-p-1}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2\end{equation}$

和一般的方差的形式看起来不同，分母是n−p−1而不是n，是因为这样的估计才是σ2的无偏估计。

$ E(\hat{\sigma}^2)=E(\dfrac{1}{n-p-1}\sum_{	i=1}^{n}(y_i-\hat{y}_i)^2)$

$）=E(\dfrac{1}{n-p-1}[y-X(X^{T}X)^{-1}X^{T}y]^T[y-X(X^{T}X)^{-1}X^{T}y]）$

$）=E(\dfrac{1}{n-p-1}y^T[I_{n}-X(X^{T}X)^{-1}X^{T}]y）$

$=\dfrac{n\sigma^2}{n-p-1}-\dfrac{1}{n-p-1}\text{tr}(X(X^TX)^{-1}X^Tyy^T) $

$=\dfrac{n\sigma^2}{n-p-1}-\dfrac{\sigma^2}{n-p-1}\text{tr}(X(X^TX)^{-1}X^T) $

$=\dfrac{n\sigma^2}{n-p-1}-\dfrac{(p+1)\sigma^2}{n-p-1} =\sigma^2$

### 一般线性回归会遇到的问题：

- 预测精度：

高维度带来的问题不止是在计算量上。例如在许多生物相关的问题中，数据的维度 非常高，但是由于收集数据需要昂贵的实验，因此可用的训练数据却相当少，这样的问题通常称为“small n, large P problem”——我们一般用 n 表示数据点的个数，用 p  表示特征的个数，即数据维度。

当 $n>= p$ 时，最小二乘回归会有较小的方差。

当 $n \approx p$ 时，容易产生过拟合。

当  p>  n  的时候，不做任何其他假设或者限制的话，学习问题基本上是没法进行的。因为如果用上所有变量的话， p越大，通常会导致模型越复杂，但是反过来 n 有很小，于是就会出现很严重的 overfitting 问题。

- 模型的解释能力：

如果模型中的特征之间有相互关系，这样会增加模型的复杂程度，并且对整个模型的解释能力并没有提高，这时，我们就要进行特征选择。

以上的这些问题，主要就是表现在模型的方差和偏差问题上。

参考：

[csdn](https://blog.csdn.net/xbinworld/article/details/43919445)

[Sparsity and Some Basics of L1 Regularization](http://freemind.pluskid.org/machine-learning/sparsity-and-some-basics-of-l1-regularization/)

[概念](https://yoyoyohamapi.gitbooks.io/mit-ml/content/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/articles/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%E4%B8%8E%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.html)

[回归总结](https://blog.csdn.net/hzw19920329/article/details/77200475)
