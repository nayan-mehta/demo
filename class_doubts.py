# from functools import reduce
#lambda function

# demo_list = list(range(4))
# print(demo_list)
#
# anonymous_func = lambda x: x*10
#
# # print(anonymous_func(demo_list))
#
# for i in demo_list:
#     print(anonymous_func(i))

#lamda function with map
# demo_list = list(range(4))
# print(tuple(map(lambda x:x*10 , demo_list)))

#lambda function with filter
# demo_list = list(range(4))
# print(list(filter(lambda x: (x%2 != 0),demo_list)))

#lambda function with reduce

# demo_list = list(range(4))
# print(reduce(lambda x,y:x+y, demo_list))


#User defined function
#
# def add (x,y):
#     sum = x+y
#     return sum
#
# num1=5
# num2=6
# print(add(num1,num2))


#5, range(1,6)

# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return reduce(lambda x,y:x*y, range(1,n+1))
#
# print(fac(100))

# Flag

# flag = 0

