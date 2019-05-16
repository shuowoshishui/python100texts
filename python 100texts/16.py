"""输入一行字符，分别统计其中的英文字符、空格、数字和其他字符的个数"""

while 1:
    n = str(input("输入一段字符："))
    letters = 0
    space = 0
    digit = 0
    others = 0
    for i in n:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            others += 1
    print("letters:", letters, "space:", space, "digit:", digit, "others:", others)
