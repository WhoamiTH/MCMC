import random

n = 10000000
c = 0.0

for i in range(1, n):
    x = random.uniform(0, 2)
    y = random.uniform(0, 4)
    if x * x > y:  # 取函数下方的点，所以y的值应该小于x对应的函数值
        c += 1

print(8 * c / float(n))
# 2.67