def findmax(n):

    mylist = []
    count = 0

    while count < n:
        item = int(input("请输入元素:"))
        mylist.append(item)
        count += 1

    return max(mylist)

n = int(input("请输入列表元素个数: "))
print("列表中最大的元素是：", findmax(n))


