# Sigmoid函数

最早Logistic函数是皮埃尔·弗朗索瓦·韦吕勒在1844或1845年在研究它与人口增长的关系时命名的。广义Logistic曲线可以模仿一些情况人口增长（P）的 S 形曲线。起初阶段大致是指数增长；然后随着开始变得饱和，增加变慢；最后，达到成熟时增加停止。

Sigmoid函数之所以叫Sigmoid，是因其图像象一个字母S。sigmoid函数，也就是s型曲线函数，如下： 

函数：$f(z)=\cfrac{1}{1+e^{-z}}$

1. 定义域：(−∞,+∞)
2. 值域：(−1,1)
3. 函数在定义域内为连续和光滑函数
4. 导数：$f'(z)=f(z)(1-f(z))$

曲线图如下：函数的取值在0-1之间，且在0.5处为中心对称，并且越靠近x=0的取值斜率越大。

![Logistic-curve](https://github.com/appletrue/NoteML/blob/master/PICs/Logistic-curve.png)



Sigmoid导数具体的推导过程如下： 

$\begin{aligned} f'(z) &= (\frac{1}{1+e^{-z}})' \\ &= \frac{e^{-z}}{(1+e^{-z})^{2}} \\ &= \frac{1+e^{-z}-1}{(1+e^{-z})^{2}} \\ &= \frac{1}{(1+e^{-z})}(1-\frac{1}{(1+e^{-z})}) \\ &= f(z)(1-f(z)) \\ \end{aligned}$



------
[关于e ：](https://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/)

