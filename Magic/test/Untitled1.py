MyList = "123456123456"

print(MyList[0:3])
Left = MyList[0:6]
Right = MyList[6:12]

def Convert(List):
    print(List)
    New = []
    for i in List:
        if int(i) == 1:
            New.append("000000")
        if int(i) == 2:
            New.append("000001")
        if int(i) == 3:
            New.append("000010")
        if int(i) == 4:
            New.append("000011")
        if int(i) == 5:
            New.append("000100")
        if int(i) == 6:
            New.append("000101")
    print(New)

Convert(Left)
Convert(Right)