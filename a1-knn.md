from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ["A","A","B","B"]
    return group,labels

group,labels = createDataSet()

"""K-近邻算法：构造分类器的方法
inX  用于分类的输入向量，
dataSet 输入的训练样本集
labels  标签向量,标签向量的元素数目和矩阵dataSet的行数相同
k  选择最近邻居的数目"""
def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    # dataSet.shape[0]：求dataSet矩阵的行数
    # dataSet.shape[1]：求dataSet矩阵的列数
    # dataSet.shape：元组形式输出矩阵行数、列数
    """欧式距离计算
    tile(A, B)：将A重复B次，其中B可以是int类型也可以是元组类型,重复求向量inX与矩阵dataSet里每组数据之差"""
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    """sqDiffMat.sum(axis=0)：对矩阵的每一列求和，sqDiffMat.sum(axis=1)：对矩阵的每一行求和，
    sqDiffMat.sum()：对整个矩阵求和"""
    distances = sqDistances**0.5  # 求平方根
    """计算完所有点之间的距离后，对数据按照从小到大次序排序，确定前k个距离最小元素所在的主要分类"""
    sortedDistIndicies = distances.argsort()
    classCount = {} # 创建字典
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] #字典的key值和value值
        classCount[voteIlabel] = classCount.get(voteIlabel,0) #选择距离最小的k个点，若字典的key值中有voteIlabel，则返回0（第二个参数的值）
    #x.items()是把所有字典的项按照列表形式返回，
    #operator.itemgetter：operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),reverse=True) #按照第二元素次序为元组排序
    return sortedClassCount[0][0] #以二元组形式返回分类结果

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines) #得到文件的行数
    returnMat = zeros((numberOfLines,3)) #创建返回的numpy矩阵，以0填充
    classLabelVector = [] # 解析文件数据到列表
    index = 0
    for line in arrayOLines: #循环处理文件中的每行数据
        line = line.strip() #去掉所有回车符
        listFromLine = line.split('\t') #以tab键分隔成元素列表
        returnMat[index,:] = listFromLine[0:3] #选取前3个元素存储到特征矩阵中，
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
