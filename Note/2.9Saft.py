# -*- coding: UTF-8 -*-
# Bill James' safe Lead Calculator
# form http://www.slate.com/id/2185975/

# 1.Take the number of points one team is ahead.
pointsStr = raw_input("Enter the lead in points:")
points = int(pointsStr)

#2.Subtract three.
points =points -3

#3.Add a balf-point if the team that is abead has the ball.
#  and subtract a balf-point if the other team has the ball.
has_ball = raw_input("Does the lead team have the ball(Yes or No):")

if has_ball == 'Yes':
    points = points + 0.5
else:
    points = points - 0.5
#(Numbers less than zero become zero)
if points < 0:
    points = 0

#4.Square that.
points = points ** 2

#5.If the result is greater than the number o seconds left in the game,
#  the lead is safe.
seconds = int(raw_input("Enter the number of secnds remaining:"))

if points > seconds:
    print "Lead is safe."
else:
    print "Lead is not safe."