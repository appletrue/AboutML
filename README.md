[台大](http://episte.math.ntu.edu.tw/cgi/mathfield.pl?fld=pro)

Github不愿以用自己的CPU去渲染数学公式或者特殊字体排版。

渲染LaTex公式的几个方法：

1、安装Chrome插件，如我使用 [GitHub with MathJax](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima/related)插件，但有时候在Typora 本地显示正常的公式，在页面显示不出或者不能正常显示，如矩阵不换行等问题。

2、CodeCogs 提供了一个[在线 LaTeX 编辑器](https://www.codecogs.com/latex/eqneditor.php?lang=zh-cn)，可以将输入的数学公式转换为图片，并自动生成 HTML 代码（也支持其他格式）

3、用[MathJax](http://www.mathjax.org/)渲染，

```html
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```

3、Github的markdown解析是通过SunDown库实现的。这个库的宗旨就是*"Standards compliant, fast,***secure***markdown processing library in C"。*快就够用就行。并没打算加latex功能。

真的要写的话在[CodeCogs Equation Editor](https://link.zhihu.com/?target=http%3A//latex.codecogs.com/)线上生成然后 `![](http://latex.codecogs.com/gif.latex?\\frac{1}{1+sin(x)})
`效果：
来插入就好，（反正是直接在url里面写就好一样很流畅，注意要双反斜线\\来escape）

线上想画什么基本都有实现，比如哪天想在github上加uml图的话可以用[http://yuml.me/diagram/scruffy/class/samples。](https://link.zhihu.com/?target=http%3A//yuml.me/diagram/scruffy/class/samples)







-----参考网址------

[github的markdown文件中插入公式](http://www.wanguanglu.com/2016/07/18/github-markdown-equation/)

[MathJax:数学公式显示引擎](https://blog.lilydjwg.me/2011/5/23/mathjax-a-good-formula-display-engine.26966.html)

[Alex dcrozz链接：](https://www.zhihu.com/question/26887527/answer/127906478)

[在markdown中插入数学公式](http://www.mashangxue123.com/markdown/902675789.html)
