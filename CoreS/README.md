## 机器学习导引

一、机器学习主要是从大量的数据中找到数据中潜在的模式或者规律，并利用这样的模式或者规律作用于一些未知的数据。根据数据形式的不同，可以将机器学习分为：

- 监督学习：对于监督学习的数据形式为 $\left ( \mathbf{x}^{\left ( i \right )},y^{\left ( i \right )} \right ),\; i=1\cdots n$,需要学习的是从特征 $\mathbf{x}^{\left ( i \right )}$ 到标签 $y^{\left ( i \right )}$ 的映射$f\left ( \mathbf{x}^{\left ( i \right )} \right )$。

• 典型的任务包括：预测数值型数据的回归、预测分类标签的分类、预测顺序的排序等。

通过已有的训练样本（即已知数据以及其对应的输出）来训练， 从而得到一个最优模型， 再利用这个模型将所有新的数据样本映射为相应的输出结果， 对输出结果进行简单的判断从而实现分类的目的， 那么这个最优模型也就具有了对未知数据进行分类的能力。

- 无监督学习： 对于无监督学习的数据形式为 $\left ( \mathbf{x}^{\left ( i \right )} \right ),\; i=1\cdots n$,需要学习的是特征与特征之间的一种关系。我们事先没有任何训练数据样本， 需要直接对数据进行建模。

• 典型的任务包括：聚类、异常检测等。• PCA

- 强化学习

• 强化学习的数据形式与监督学习一致，但是在学习的过程中，不要通过标签评价学习的效果，而是通过自己对预测的结果进行评估。强化学习在机器人的自动控制、计算机游戏中的人工智能等方面有着广泛的应用。

二、机器学习中的典型任务

- 回归

回归，指的是把实函数在样本点附近加以近似的有监督的函数近似问题。简单来讲，对于训练数据集，$\left ( \mathbf{x}^{\left ( i \right )},y^{\left ( i \right )} \right ),\; i=1\cdots n$,其中，$y^{\left ( i \right )}$为实数，通过学习得到一个函数：$\hat{y}=f\left ( \mathbf{x} \right )$

常用的回归算法有：线性回归，Lasso，岭回归，回归树等。

- 分类

分类，指的是对于指定的模式进行识别的有监督的模式识别问题。简单来说，对于训练数据集 $\left ( \mathbf{x}^{\left ( i \right )},y^{\left ( i \right )} \right ),\; i=1\cdots n$,其中，$y^{\left ( i \right )}$为类别型数据，如 $\left \{ -1,1 \right \}$,通过学习得到一个函数：$\hat{y}=f\left ( \mathbf{x} \right )$

常用的分类算有有：SVM，Logistic回归，BP神经网络，朴素贝叶斯等。

- 异常检测

异常检测，指的是寻找样本集 $\left ( \mathbf{x}^{\left ( i \right )} \right ),\; i=1\cdots n$ 中所包含的异常数据的问题。

通常对于这类的无监督问题，采用密度估计的方法，把靠近密度中心的数据作为正常的数据，把偏离密度中心的数据作为异常的数据。

- 聚类

聚类也是一类无监督学习问题，是将样本划分到不同的类别中。

常用的聚类算法有：K-Means，谱聚类等。

- 降维

降维，是指从高维数据中提取出关键的信息，将其转换为易于计算的低维问题，进而对其进行求解。降维可以分为无监督的降维和有监督的降维。

常用的降维算法有：PCA，SVD等。

三、机器学习的方法

在机器学习中，对于分类问题，通常可以分为两种不同的学习的方法，即：

- 判别式分类

判别式分类是指利用训练数据集$\left ( \mathbf{x}^{\left ( i \right )},y^{\left ( i \right )} \right ),\; i=1\cdots n$，求得分类类别 y 的条件概率$p\left ( y\mid \mathbf{x} \right )$ 到达最大的类别，$\hat{y}=\underset{y}{argmax}\; p\left ( y\mid \mathbf{x} \right )$这种直接利用后验概率$p\left ( y\mid \mathbf{x} \right )$进行学习的过程，称为判别式分类。

- 生成式分类

由贝叶斯定理可知：$p\left ( y\mid \mathbf{x} \right )=\frac{p\left ( \mathbf{x},y \right )}{p\left ( \mathbf{x} \right )}\propto p\left ( \mathbf{x},y \right )$,通过预测数据生成概率$p\left ( \mathbf{x},y \right )$进行模式识别的分类方法称为生成式分类。

四、机器学习中的各种模型

#### 1、线性模型

线性模型是一种较为简单的模型，其基本模型如下：

$f_{\mathbf{w}}\left ( x \right )=\sum_{j=1}^{n}w_jx_j$

在实际的使用中，通常很少直接使用这样的线性模型，通常将其进行推广，推广为基于参数的线性模型：

$f_{\mathbf{w}}\left ( x \right )=\sum_{j=1}^{n}w_j\phi _j\left ( x \right )=\mathbf{w}^T\Phi \left ( x \right )$

其中$\phi _j\left ( x \right )$ 是 基函数向量$\Phi \left ( x \right )=\left ( \phi _1\left ( x \right ),\phi _2\left ( x \right ),\cdots ,\phi _n\left ( x \right ) \right )^T$的第 j 个因子。

#### 2、核模型

核模型是针对基函数向量的设计，通常使用二元函数$K\left ( \cdot ,\cdot  \right )$表示核函数，使用较多的是高斯核函数：

$K\left ( x,c  \right )=exp\left ( -\dfrac{\left \| x-c \right \|^2}{2h^2} \right )$

其中，h和c分别对应于高斯核函数的带宽与均值。

#### 3、层级模型

与参数相关的非参数模型，称为非线性模型。在非线性模型中，有一类是层级模型。层级模型中典型的是神经网络模型。



















