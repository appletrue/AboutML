1、求$e^{0.03}$的近似值

设 $f(x) = e^x= \Sigma \frac {x^n}{n!}$,n=0,1,2,….

$f(0.03) = e^0.03 = e^{(0 + 0.03)} \approx e^0  + f'(0) *0.03 \approx 1+0.03 \approx 1.03$



2、求sigmoid函数的一阶导数

$f(x)=\frac{1}{1+e^{-x}}$

$f'(x) = (\frac 1{1+e^{-x}})' =  \frac{e^{-x}}{(1+e^{-x})^2} = \frac{1+e^{-x}-1}{(1+e^{-x})^2} = \frac{1}{(1+e^{-x})}(1-\frac{1}{(1+e^{-x})}) = f(x)(1-f(x))$

3、现分别有 A，B 两个容器，在容器 A 里分别有 7 个红球和 3 个白球，在容器 B 里有 1 个红球和 9 个白球，现已知从这两个容器里任意抽出了一个球，且是红球，问这个红球是来自容器 A 的概率是多少?

A、B两个容器中，从A容器中抽取概率设为P(A)，抽取颜色为红色概率设为P(B), 

P(A) =0.5 ; P(red) = (7 + 1) / (7+ 3 + 1+ 9)=8/20=0.4；P(red|A) = 7/10 =0.7

$P(A|red) = \frac{P(A)P(red|A)}{P(red)}= 0.5*0.7/0.4 = 7/8$

4、用拉格朗日乘子法求解以下约束最优化问题:

 $minf(X) = x_1^2 +x_2^2-x_1x_2-10x_1-4x_2+60$

$s.t.     h(X) =x_1+x_2-6 =0$



5、

6、
