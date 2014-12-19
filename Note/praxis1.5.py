# -*- coding: utf-8 -*-
## 问:5.编写Python程序,提示输入1个数字。读入这个数字，加2，乘3，减6，再除以3。
##      得到的结果应该是最初输入的这个数字。
## -------------------------------------------------------------------------------
## 中文算法
#       1.提示用户输入(raw_input)一个 数字。   
#       2.读入这个数字字符并转换为数值型数据。
#       3.根据问题把这个数字((number+2)*3-6)/3    
#       4.判断结果是否和最初输入的这个数字一样。
## ----------------------
## English algorithm
#
#
#
#
#

# 1.输入一个Int数值,问题假如输入的不是一个数字应该如何写，在扩展中描述并需要扩展程序
numbersString = raw_input("Please input one of the number: ")
numbers =  int(numbersString)

# 2.根据公式进行计算数值
numbersFially = ((numbers + 2) * 3 - 6) / 3

if numbers == numbersFially:
    print "YES，得到的结果是最初输入的这个",numbersFially
else:
    print "NO"

