

极大似然法（the method of maximum likelihood）也称最大似然法，它最早是由高斯提出的，后来由英国统计学家费歇尔于1912年在其一篇文章中重新提出,并且证明了这个方法的一些性质。最大似然估计这一名称也是费歇尔给的。它是建立在最大似然原理的基础上的一个统计方法。

极大似然估计，通俗理解来说，就是在假定整体模型分布已知，利用已知的样本结果信息，反推最具有可能（最大概率）导致这些样本结果出现的模型参数值！即：“模型已定，参数未知”。

**基本思想**是找到最佳的模型参数，使得模型实现对样本的最大程度拟合，也就使样本集出现的可能性最大。极大似然估计中采样需满足一个重要的假设，就是所有的采样都是独立同分布的。

从“极大似然”的原文maximum likelihood来看，就会发现这个名称的原始含义就是“看起来最像”的意思。“看起来最像”，在很多情况下其实就是我们决策时的依据。一个总体往往都有若干个重要的参数。比如，对于正态总体来说，均值和方差就是两个非常重要的参数。但是在很多情况下，这些参数往往是不知道的，这就需要我们利用抽样所得的部分数据来做统计推断。

概率 VS 似然

以扔硬币为例

概率:已经硬币的参数(如正反面),推测抛硬币的各种情况的可能性,是为概率.

似然:对硬币的参数不清楚,通过抛硬币的情况去推测硬币的参数,是为似然.

最大似然估计的原理

给定一个概率分布 D，已知其[概率密度函数](https://zh.wikipedia.org/wiki/%E6%A6%82%E7%8E%87%E5%AF%86%E5%BA%A6%E5%87%BD%E6%95%B0)（连续分布）或[概率质量函数](https://zh.wikipedia.org/wiki/%E6%A6%82%E7%8E%87%E8%B4%A8%E9%87%8F%E5%87%BD%E6%95%B0)（离散分布）为$f_{D}$，以及一个分布参数$ \theta$，我们可以从这个分布中抽出一个具有![n](https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b)个值的采样${ X_{1},X_{2},\ldots ,X_{n}}$，利用$f_{D}$计算出其似然函数：

$ {\mbox{lik}}(\theta \mid x_{1},\dots ,x_{n})=f_{\theta }(x_{1},\dots ,x_{n})$

若 D是离散分布，{\displaystyle f_{\theta }}![{\displaystyle f_{\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9874ae06066a2250709085e0fb521eebff2c2fb7)即是在参数为$ \theta$时观测到这一采样的概率。若其是连续分布，$Extra close brace or missing open brace f_{\theta }}!$ f_{\theta }$则为{\displaystyle X_{1},X_{2},\ldots ,X_{n}}![X_1, X_2,\ldots, X_n](https://wikimedia.org/api/rest_v1/media/math/render/svg/d67872301909a9d739e265252ad0c7339cead069)联合分布的概率密度函数在观测值处的取值。一旦我们获得{\displaystyle X_{1},X_{2},\ldots ,X_{n}}![X_1, X_2,\ldots, X_n](https://wikimedia.org/api/rest_v1/media/math/render/svg/d67872301909a9d739e265252ad0c7339cead069)，我们就能求得一个关于{\displaystyle \theta }![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af)的估计。最大似然估计会寻找关于{\displaystyle \theta }![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af)的最可能的值（即，在所有可能的{\displaystyle \theta }![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af)取值中，寻找一个值使这个采样的“可能性”最大化）。从数学上来说，我们可以在{\displaystyle \theta }![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af)的所有可能取值中寻找一个值使得似然[函数](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0)取到最大值。这个使可能性最大的{\displaystyle {\widehat {\theta }}}![\widehat{\theta}](https://wikimedia.org/api/rest_v1/media/math/render/svg/89a031ed08d81ed4f0df984f0d9f30b7ae07be46)值即称为![\theta ](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e5ab2664b422d53eb0c7df3b87e1360d75ad9af)的**最大似然估计**。由定义，最大似然估计是样本的函数。

- 这里的[似然函数](https://zh.wikipedia.org/wiki/%E4%BC%BC%E7%84%B6%E5%87%BD%E6%95%B0)是指{\displaystyle x_{1},x_{2},\ldots ,x_{n}}![x_1,x_2,\ldots,x_n](https://wikimedia.org/api/rest_v1/media/math/render/svg/8694289524164f895d6665f163e14c4dc5ec648d)不变时，关于$ \theta$的一个函数。
- 最大似然估计不一定存在，也不一定唯一。







http://blog.csdn.net/zengxiantao1994/article/details/72787849

http://blog.csdn.net/yanqingan/article/details/6125812

https://www.zhihu.com/question/24124998

https://www.cnblogs.com/liliu/archive/2010/11/22/1883702.html

http://mp.weixin.qq.com/s?src=11&timestamp=1517391901&ver=670&signature=LnR23zIkbT3Y8V3-FodJ*K8VdopANWf1SVdmovCEugwyy-y3CAt0WRAZwSqZSU9hTyow8m4xKOYqHLra4E7m6Yt7hodJb1w1sl8r2A9YLXKH4KXR31obhxvg-B7yJV3d&new=1

http://mp.weixin.qq.com/s?src=3&timestamp=1517390749&ver=1&signature=aT9O7L-JIsHE5UKhaCubPVs1RApsDzSphq1hqjIO-zsShuMx*vkjF*uwYxN6Ng-XSPFA*0F**zOeE2vJ9xbRN9SPVptrOZMhmVCSyRsBfl-G0mDmvTQr*wBcL5HK36SSRTK5IiudgqSfkMnPSnxoNoeBxg6tVISrf5iF3PapzzY=



http://blog.csdn.net/raintungl/article/details/78188182

http://blog.csdn.net/guzhenping/article/details/43491835

http://blog.csdn.net/liu1194397014/article/details/52766760

 由上可知最大似然估计的一般求解过程：

　　（1） 写出似然函数；

　　（2） 对似然函数取对数，并整理；

　　（3） 求导数 ；

　　（4） 解似然方程

http://blog.csdn.net/chunyun0716/article/details/51111864

http://blog.csdn.net/xwl198937/article/details/53158704
