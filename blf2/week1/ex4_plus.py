#! /usr/bin/env python
#-*- coding:utf-8 -*_
cars = 100
# 每个汽车的位置
space_in_a_car = 4
# 司机个数
drivers = 30
#乘客数
passengers = 90
#多少汽车没有司机
cars_not_driven = cars - drivers
#可乘坐的汽车数等于司机的个数
cars_driven = drivers
#乘客总数
carpool_capacity = cars_driven * space_in_a_car
#平均没车的乘客数
average_passengers_per_car = passengers / cars_driven

print "There are",cars,"cars available."#hypo的这句话中are拼写错误
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
