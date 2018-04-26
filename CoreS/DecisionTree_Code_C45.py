Function C4.5(R:包含连续属性的无类别属性集合,C:类别属性,S:训练集)  
/*返回一棵决策树*/  
Begin  
   If S为空,返回一个值为Failure的单个节点;  
   If S是由相同类别属性值的记录组成,  
      返回一个带有该值的单个节点;  
   If R为空,则返回一个单节点,其值为在S的记录中找出的频率最高的类别属性值;  
   [注意未出现错误则意味着是不适合分类的记录]；  
  For 所有的属性R(Ri) Do  
        If 属性Ri为连续属性，则  
     Begin  
           将Ri的最小值赋给A1：  
        将Rm的最大值赋给Am；/*m值手工设置*/  
           For j From 2 To m-1 Do Aj=A1+j*(A1Am)/m;  
           将Ri点的基于{< =Aj,>Aj}的最大信息增益属性(Ri,S)赋给A；  
     End；  
  将R中属性之间具有最大信息增益的属性(D,S)赋给D;  
   将属性D的值赋给{dj/j=1,2...m}；  
  将分别由对应于D的值为dj的记录组成的S的子集赋给{sj/j=1,2...m};  
   返回一棵树，其根标记为D;树枝标记为d1,d2...dm;  
   再分别构造以下树:  
   C4.5(R-{D},C,S1),C4.5(R-{D},C,S2)...C4.5(R-{D},C,Sm);  
End C4.5 
