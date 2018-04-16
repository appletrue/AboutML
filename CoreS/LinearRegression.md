## 线性回归

**线性回归步骤：**

- 清洗数据
- 切分训练测试
- 选择算法，训练模型
- 交叉验证调参
- 终止模型

回归分析适用于有监督学习的连续型场景，如果因变量转变为离散型变量，将转换为分类问题。如分类将预测结果离散为类别。如（吴恩达-房价预测实例）。线性回归的两个变种**岭回归**以及**Lasso回归**。

常用于分析两个变量 X 和 Y 之间的关系。假设我们有某个地区住房面积和相应房价的数据集合(训练数据)，对于这样的给定的数据，目的是要利用已有的信息，来对房价建立预测模型，当新来一个面积数据时，可以自动预测出销售价格。

线性回归，学出来的不一定是一条直线，只有在变量x是一维的时候才是直线，高维的时候是超平面。

- **特征（feature）**：xi， 比如，房屋的面积，卧室数量都算房屋的特征，（向量）

- **特征向量（输入）**：通常习惯用$X=(x_1, x_2, ...,x_n)^T \in \mathbb{R}^{n\times p}$ 表示数据矩阵，其中$x_i \in \mathbb{R}^p$表示一个p维度长的数据样本；

- **输出向量**：y，y(i) 表示了第 i 个输入所对应的输出,$Y=(y_1, y_2, ...,y_n)^T \in \mathbb{R}^{n}$表示数据的label

- **假设（hypothesis）**：也称为预测函数，比如一个线性预测函数是：

  $h_\theta(x)=\theta_0+\theta_1x_1+\theta_2x_2+\dots+\theta_nx_n=\theta^Tx$,表达式也称之为**回归方程（regression equation）**，θ 为回归系数，它是我们预测准度的基石。

对于一个样本xi，它的输出值是其特征的线性组合： $\begin{equation}f(x_i) = \sum_{m=1}^{p}w_m x_{im}+w_0={w}^T{x_i}\end{equation}$ (w0为截距，或bias)

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

