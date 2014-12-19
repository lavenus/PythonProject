# -*- coding: utf-8 -*-
## 计算圆周长和面试的程序
## 问题:已知圆半径,计算圆周长和面积.所用到的数学公式有:
## 圆周长 = 2 * pi * r
## 圆面积 = pi * r * r
##--------------------
## 中文算法
#  (1) 提示用户输入圆的半径.
#  (2) 利用上面公式进行计算圆的周长和面积.
#  (3) 把计算得出的周长和面积输出结果
##----------------------
## English algorithm
#  calculate the area and circumference of a circla from its radius
#  Step 1: prompt for a radius
#  Step 2: apply the area formula
#  Step 3: Print out the results

import math

radiusString = raw_input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print "The circumference is: ",circumference,", and the area is: ",area


