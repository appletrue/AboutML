# Sigmoid函数

最早Logistic函数是皮埃尔·弗朗索瓦·韦吕勒在1844或1845年在研究它与人口增长的关系时命名的。广义Logistic曲线可以模仿一些情况人口增长（P）的 S 形曲线。起初阶段大致是指数增长；然后随着开始变得饱和，增加变慢；最后，达到成熟时增加停止。

**定义： Sigmoid函数是一种有界的可微实函数，函数曲线上的任一点对应的导数值均为正值。**

Sigmoid函数之所以叫Sigmoid，是因其图像象一个字母S。sigmoid函数，也就是s型曲线函数，阈值函数，【如果x = a*r.其中a为倾斜系数，当a足够小，这个图形可以无限制接近你这个阈值函数】如下： 

函数：$f(z)=\cfrac{1}{1+e^{-z}}$

1. 定义域：(−∞,+∞)
2. 值域：(−1,1)
3. 函数在定义域内为连续和光滑函数

曲线图如下：函数的取值在0-1之间，且在0.5处为中心对称，并且越靠近x=0的取值斜率越大。当z趋近于无穷大时，f(z)趋近于1；当z趋近于无穷小时，f(z)趋近于0

![Logistic-curve](https://github.com/appletrue/NoteML/blob/master/PICs/Logistic-curve.png)

如何来衡量一个结果与实际计算值的差距呢？

一种思路就是，如果结果越接近，差值就越小，反之越。Sigmoid函数就提供了这样一种思路，如果计算所得值越趋近1，越接近实际结果，反之越远，所以Sigmoid函数可作为逻辑回归分类器的损失函数，如果所有的结果都能接近结果值，那么就越接近于0，如果所有样本计算完成后，结果接近于0，就表示计算结果与实际结果非常相近。

1. 性质：

- 通分：$ f(x)= \cfrac {e^z} {1+e^z}$

- "对称" ：$1-f(z) = f(-z) $

- 导数：$f'(z)=f(z)(1-f(z))$ , Sigmoid导数具体的推导过程如下： 

  $\begin{aligned} f'(z) &= (\frac{1}{1+e^{-z}})' \\ &= \frac{e^{-z}}{(1+e^{-z})^{2}} \\ &= \frac{1+e^{-z}-1}{(1+e^{-z})^{2}} \\ &= \frac{1}{(1+e^{-z})}(1-\frac{1}{(1+e^{-z})}) \\ &= f(z)(1-f(z)) \\ \end{aligned}$

  利用：函数的和的求导法则(f(x)+g(x))'=f(x)'+g(x)'， 复合函数的求导法则f(g(x))'=f(u)'g(x)'

  sigmoid 函数的导数也是小于 1 的，不仅小于 1，$f'(z)=f(z)(1-f(z)) < f(z)$ 

## 常规求导过程

 e=(a+b)(b+1)

c是a的函数，e是c的函数，如果我们用链式求导法则，分别对a和b求导，那么就是求出e对c的导数，c对a的导数，乘起来，对b求导则是求出e分别对c和d的导数，分别求c和d对b的导数，然后加起来，这种方法使我们常规的做法。计算量就变得很大，怎样能够让每次求导只计算一次呢？

从上往下开始计算，将每个单元的值计算出来，然后计算每个单元的偏导数，保存下来；接下来继续计算子单元的值，子单元的偏导数，保存下来；将最后的子单元到根节点所在的路径的所有偏导乘起来，就是该函数对这个变量的偏导。

计算的本质就是从上往下，计算的时候将值存起来，乘到后面的单元上去，这样每个路径的偏导计算只需要一次，从上到下计算一遍就得到了所有的偏导数。

BP(Backpropagation，反向传播算法)，就是如此计算的。有一个三层的神经网络，有输入、一个隐藏层，输出层，我们对损失函数求权重的偏导数，它是一个复杂的复合函数，如果先对第一层的权重求偏导，然后在对第二层的权重求偏导，会发现，其中有很多重复计算的步骤，就像上面的简单函数的示例，所以，为了避免这种消耗，我们采用的就是从后往前求偏导，求出每个单元的函数值，求出对应单元的偏导数，保存下来，一直乘下去，输入层。

 那么我们会有两个初始的权重矩阵：

$\begin{aligned} \theta^{1} = \begin{bmatrix} \theta^1_{10} &\theta^1_{11}& \theta^1_{12} \\ \theta^1_{20} &\theta^1_{21}& \theta^1_{22} \end{bmatrix} \\ \\ \theta^{2} = \begin{bmatrix} \theta^2_{10} &\theta^2_{11}& \theta^2_{12} \end{bmatrix} \end{aligned}$

得到了上面的矩阵，现在我们以sigmoid函数作为激活函数，分别来计算每一层网络的激励（假设我们只有一个样本，输入是x1,x2,输出是y）； 第一层是输入，激励就是样本的特征值；记为: 

$\begin{aligned} a^1 = \begin{bmatrix} x_0 \\ x_1 \\ x_2 \end{bmatrix} \end{aligned}$x0是偏置项，为1.

第二层是隐藏层，激励通过特征值与区中相乘得到，然后取sigmoid函数变换，得到$a^2$，未变换之前的记为$z^2$：

$\begin{aligned} z^2_1 &= \theta^1_{10} *x_0 + \theta^1_{11}*x_1+\theta^1_{12} * x_2 \\ z^2_2 &= \theta^1_{20} *x_0 + \theta^1_{21}*x_1+\theta^1_{22} * x_2 \\ z^2 &= \begin{bmatrix} z^2_1 \\ z^2_2 \end{bmatrix} \\ a^2 &= sigmoid(z^2) \\ a^2 &= \begin{bmatrix} 1\\ a^2_1\\ a^2_2 \end{bmatrix} \\ \end{aligned}$

最后加上了偏置项；

第三层是输出层：

$\begin{aligned} z^3_1 &= \theta^2_{10} *a^2_{0} + \theta^2_{11}*a^2_{1}+\theta^2_{12} * a^2_{2} \\ z^3 &= \begin{bmatrix} z^3_1 \end{bmatrix} \\ a^3 &= sigmoid(z^3) \\ a^3 &= \begin{bmatrix} a^3_1 \end{bmatrix} \\ \end{aligned}$

因为是输出层了，所以不需要再往下计算，所以不加偏置项；

计算流程从输入到输出，也称为前向传播(Forward propagation)。

根据损失函数，写出损失函数的公式，在这里，只有一个输入，一个输出，写出损失函数。

 在这里，m=1; 

$ J(\Theta) = - \frac{1}{m} \left[y^{(i)}_k \log ((h_\Theta (x^{(i)}))_k) + (1 - y^{(i)}_k)\log (1 - (h_\Theta(x^{(i)}))_k)\right] + \frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2 $
$= - \frac{1}{m}\left[ y * log(a^3) + (1-y)* log(1-a^3) \right] + \frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2 $

说明$\frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2$ 实际是所有的权重的平方和，一般不会将和偏置项相乘的放进

，后面暂时不写（正则化）

$J(\Theta) = - \frac{1}{m}\left[ y * log(a^3) + (1-y)* log(1-a^3)\right]$

式子其实是一个复合函数，y是常数，$a^3$是$z^3$的sigmoid函数变换，而$z^3$则是$a^2$与权重相乘得来的，

找到了权重在哪里，就可以求$θ^2_{12}$的偏导数，$a^3$写成$s(z^3)$,

$ \frac{\partial J(\Theta)}{\partial \theta^2_{12}}  = - \frac{1}{m}\left[ y* \frac{1}{s(z^3)} - (1-y) * \frac{1}{1-s(z^3)} \right] * s(z^3)*(1-s(z^3)) * a^2_{12} $
$=- \frac{1}{m}\left[ y* (1-s(z^3) - (1-y) * s(z^3) \right] * a^2_{12} $
$= - \frac{1}{m}\left[ y -s(z^3) \right] * a^2_{12} $
$= \frac{1}{m}\left[ s(z^3) -y \right] * a^2_{12} $
$= \frac{1}{m}\left[ a^3 -y \right] * a^2_{12} $

得到: $\frac{\partial J(\Theta)}{\partial \theta^2_{10}} = \frac{1}{m}\left[ a^3 -y \right] * a^2_{10} $
$\frac{\partial J(\Theta)}{\partial \theta^2_{11}} = \frac{1}{m}\left[ a^3 -y \right] * a^2_{11} $

根据上式子，对于第二个权重矩阵的偏导，可以由$[a^3−y]$乘以前一层网络的激励，然后除以样本个数求得，将这个差值称为$δ^3$，保存下来，使用矩阵的形式相乘，得到第二个权重矩阵的偏导数；

得到了第二个权重矩阵的偏导数，如何求第一个权重矩阵中的偏导数呢？

对 $θ^1_{12}$求偏导数

$\frac{\partial J(\Theta)}{\partial \theta^1_{12}} & = - \frac{1}{m}\left[ y* \frac{1}{s(z^3)} - (1-y) * \frac{1}{1-s(z^3)} \right] * s(z^3)*(1-s(z^3)) * \theta^2_{11}*s(z^2)*(1-s(z^2))*x_2 $
$= -\frac{1}{m}*\left[ a^3 -y \right] * \theta^2_{11}*s(z^2)*(1-s(z^2))*x_2 $
$= -\frac{1}{m} * \delta^3 * \theta^2_{11}*s(z^2)*(1-s(z^2))*x_2 $

可以看出，保存的导数可以直接乘，不需再次计算，多层网络其过程一样,多层乘下去。得到：

$\begin{align} \delta^3 &= a^3 - y \\ \delta^2 &= \delta^3 * (\theta^2)^T * s(z^2)' \end{align}$















------

[深度学习：Sigmoid函数与损失函数求导](http://blog.csdn.net/zhishengqianjun/article/details/75303820)

[关于e ：](https://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/)

