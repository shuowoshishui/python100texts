"""一个整数，他加上100 后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少。"""
import math

for x in range(100000):
    if ((x + 100) % math.sqrt(x + 100)) == 0 and ((x + 468) % math.sqrt(x + 468)) == 0:
        print(x)
