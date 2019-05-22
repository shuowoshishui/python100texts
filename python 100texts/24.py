"""求1+2！+3！+4！+。。。+20!"""
t2 = 0
for i in range(1, 21):
    t1 = 1
    for j in range(1, i + 1):
        t1 = j * t1
    t2 += t1
print(t2)
