# -*- coding: utf-8 -*-
## 问:24.考虑表达式(a+b)*c,但a、b和c的值为字符串类型.在Python shell
##       中会发生了什么情况?为什么?
## -----------------------------------------------------------------
## 答:在Python shell中(a+b)*c表达式将会出错,因为两个字符连接只能用+,
##    a+b会也把a和b的会值相连接如a为"5",b为"5",相连接就是"55"因为它
##    是字符相连接,但*只会出现在算术运算当中,所以会出错.
#

a = raw_input("please input a,")
b = raw_input("please input b,")
c = raw_input("please input c,")

print "output",(a + b) * c