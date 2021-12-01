def findmax(n):

    mylist = []
    count = 0

    while count < n:
        item = input("请输入元素:")
        mylist.append(item)
        count += 1

    int_count = 0
    str_count = 0

    for item in mylist:
        if item[0] == '-':
            item = list(item)
            item.remove('-')
            item_abs = "".join(item)

            if item_abs.isdigit():
                int_count += 1

        else:
            if item.isdigit():
                int_count += 1
            else:
                str_count += 1
                break

    if str_count == 0 and int_count == n:
        count = 0
        while count < n:
            mylist[count] = int(mylist[count])
            count += 1

    return mylist

n = int(input("请输入列表元素个数: "))
print("列表中最大的元素是：", max(findmax(n)))


