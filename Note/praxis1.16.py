# -*- coding: utf-8 -*-
## 问:16.提示进行输入,并将输入内容按字符串、整数和浮点数的方式在屏幕上输出。
##       哪种类型的值在这个过程中不会出错
## ----------------------------------------------------------------------------
##
##
##

#       答：字符串类型的值在这个过程中不会出错，整数和浮点数假如输入超过整数和浮点数
#           的范围值就会出错
inputString = raw_input("input String: ")
print "output string",inputString

inputInt = raw_input("input Integer: ")
inputInt = int(inputInt)
print "output int",inputInt

inputFloat = raw_input("input Floa: ")
input = float(inputFloat)
print "output float",inputFloat
