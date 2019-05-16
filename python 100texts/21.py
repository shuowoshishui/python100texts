"""两个乒乓球队进行比赛，各出三个人，甲队为a，b，c三个人，乙队为x，y，z三个人。已经抽签决定比赛名单
有人向队员大打听比赛的名单，a说他不和x比，c说他不和x，y比，请编程找出三队赛手的名单"""
for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            dfg
            for k in range(ord('x'), ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('y')):
                        print("order is :" + 'a--' + chr(i) + ' ' + 'b--' + chr(j) + ' ' + 'c--' + chr(k))
