import copy

# 可变类型
l1 = [1, 2, 3, [4, 5]]
l2 = l1
l3 = copy.copy(l1)
l4 = copy.deepcopy(l1)
# l1表层改变
l1.append(6)
# l1内层改变
l1[3].append(7)

# 分别查看l1、l2、l3、l4的变化
print(l1)
print(l2)
print(l3)
print(l4)


# 不可变类型
t1 = (1, 2, 3)
t2 = t1
t3 = copy.copy(t1)
t4 = copy.deepcopy(t1)
# l1表层改变
t1 = (4, 5, 6)


# 分别查看t1、t2、t3、t4的变化
print(t1)
print(t2)
print(t3)
print(t4)