$）））=E(\dfrac{1}{n-p-1}[y-X(X^{T}X)^{-1}X^{T}y]^T[y-X(X^{T}X)^{-1}X^{T}y]）$

$）））=E(\dfrac{1}{n-p-1}y^T[I_{n}-X(X^{T}X)^{-1}X^{T}]y）$

$=\dfrac{n\sigma^2}{n-p-1}-\dfrac{1}{n-p-1}\text{tr}(X(X^TX)^{-1}X^Tyy^T) $

$=\dfrac{n\sigma^2}{n-p-1}-\dfrac{\sigma^2}{n-p-1}\text{tr}(X(X^TX)^{-1}X^T) $

$=\dfrac{n\sigma^2}{n-p-1}-\dfrac{(p+1)\sigma^2}{n-p-1} =\sigma^2$

#### 一般线性回归会遇到的问题：

- 预测精度：

高维度带来的问题不止是在计算量上。例如在许多生物相关的问题中，数据的维度 非常高，但是由于收集数据需要昂贵的实验，因此可用的训练数据却相当少，这样的问题通常称为“small n, large P problem”——我们一般用 n 表示数据点的个数，用 p  表示特征的个数，即数据维度。

当 $n>= p$ 时，最小二乘回归会有较小的方差。

当 $n \approx p$ 时，容易产生过拟合。

当  p>  n  的时候，不做任何其他假设或者限制的话，学习问题基本上是没法进行的。因为如果用上所有变量的话， p越大，通常会导致模型越复杂，但是反过来 n 有很小，于是就会出现很严重的 overfitting 问题。

- 模型的解释能力：

如果模型中的特征之间有相互关系，这样会增加模型的复杂程度，并且对整个模型的解释能力并没有提高，这时，我们就要进行特征选择。

以上的这些问题，主要就是表现在模型的方差和偏差问题上。

## 过拟合和欠拟合

前提：

$x^{(i)},y^{(i)}$,——第i 个训练样本

令$x_0=1$,以参数向量 $\theta$为条件，对于输入x，输出为 $h(x)=\sum_{i=0}^n{\theta}_ix_i=\theta^Tx$,n为特征向量，

成本函数 J 定义：$J(\theta)=\dfrac{1} {2}\sum_{i=1}^m(h_{\theta}(x^{(i)}-y^{(i)})^2$,m 为训练样本；

通过正规方程组推导的结论：$\theta=(X^TX)^{-1}X^T\overrightarrow y$

#### 三种误差的计算方法：

- Training Error

$J_{train}(\theta)=\dfrac 1 {2m}\sum_{i=1}^m(h_{\theta}(x^{(i)}-y^{(i)})^2$

- Cross Validation Error

$J_{cv}(\theta)=\dfrac {1} {2m_{cv}}\sum_{i=1}^{m_{cv}}(h_{\theta}(x_{cv}^{(i)}-y_{cv}^{(i)})^2$

- Test Error

$J_{test}(\theta)=\dfrac {1} {2m_{test}}\sum_{i=1}^{m_{test}}(h_{\theta}(x_{test}^{(i)}-y_{test}^{(i)})^2$

#### 学习曲线（Learning Curves）

学习曲线就是比较 j_train 和 j_cv。如下图所示，为一般的学习曲线，蓝色的线表示训练集上的误差 j_train, 粉色的线表示验证集上的误差 j_cv，横轴表示训练集合的大小。

![learntrain](https://github.com/appletrue/NoteML/blob/master/PICs/learntrain.png)

刚开始处于 “A” 点，表示当训练数据很小时，很容易时训练集上的误差非常小，此时处于过拟合状态。随着训练数据的增加，训练数据上的误差 J_train 越来越大，而验证集上的误差 J_cv 越来越小，J_train 和 J_cv 越来越接近但始终保持 J_cv > J_train.

#### 交叉验证（Cross-Validation）

先解释一下bias和variance的概念。模型的Error = Bias + Variance，Error反映的是整个模型的准确度，Bias反映的是模型在样本上的输出与真实值之间的误差，即模型本身的精准度，Variance反映的是模型每一次输出结果与模型输出期望之间的误差，即模型的稳定性。

我们可以根据j_cv 与 j_train两个来判断是处于欠拟合还是过拟合。

![crossValid](https://github.com/appletrue/NoteML/blob/master/PICs/crossValid.jpg)

当观察到 J_cv 很大时，可能处在途中蓝色圆圈中的两个位置，虽然观察到的现象很相似(J_cv都很大)，但这两个位置的状态是非常不同的，处理方法也完全不同。

- 当cross validation error (Jcv) 跟training error(Jtrain)差不多，且Jtrain较大时，即图中标出的bias，此时 high bias low variance，当前模型更可能存在欠拟合。
- 当Jcv >> Jtrain且Jtrain较小时，即图中标出的variance时，此时 low bias high variance，当前模型更可能存在过拟合。

### 欠拟合:

—— 没有很好地捕捉到数据特征，不能够很好地拟合数据；欠拟合指的是模型在训练和预测时表现都不好的情况。

 一个欠拟合的机器学习模型不是一个良好的模型并且由于在训练数据上表现不好这是显然的， 也叫高偏差。

解决方法：

1）添加其他特征项，有时候我们模型出现欠拟合的时候是因为特征项不够导致的，可以添加其他特征项来很好地解决。例如，“组合”、“泛化”、“相关性”三类特征是特征添加的重要手段，无论在什么场景，都可以照葫芦画瓢，总会得到意想不到的效果。除上面的特征之外，“上下文特征”、“平台特征”等等，都可以作为特征添加的首选项。

**泛化：** 机器学习模型学习到的概念在它处于学习的过程中时模型没有遇见过的样本时候的表现。

2）添加多项式特征，这个在机器学习算法里面用的很普遍，例如将线性模型通过添加二次项或者三次项使模型泛化能力更强。例如上面的图片的例子。

3）减少正则化参数，正则化的目的是用来防止过拟合的，但是现在模型出现了欠拟合，则需要减少正则化参数。

### 过拟合

当某个模型过度的学习训练数据中的细节和噪音， 以至于模型在新的数据上导致在后期测试的时候不能够很好地识别数据，即不能正确的分类，模型泛化能力太差， 我们称过拟合发生了。

这意味着训练数据中的噪音或者随机波动也被当做概念被模型学习了， 也叫高方差。

解决方法：

1）优化训练集

i、清洗数据集——归一化、标准化，重新清洗数据，导致过拟合的一个原因也有可能是数据不纯导致的，如果出现了过拟合就需要我们重新清洗数据。增大数据的训练量，还有一个原因就是我们用于训练的数据量太小导致的，训练数据占总数据的比例过小。

ii、特征选择（卡方、信息增益、相关系数）

- 消除共线性
- 选择重要的特征
- 构造更快，消耗更低
- 可解释性

2）采用正则化方法。正则化方法包括L0正则、L1正则和L2正则，而正则一般是在目标函数之后加上对于的范数。但是在机器学习中一般使用L2正则。

原因如下：

L0 范数是指向量中非0的元素的个数。

L1范数是指向量中各个元素绝对值之和，也叫“稀疏规则算子”（Lasso regularization）。

两者都可以实现稀疏性，既然L0可以实现稀疏，为什么不用L0，而要用L1呢？个人理解一是因为L0范数很难优化求解（NP难问题），二是L1范数是L0范数的最优凸近似，而且它比L0范数要容易优化求解。所以大家才把目光和万千宠爱转于L1范数。

L2范数是指向量各元素的平方和然后求平方根。可以使得W的每个元素都很小，都接近于0，但与L1范数不同，它不会让它等于0，而是接近于0。

L2正则项起到使得参数w变小加剧的效果，但是为什么可以防止过拟合呢？

一个通俗的理解便是：更小的参数值w意味着模型的复杂度更低，对训练数据的拟合刚刚好（奥卡姆剃刀原理： “如无必要， 勿增实体”），不会过分拟合训练数据，从而使得不会过拟合，以提高模型的泛化能力。

3）采用dropout方法。这个方法在神经网络里面很常用。dropout方法是ImageNet中提出的一种方法，通俗一点讲就是dropout方法在训练的时候让神经元以一定的概率不工作。具体看下图：

![201804160967](https://github.com/appletrue/NoteML/blob/master/PICs/201804160967.png)

左边a图是没用用dropout方法的标准神经网络，右边b图是在训练过程中使用了dropout方法的神经网络，即在训练时候以一定的概率p来跳过一定的神经元。

#### 正则化的理解：

1、方程本身的理解：

要求参数不能差异过大，加大模型复杂度的约束。

2、线性代数方法理解：

$\nabla_\theta J(\theta)=\nabla_\theta \left  (  \dfrac{1}{2}(X\theta-y)^T(X\theta-y) \right ) $

$= \nabla_\theta \left  (  \dfrac{1}{2}(\theta^TX^T-y^T)(X\theta-y) \right ) +\lambda\theta^2$

$= \nabla_\theta \left  (  \dfrac{1}{2}(\theta^TX^TX\theta -\theta^TX^Ty -y^TX\theta+y^Ty) \right ) + \lambda \theta^2$

$求驻点=  \dfrac{1}{2}\left  (2X^TX\theta -X^Ty -(y^TX)^T \right ) = X^TX\theta -X^Ty \xrightarrow{求驻点}0$      $ (X^TX+\lambda I)^{-1}X^Ty $

岭回归即L2正则化。

3、贝叶斯理解：

假设损失函数按照均值为0， 方差为模型复杂度的一个概率分布的先验，训练数据的均方根误差代表似然。后验概率为综合先验认识和观测结果后所认为的假设空间上函数的概率分布。  

## 岭回归

多元线性回归模型中，如果所有特征一起上，容易造成过拟合使测试数据误差方差过大；因此减少不必要的特征，简化模型是减小方差的一个重要步骤。除了直接对特征筛选，来也可以进行特征压缩，减少某些不重要的特征系数，系数压缩趋近于0就可以认为舍弃该特征。

岭回归（Ridge Regression）和Lasso回归是在普通最小二乘线性回归的基础上加上正则项以对参数进行压缩惩罚，本质都是通过调节λ来实现模型误差vs方差的平衡调整。

最为常见的就是对w的模做约束。岭回归，就是在线性回归的基础上加上$l_2-norm$的约束，loss function是（习惯上一般会去掉前面线性回归目标函数中的常数项$1/n$，同时为了后面推导的简洁性会加上一个1/2）： 

首先，对于普通的最小二乘线性回归，它的代价函数是：

$\begin{equation}J_R(w)=\frac{1}{2}\|y-Xw\|^2+\frac{\lambda}{2}\|w\|^2\end{equation}$

有解析解：$\begin{equation}\hat{w}_R = (X^{T}X+\lambda I)^{-1}X^{T}y\end{equation}$

其中λ>0是一个参数，有了正则项以后解就有了很好的性质，首先是对w的模做约束，使得它的数值会比较小，很大程度上减轻了overfitting的问题；其次是上面求逆部分肯定可以解，在实际使用中ridge regression的作用很大，通过调节参数λ，可以得到不同的回归模型。

ridge regression可以用下面的优化目标形式表达：

$\begin{equation}\min_{w} \frac{1}{2}\|y-Xw\|^2, \quad s.t. \|w\|_2<\theta\end{equation}$

优化线性回归的目标，但是条件是w的模长不能超过限制θ。

上面两种优化形式是等价的，可以找到一 一对应的λ和θ。

根据线性代数的理论可知，只要样本量合适，它就存在唯一解，也就是该模型的最优解。但尽管使$J_R$达到了最小，它还是把所有的特征看作同样重要的程度来求解，并没有做任何特征选择，因此存在过拟合的可能。

**岭回归在OLS回归模型的F上加上了惩罚项（l2范数）**，这样代价函数就成为：

$\sum_{i=1}^{n}(y_i - \beta _0 - \sum_{j=1}^p \beta_j x_{ij})+ \lambda\sum_{j=1}^p\beta^2_j$ ------(岭回归的代价函数)

λ是一个非负的调节参数，可以看到：

当λ=0时，此时它与F一致，没有起到任何惩罚作用；

当λ -> ∞时，它的惩罚项也就是无穷大，而为了使代价函数最小，只能压缩系数β趋近于0。

但是因为λ不可能为无穷大，二次项求偏导时总会保留变量本身，所以事实上它也不可能真正地将某个特征压缩为0。尽管系数较小可以有效减小方差，但依然留着一大长串特征会使模型不便于解释。这是岭回归的缺点。

### 岭回归示例：

病态系统：现有现行系统，Ax=b，解方程 

$\begin{pmatrix}400&  -201\\  -800   & 401\end{pmatrix}\begin{pmatrix}x_1\\ x_2   \end{pmatrix}=\begin{pmatrix}200\\ -200  \end{pmatrix}$

很容易得到解为，x1 =-100,x2=-200,如果在样本采集时存在一个微小的误差，如，A矩阵的系数400变成401，

$\begin{pmatrix}401&  -201\\  -800   & 401\end{pmatrix}\begin{pmatrix}x_1\\ x_2   \end{pmatrix}=\begin{pmatrix}200\\ -200  \end{pmatrix}$

则得到一个截然不同的解，x1=40000,x2=79800

当解集x 对A 和b 的系数高度敏感，则这个方程组就是病态的。

$\begin{pmatrix}400+10&  -201\\  -800   & 400+10\end{pmatrix}$ 解为 x1=5.726,x2=10.685

$\begin{pmatrix}400+10&  -201\\  -801   & 400+10\end{pmatrix}$ 解为 x1=5.888,x2=11.016

因此，对岭回归的解法写作 $(x^TX + \lambda I) ^{-1}X^Ty$,即 把$X^TX$近半正定矩阵，用正定矩阵替代。

## LASSO（Least Absolute Shrinkage and Selection Operator)

又译最小绝对值收敛和选择算子、套索算法

看一下几种范式(norm)的定义， 

$\begin{equation}\|w\|_2=(\sum_{i}{w_i}^{2})^{1/2}\end{equation}$

$\begin{equation}\|w\|_1=\sum_{i}|w_i|\end{equation}$

$\begin{equation}\|w\|_0=\sum_i 1(w_i \neq 0)\end{equation}$

Ridge Regression，对w做2范式约束，就是把解约束在一个l2-ball里面，放缩是对球的半径放缩，因此w的每一个维度都在以同一个系数放缩，通过放缩不会产生稀疏的解——即某些w的维度是0。

实际应用中，数据的维度中是存在噪音和冗余的，稀疏的解可以找到有用的维度并且减少冗余，提高回归预测的准确性和鲁棒性（减少了overfitting）。在压缩感知、稀疏编码等非常多的机器学习模型中都需要用到稀疏约束。

稀疏约束最直观的形式应该是约束0范式，如上面的范式介绍，w的0范式是求w中非零元素的个数。如果约束∥w∥0≤k，就是约束非零元素个数不大于k。不过很明显，0范式是不连续的且非凸的，如果在线性回归中加上0范式的约束，就变成了一个组合优化问题：挑出≤k个系数然后做回归，找到目标函数的最小值对应的系数组合，是一个NP问题。

l1l1-norm（1范式）也可以达到稀疏的效果，是0范式的最优凸近似。

**lasso回归的正项则就把二次项改成了一次绝对值（l1范数）**，1范式容易求解，并且是凸的。具体为：

$\sum_{i=1}^{n}(y_i - \beta _0 - \sum_{j=1}^p \beta_j x_{ij})+ \lambda\sum_{j=1}^p\mid\beta_j\mid$ 

$\begin{equation}\min_{w} \frac{1}{2}\|y-Xw\|^2, \quad s.t. \|w\|_1<\theta\end{equation}$

约束在一个l1l1-ball里面。ridge和lasso的效果见下图：

![RRLasso](https://github.com/appletrue/NoteML/blob/master/PICs/RRLasso.jpg)

红色的椭圆和蓝色的区域的切点就是目标函数的最优解，我们可以看到，如果是圆，则很容易切到圆周的任意一点，但是很难切到坐标轴上，因此没有稀疏；但是如果是菱形或者多边形，则很容易切到坐标轴上，因此很容易产生稀疏的结果。这也说明了为什么1范式会是稀疏的。

一次项求导可以抹去变量本身，因此lasso回归的系数可以为0。这样可以起来真正的特征筛选效果。

$ \nabla_\theta J(\theta)= \nabla_\theta \left  (  \dfrac{1}{2}(X\theta-y)^T(X\theta-y) \right ) =\nabla_\theta \left  (  \dfrac{1}{2}(\theta^TX^T-y^T)(X\theta-y) \right ) +\lambda||\theta||$

LASSO兴起是在L2 正则化后： 1，没有碰过多高维数据；2，对LASSO的理解不够

LASSO具有特征选择的作用

##### Lasso稀疏性的进一步理解：

类似Ridge，我们也可以写出Lasso的优化目标函数：$\begin{equation}J_L(w)=\frac{1}{2}\|y-Xw\|^2+\lambda\sum_{i}|w_i|\end{equation}$

一般的思路，我们希望对JL(w)JL(w)求导数=0求出最优解，即▽JL(w)=0，但是l1-norm在0点是连续不可导的，没有gradient，这个时候需要subgradient：

**定义1：记f:U→R是一个定义在欧式空间凸集Rn上的实凸函数，在该空间中的一个向量v称为f在点x0∈U的次梯度(subgradient)，如果对于任意x∈U,满足f(x)−f(x0)≥v⋅(x−x0)成立。**

其中⋅是向量的点积。由在点x0处的所有subgradient所组成的集合称为x0处的subdifferential，记为∂f(x0)。注意subgradient和subdifferential只是对凸函数定义的。例如一维的情况，f(x)=|x|f(x)=|x|，在x=0x=0处的 subdifferential就是[−1,1]这个区间（集合）。又例如，过x0点不同线的斜率就是表示subgradient的大小，有无穷多。

**性质1：**点x0是凸函数ff的全局最小值，当且仅当0∈∂f(x0)。

在x0点不是全局最小值，因为subgradient不包含0，而原点0就是全局最小值。如果要证明也很显然，将0∈∂f(x0)带入前面的定义1中，就得到f(x)≥f(x0)。

为了方便说明，需要做一个简化假设，即数据X的列向量是orthonormal的[2,3]，即$X^TX=I$（当然没有这个假设Lasso也是可以运作的）。于是线性回归的最优解是 $\begin{equation}w^* =X^{T}y\end{equation}$

假设lasso问题JL(w)的全局最优解是w¯∈Rn，考察它的任意一个维度$\bar{w}^j$，需要分别讨论两种情况

**情况1：gradient存在的区间，即w¯j≠0 
由于gradient在最小值点=0，所以 $\begin{equation}{\left.\begin{matrix}\frac{\partial J_L(w)}{\partial w^j}\end{matrix}\right|_{\bar{w}^j}}=0\end{equation}$

$\begin{equation}-(X^{T}y-X^{T}X\bar{w})_j + \lambda\cdot \text{sgn}(\bar{w}^j)=0\end{equation}$  其中λ≥0。所以 

$\begin{equation}\bar{w}^j=w^{*j} - \lambda\cdot\text{sgn}(\bar{w}^j)\end{equation}$

看出，w¯j和w∗j是同号的，因此可以得出 

$\begin{equation}\bar{w}^j=w^{*j} - \lambda\cdot\text{sgn}(\bar{w}^j)=\text{sgn}(w^{*j})(|w^{*j}|-\lambda)\\(|w^{*j}|-\lambda)=|\bar{w}^j|\geq 0\end{equation}$

$\begin{equation}\bar{w}^j=\text{sgn}(w^{*j})(|w^{*j}|-\lambda)_+\\\end{equation}$

其中(x)+(x)+表示取xx的正数部分；(x)+=max(x,0)(x)+=max(x,0)。

**情况2：gradient不存在，即w¯j=0w¯j=0** 
根据前面的性质1，如果w¯jw¯j是最小值，则 

$\begin{equation}\textbf{0} \in \partial J_L(\bar{w})=-(X^{T}y-X^{T}X\bar{w}) + \lambda\cdot \textbf{e} = \bar{w} - w^{*}+\lambda\cdot \textbf{e}\end{equation}$

其中ee是一个向量，每一个元素ej∈[−1,1]ej∈[−1,1]，使得0=−w∗j+λ⋅ej0=−w∗j+λ⋅ej成立。因此

$\begin{equation}|w^{*j}|=\lambda |e^j|\leq \lambda\end{equation}$ 所以和情况（1）和（2）可以合并在一起。

Lasso的最优解： $\begin{equation}\bar{w}^j=\text{sgn}(w^{*j})(|w^{*j}|-\lambda)_+\\\end{equation}$

$\begin{equation}\hat{w}_R=\frac{1}{1+\lambda}w^*\\\end{equation}$

ridge实际上就是做了一个放缩，而lasso实际是做了一个soft thresholding，把很多权重项置0了，所以就得到了稀疏的结果！ 

![20180416xxx](https://github.com/appletrue/NoteML/blob/master/PICs/20180416xxx.jpg)

除了做回归，Lasso的稀疏结果天然可以做机器学习中的另外一件事——特征选择feature selection，把非零的系数对应的维度选出即可，达到对问题的精简、去噪，以及减轻overfitting。



------

参考网址：

[yoyoyohamapi-Github](https://yoyoyohamapi.gitbooks.io/mit-ml/content/)

[数据挖掘模型应用入门](https://cosx.org/2016/10/data-mining-1-lasso/)

[Sparsity and Some Basics of L1 Regularization](http://freemind.pluskid.org/machine-learning/sparsity-and-some-basics-of-l1-regularization/)

[概念](https://yoyoyohamapi.gitbooks.io/mit-ml/content/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/articles/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92%E4%B8%8E%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.html)

[回归总结](https://blog.csdn.net/hzw19920329/article/details/77200475)

[欠拟合、过拟合及其解决方法](https://blog.csdn.net/willduan1/article/details/53070777)
