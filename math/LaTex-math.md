# LaTeX 排版 数学公式

------

- 1.1 前言
- 1.2 名词解释
- 2 基本规则　【注：原帖才有“公式在线预览器”，涂鸦版】
- 3 LaTeX 的命令与环境，及基本符号
- 4 MathJax 浮动菜单
- 5 常用命令
- 6 数学标点与数学间距
- 7 环境　　　【注：部分公式会因指定标签重名而不正常显示，影响不大】
- 8 注意事项

## **名词解释**

[TeX](http://baike.baidu.com/link?url=Aaj0GOJ-wmTAztgpAbGn1mSTuo0OTSa3ITyjGzDdPaT9Xe9oL4iUCNrcJ6VWRTtb)
　　\(\rm\TeX\) 是由著名的计算机科学家 Donald E. Knuth（高德纳）发明的排版系统，利用 TeX 很一很容易的生成高质量的 dvi 文件，打印输出。利用 dvips,dvipdfmx,pdflatex 等程序生成 pdf,ps 文件，latexhtml 生成 html 文件。 它在学术界十分流行，特别是数学、物理学和计算机科学界。TeX 被普遍认为是一个很好的排版工具，特别是在处理复杂的数学公式时。利用诸如是 LaTeX 等终端软件，TeX 就能够排版出精美的文本。

[LaTeX](http://baike.baidu.com/link?url=f6oAQD7tmiGjVPrY-IFizgpLU0ZG65oKbXkDgSFxTJxPX-ajB6dS3OT4qlD5GA5t)
　　\(\rm\LaTeX\)（音译“拉泰赫”）是一种基于 TeX 的排版系统，由美国计算机学家莱斯利·兰伯特（Leslie Lamport）在 20 世纪 80 年代初期开发，利用这种格式，即使使用者没有排版和程序设计的知识也可以充分发挥由 TeX 所提供的强大功能，能在几天，甚至几小时内生成很多具有书籍质量的印刷品。对于生成复杂表格和数学公式，这一点表现得尤为突出。因此它非常适用于生成高印刷质量的科技和数学类文档。这个系统同样适用于生成从简单的信件到完整书籍的所有其他种类的文档。

[MathML](http://baike.baidu.com/link?url=9azngaV2TFCXEzDPVhwA2OBhFIr7V2fPFysV2JECLFG_b5ptFxkzXa1NAe6eIYg9c5dknUfGsgFIiBEYpxobZq)
　　MathML 即数学置标语言。数学标记语言，是一种基于 XML（标准通用标记语言的子集）的标准，用来在互联网上书写数学符号和公式的置标语言。

　　由于数学符号和公式的结构复杂且符号与符号之间存在多种逻辑关系，MathML 的格式十分繁琐。因此，大多数人都不会去手写 MathML，而是利用其它的工具来编写，其中包括 TeX 到 MathML 的转换器。在现在几个主要的网页浏览器中，最新版的 Mozilla、Mozilla Firefox 和 Netscape Navigator 都已经对 MathML 提供直接的支持。微软的 Internet Explorer 在安装了 MathPlayer 插件后也可以识别 MathML。此外，MathML 还得到了一些办公软件的支持，如 openoffice .org 和 Microsoft Office。

　　MathML 是受 XML 的启发在万维网联盟数学工作组的具体组织下产生的，作为 XML 定义的一种应用,它用标记的形式来表示数学表达式。用 MathML 形式 来描述数学表达式，不仅可以明确地表达数学内容,而且可以在 Web 的其它应用程序中实现再利用和转换。MathML 标记的递归性和树状结构使得它在计算机程序的实现上更方便、简单。MathML 使用文本的形式来描述数学表达式的树形结构,克服了传统的 Web 中使用图片表达数学公式的缺点。

ASCIIMathML
　　ASCIIMathML.js 是一种将 ASCII 符号翻译成直观的 MathML(HTML 版本)的开源 JavaScript 脚本。

　　您只要遵循简单的语法，用普通的 ASCII 字母和符号，就可以在网页上输入并显示出漂亮的数学公式。这些公式遵循 W3C 标准，目前在 Netscape7.1/Mozilla/Firefox 下可以直接观看，如果您用的是 Internet Explorer 和以之为内核的其它浏览器（如 Maxthon 或者 GreenBrowser 等），只需要下载一个 MathPlayer 插件。

[MathJax](https://mathjax-chinese-doc.readthedocs.org/en/latest/mathjax.html)
　　MathJax 是一个开源 JavaScript 库。它支持 LaTeX、MathML、AsciiMath 符号，可以运行于所有流行浏览器上。 它的设计目标是利用最新的 web 技术，构建一个支持 math 的 web 平台。支持主要的浏览器和操作系统，包括那些移动设备。 对大部分用户而言它不需要安装，即没有插件需要下载也没有软件需要安装，所以网页作者可以编写包含数学公式的页面并有信心可以自然而容易的浏览到它们。 只需要在页面中包含 MathJax 脚本和一些数学公式，其他的事情交给 MathJax 来处理吧。

　　MathJax 使用网络字体（大部分浏览器都支持）去产生高质量的排版，使其在所有分辨率都可缩放和显示，这远比使用包含公式的图片要有效得多。 MathJax 也可以用于屏幕阅读器，让视力受损者也可以使用。

　　使用 MathJax 显示数学公式是基于文本的，而非图片。它可以被搜索引擎使用，这意味着方程式和页面上的文字一样是可以被搜索的。 MathJax 允许页面作者使用 TeX、LaTeX 符号和 MathML 或者 AsciiMath 去书写公式。MathJax 甚至可以将TeX 格式转化为 MathML 格式，使其可以被原生支持 MathML 格式的浏览器更多的渲染。转化为 MathML 格式后你可以复制粘贴它们到其他程序中。

　　MathJax 是模块化的，所以它仅仅在需要时才加载它的组件，同时也可以被扩展以实现更多功能。 MathJax 同时也是高度可配置的，允许作者作出更适宜网站自身的自定义。 最重要的，MathJax 的 API 可以让你在你的网页上动态的创建公式。

我们要介绍就是 MathJax，其官网是：<http://www.mathjax.org/>，感兴趣者可以去看看。

**## LATEXLATEX的命令与环境，及基本符号**

LATEXLATEX的命令（command）是大小写敏感的：以一反斜线\ 开始，后接命令名，命令名或者是一串字母，或是单个符号。

命令名后的空格符、数字或任何非字母的字符都标志着该命令的结束。

命令可以带一些参数，通常用花括号{}括起来。

如果命令参数只有一个字符（不包括空格），花括号可以省略不写。

如果有可选参数，则用方括号[]括起来。比如3次根号下5，可写作：$\sqrt[3]5~or~\root3\of5$

LATEXLATEX的命令很丰富，MathJax支持其中最常用的那部分，具体列表，大家可以点上楼的

LATEXLATEX的环境（environment）是指形如 `\begin{环境名} ... \end{环境名}`

 部分的代码，可用于对齐等排版，后面的章节会专门讲解。

`“#、%、&、^、_、{、}、~、\`、$ 及空格符、\”在 LATEX 中被赋予新的含义：

- \# 用在参数指定编号，多用于宏（大家不必深入了解）；
- % 起单行注释作用；
- & 作为对齐环境的分隔符（关于“环境”，下面会讲述）；
- ^ 作为指数符或上标，其用法差不多相当于带一个参数的命令；
- _ 作为下标符，其用法差不多相当于带一个参数的命令；
- { } 作为群组的标记。对比一下：“`2^32` $2^32$” 与 “`2^{32}`$ 2^{32}$”（不同的是，它们在 ASCIIMathML 中是等效的）；
- ~ 是“带子”，在 MathJax 中作为空格效果使用，因为在 TEXTEX 中所有的空格和分行都将被忽略；
- `、$ 作为数学公式的标记，其中`是与“~”位于同一个键位上，一般在左上角esc键下方那个键；
- 空格符 在 TEXTEX 中所有的空格和分行都将被忽略。所有的空格或是由数学表达式逻辑的衍生；
- \ 作为TEXTEX 命令的开始标记；

如果作为文本，在 `\text`命令下，可以直接输入上述字符得到其本义效果；

但如果需要在公式中表达它，前面需加转义符“\”，比如：

比如：AB~CD^12_34 \# \% \& \_ { }AB~CD^12_34 \# \% \& \_ { }in text mode vs.vs.相同代码，不同模式，不同效果 AB CD1234#%&_{}AB CD1234#%&_{}in math mode
比如说，在LATEXLATEX公式里是忽略空格的，要想表达这个空格，在前面加转义符“\”即可。
不过“\”本身比较特殊，“\\”是作为换行符的，要表达单反斜杠，请用 \backslash ∖∖
另，换行也可用 \cr 或 \newline 命令。
如果在逻辑表达式中，&& 也可用 \And 表达，如 x=y⟺x≤y & x≥yx=y⟺x≤y & x≥y.

## **常用命令**

- **小写希腊字母：**
  \alpha α　\beta β　\gamma γ　\delta δ　\epsilon ϵϵ　\zeta ζζ　\eta ηη　\theta θθ　\iota ιι　\kappa κκ　\lambda λλ　\mu μμ　\nu νν　\xi ξξ　\omicron οο　\pi ππ　\rho ρρ　\sigma σσ　\tau ττ　\upsilon υυ　\phi ϕϕ　\chi χχ　\psi ψψ　\omega ωω
  \varepsilon εε　\vartheta ϑϑ　\varkappa ϰϰ　\varpi ϖϖ　\varrho ϱϱ　\varsigma ςς　\varphi φφ　\digamma ϝϝ
- **大写希腊字母：**
  \Gamma ΓΓ　\Delta ΔΔ　\Theta Θ　\Lambda ΛΛ　\Xi ΞΞ　\Pi ΠΠ　\Sigma ΣΣ　\Upsilon ΥΥ　\Phi ΦΦ　\Psi ΨΨ　\Omega ΩΩ
  \varGamma ΓΓ　\varDelta ΔΔ　\varTheta ΘΘ　\varLambda ΛΛ　\varXi ΞΞ　\varPi ΠΠ　\varSigma ΣΣ　\varUpsilon ΥΥ　\varPhi ΦΦ　\varPsi ΨΨ　\varOmega ΩΩ
  将对应的首字母大写即可；未罗列的表明 TEXTEX 未定义（其实也没人这么去用它）；
  还需注意：\Sigma ΣΣ 常用来表示累加（更推荐的是 `\sum` ∑∑）；\Pi ΠΠ 常用来表示累积（更推荐的是 `\prod` ∏∏）；
- **常用二元关系符：**
  < or \lt <<　\le or \leq ≤≤　\leqslant ⩽⩽
  \> or \gt >>　\ge or \geq ≥≥　\geqslant ⩾⩾
  = ==　\neq or \ne ≠≠ 　\equiv ≡≡　\mid ∣∣　\nmid ∤∤　\approx ≈≈　\sim ∼∼　\cong ≅≅
  \in ∈∈　\notin ∉∉　\ni ∋∋　\subset ⊂⊂　\supset ⊃⊃　\subseteq ⊆⊆　\supseteq ⊇⊇
  你可以在上述命令的前面加上 `\not` 来得到其否定形式，如：\not \equiv ≢≢
- **常用二元运算符：**
  + ++　- −−　\times ××　\div ÷÷　\setminus ∖∖　\pm ±±　\mp ∓∓
  \*[注][注] or \cdot ⋅⋅　* or \ast ∗∗　\star ⋆⋆　\bullet ∙∙　\circ ∘∘　\diamond ⋄⋄
  \oplus ⊕⊕　\ominus ⊖⊖　\otimes ⊗⊗　\oslash ⊘⊘　\odot ⊙⊙　\bigoplus ⨁⨁　\bigotimes ⨂⨂　\bigodot ⨀⨀
  \vee ∨∨　\wedge ∧∧　\bigvee ⋁⋁　\bigwedge ⋀⋀
  \cup ∪∪　\cap ∩∩　\bigcup ⋃⋃　\bigcap ⋂⋂
- **箭头：**
  \leftarrow or \gets ←←　\rightarrow or \to →→　\leftrightarrow ↔↔
  \Leftarrow ⇐⇐　\Rightarrow ⇒⇒　\Leftrightarrow ⇔⇔
  \longleftarrow ⟵⟵　\longrightarrow ⟶⟶　\longleftrightarrow ⟷⟷
  \Longleftarrow ⟸⟸　\Longrightarrow ⟹⟹　\Longleftrightarrow ⟺⟺
  \uparrow ↑↑　\downarrow ↓↓　\updownarrow ↕↕ 　% 可作为非括号定界符
  \Uparrow ⇑⇑　\Downarrow ⇓⇓　\Updownarrow ⇕⇕　% 可作为非括号定界符
  \rightharpoonup ⇀⇀　\rightharpoondown ⇁⇁　\leftharpoonup ↼↼　\leftharpoondown ↽↽
  \upharpoonright ↾↾　\downharpoonright ⇂⇂　\upharpoonleft ↿↿　\downharpoonleft ⇃⇃
  \nearrow ↗↗　\searrow ↘↘　\swarrow ↙↙　\nwarrow ↖↖
  \rightleftharpoons ⇌⇌　\leftrightsquigarrow ↭↭
  \nleftarrow ↚↚　\nleftrightarrow ↮↮　\nrightarrow ↛↛
  \nLeftarrow ⇍⇍　\nLeftrightarrow ⇎⇎　\nRightarrow ⇏⇏
  注意命令以long为前缀表示长箭头，及首字母大小写的区别。
  在逻辑推理中，推荐用 `\implies` 表示 ⟹⟹；推荐用 `\impliedby` 表示 ⟸⟸；推荐用 `\iff` 表示 ⟺⟺；因为符号两边会比单纯的箭头符多留出一点空白；
- **定界符：**
  ( ((　) ))
  [ or \lbrack [[　] or \rbrack ]]　\lfloor ⌊⌊　\rfloor ⌋⌋　\lceil ⌈⌈　\rceil ⌉⌉
  \{ or \lbrace {{　\} or \rbrace }}　% 仅花括号前必须加转义符 `\`
  < or \langle ⟨⟨　> or \rangle ⟩⟩
  / //　\backslash ∖∖　| or \vert ||　\|~or~\Vert ‖‖
  定界符可成对使用 `\left` 和 `\right` 命令（中间的定界符还可配合用 `\middle` 命令修饰），可实现按需要自动改变大小（即外围的自动变大）；
  `\left` 和 `\right` 命令必须在同一行配对，但用来配对的定界符并不需要与原来的是同一种括号，甚至可以使用一个句点 . 表示空的定界符（比如用在列方程组时）。
- **其它符号：**
  \spadesuit ♠♠　\heartsuit ♡♡　\clubsuit ♣♣　\diamondsuit ♢♢　\bigstar ★★
  \oint ∮∮　\int ∫∫　\iint ∬∬　\iiint ∭∭　\iiiint ⨌⨌　\dif d[注]d[注]　\partial ∂∂　\nabla ∇∇
  \because ∵∵　\therefore ∴∴　\ldots ……　\cdots ⋯⋯　\vdots ⋮⋮　\ddots ⋱⋱　\iddots ...[注]...[注]
  \infty ∞∞　\propto ∝∝　\hbar ℏℏ　\imath ıı　\jmath ȷȷ　\ell ℓℓ　\Re ℜℜ　\Im ℑℑ　\aleph ℵℵ　\wp ℘℘
  \forall ∀∀　\exists ∃∃　\lnot ¬¬　\lor ∨∨　\land ∧∧　\varnothing ∅∅　% 任意、存在、非、或、且、空集
  \odot ⊙⊙　\square ◻◻　\triangle △△　% 圆、方、三角形
  \parallel ∥∥　\nparallel ∦∦　\varparallel //[注]//[注]　\pqd ==//[注]==//[注]　\perp ⊥⊥　% 平行、不平行、平行（斜体）、平行且相等、垂直　
  \angle ∠∠　\measuredangle ∡∡　\sphericalangle ∢∢　% 角
  [注]：这是本论坛自定义的命令。

**常用数学结构：**

| LaTex公式                   | 预览                       | LaTex公式         | 预览                 | LaTex公式              | 预览                      |
| ------------------------- | ------------------------ | --------------- | ------------------ | -------------------- | ----------------------- |
| \𝚏𝚛𝚊𝚌{𝚊𝚋𝚌}{𝚡𝚢𝚣} | $ \frac{𝚊𝚋𝚌}{𝚡𝚢𝚣}$ | \overline{abc}  | $ \overline{abc}$  | \overrightarrow{abc} | $ \overrightarrow{abc}$ |
| \sqrt{abc}                | $ \sqrt{abc}$            | \underline{abc} | $\underline{abc}$  | \overleftarrow{abc}  | $ \overleftarrow{abc}$  |
| \sqrt[n]{abc}             | $ \sqrt[n]{abc}$         | \widehat{abc}   | $ \widehat{abc}$   | \overbrace{abc}      | $ \overbrace{abc}$      |
| {f'}                      | $ {f'}$                  | \widetilde{abc} | $ \widetilde{abc}$ | \underbrace{abc}     | $ \underbrace{abc}$     |

**注意**：撇 `'` 由右单引号键打出（台式机键盘在分号右面，必须要在纯英文状态下输入），二阶就打两撇，而不是打双引号，三阶就三撇，如此类推；
开方也可用这种形式表达：`\root n \of {abc}`  $\root n \of {abc}$ 

- **标准数学函数：**

  | LaTex公式 | 预览         | LaTex公式 | 预览   | LaTex公式 | 预览   | LaTex公式 | 预览     |
  | ------- | ---------- | ------- | ---- | ------- | ---- | ------- | ------ |
  | \arccos | $ \arccos$ |         |      |         |      | \arg    | $\arg$ |
  | \arcsin | $\arcsin$  |         |      |         |      | \exp    |        |
  | \sec    |            |         |      | \liminf |      | \inf    |        |
  | \cos    |            | \ker    |      | \dim    |      | \hom    |        |
  |         |            | \det    |      |         |      | \gcd    |        |

  数学函数一般用直立的Roman体排印，而普通字母一般用Italic字体（上表中左边是函数名，右边是命令代码），
  所以，需在其对应函数名（注意区分大小写）前加上∖∖，否则渲染成就如同右侧的斜体效果（这是不正确的！）；
  很奇怪，同余函数 mod 居然没收录在上面，但也需遵循上述规则：`36\equiv5\mod{31}` 36≡5mod3136≡5mod31
  还可以用命令 `\pmod` 自动加上圆括号，例如：`36\equiv5\pmod{31}` 36≡5(mod31)

## **数学标点与数学间距**



名称

逗号分号叹号问号冒号命令,;!?\𝚌𝚘𝚕𝚘𝚗示例f(x,y,z)=x+y+zP(a;m,n)=P(b;m,n)Pmn=n!/(n−m)!x2=1, x=±1?f:x↦x2名称命令示例逗号,f(x,y,z)=x+y+z分号;P(a;m,n)=P(b;m,n)叹号!Pnm=n!/(n−m)!问号?x2=1, x=±1?冒号\colonf:x↦x2 
注意逗号符，它在前面一般不留间距，后侧留有小的间距，比如：`1,234,567` 得到是 1,234,5671,234,567；
请对比：`1\mathord{,}234\mathord{,}567` 得到是 1,234,5671,234,567，或者  `\text{1,234,567}` 1,234,5671,234,567 .

需要特别说明的数学标点中的冒号，用 `\colon` 可使两侧间距比通常的冒号更紧凑。
直接从键盘上输入“`:`” 得到的是二元关系符，两侧的间距比较大，多用于比例，如：  a:b=ac:bca:b=ac:bc 
两个关系符在一起，中间没有间距，比如用 `f(x):=x^2` 可得到 f(x):=x2f(x):=x2
可以使用 `\mathpunct` 命令把一个符号看作数学标点，比如 `\colon` 等价于 `\mathpunct{:}`

省略号并不属于 TEXTEX 的数学标点类型，但却是公式中常用的标点符号。
`\ldots` 位置比较低，主要用在逗号之间，如  (1,2,…,n)(1,2,…,n) ；
`\cdots` 位置在中间，主要用在二元运算符、关系符之间，如  1+⋯+n1+⋯+n；或者没有乘号的连乘积，如 a1⋯ana1⋯an；或者连接多个积分符，如  ∫10⋯∫10∫01⋯∫01.
也可统一用命令 `\dots`，在多数情况下会自动识别各种情况，如上面的： (1,2,…,n)1+⋯+na1…an∫10…∫10a=⋯=z(1,2,…,n)1+⋯+na1…an∫01…∫01a=⋯=z 

说完数学标点，我们来说间距控制，这里仅讲如何控制水平间距。
用 `\quad` 可以得到 1em1em 的间距，其中“emem”是 TEXTEX 长度单位的一种，相当于当前字体大写字母“MM”的宽度（“exex”则是当前字体小写字母“xx”的高度）；
用 `\qquad` 可以得到 2em2em 的间距；用 `\enspace` 可以得到 0.5em0.5em 的间距；
上面主要用于文本间距控制，数学间距有其专门的单位，记为 mumu（math unit）， 1mu=1/18em1mu=1/18em
间距符(无)\,\: 𝚘𝚛 \>\;\!间距3mu4mu5mu−3mu示例abababababababababababababababababababab间距符间距示例(无)abababab\,3muabababab\: or \>4muabababab\;5muabababab\!−3muabababab
其中，利用 `\rm I\!R` 可用来得到  IRIR



------

参考网址：[数学研发论坛](http://bbs.emath.ac.cn/thread-5237-1-1.html)

