def check(pswd):
    if len(pswd) <= 8:
        print("NG")
        return
    types = set()
    for l in pswd:
        if l.isdigit():
            types.add("d")
            continue
        if l.isupper():
            types.add("uc")
            continue
        if l.islower():
            types.add("lc")
            continue
        if l.strip().isascii():
            types.add("sp")
            continue
    if len(types) < 3:
        print("NG")
        return
        # 随机连续3个元素，和另外随机3个连续元素相同，就NG
    ng = False
    tmp = {}
    for i in range(0, len(pswd)):
        if ng:
            break
        for j in range(i, len(pswd), 3):
            if pswd[j:j + 3] in tmp:
                before = tmp[pswd[j:j + 3]]
                if before / 3 != j / 3:
                    ng = True
                    break
            tmp[pswd[j:j + 3]] = j
    print("NG") if ng else print("OK")
    return


while True:
    try:
        pswd = input().strip()
        if pswd == '':
            break
        check(pswd)
    except:
        break
