几种常用概率分布表

|分布|参数|分布律或概率密度|数学期望|方差|
|0-1分布|0<p<1|$P\{X=k\}=p^k(1-p)^{1-k},k=0,1$|p|p(1-p)|
|二项分布|n≥1,0<p<1|$P\{X=k\}=\binom{n}{k}p^k(1-p)^{n-k},k=0,1...,n$|np|np(1-p)|
|负二项分布|r≥1,0<p<1|$P\{X=k\}=\binom{r-1}{k-1}p^r(1-p)^{k-r},k=r,r+1...$|r/p|$r(1-p)/p^2$|
|几何分布|0<p<1|$P\{X=k\}=(1-p)^{k-1}p,k=1,2,...$|1/p|$(1-p)/p^2$|
|超几何分布|N,M,n (M≤N)(n≤N)|$P\{X=k\}=\frac {\binom{k}{M} \binom{n-k}{N-M}}{\binom{k}{N}},k为整数,max\{0, n ~ N+M\}≤k≤min(n,M)$|$\frac {nM}N$|$\frac {nM}N (1-\frac{M}{N})(\frac{N-n}{N-1})$|
|泊松分布|λ>0|$P\{X=k\}=\frac {\lambda^k e^{- \lambda}}{k!},k=0,1,2,...,\lambda,\lambda>0$ |λ|λ|
|均匀分布|a<b|$f(x) = { 1/(b-1) , a <= x <= b ;  0 , else }$|(a+b)/2|$(b-a)^2/12$|
|正态分布 |μ,σ>0|$f(x|\mu,\sigma^2)=\dfrac{1}{\sigma\sqrt{2\pi}}e^{-\tfrac{(x-\mu)^2}{2\sigma^2}}$|μ|$σ^2$|
|Γ分布|α>0,β>0|$f(x)= \begin{cases} \displaystyle\frac {x^{\alpha-1} e^{x/\beta}} {\beta^\alpha \Gamma(\alpha)}, & 0 \leq x \leq \infty; \alpha > 0; \beta > 0 \\ \quad 0, & others \end{cases}$|αβ|$αβ^2$|
|指数分布|θ>0|$ f(x)= \begin{cases} \displaystyle \frac {1} {\theta}e^{-\lambda x} & x > 0 , \\ \quad 0, & others \end{cases}$|θ|$θ^2$|
|$χ^2$分布|n≥1||n|2n|
