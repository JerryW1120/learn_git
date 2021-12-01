def mean(n):
    list_number = []
    sum = 0
    count = 0

    while count < n:
        number = int(input("请输入数字:"))
        list_number.append(number)
        sum += number
        count += 1

    return list_number, float(sum / n)


n = int(input("请输入列表数字个数: "))

list_number, mean_num = mean(n)

print("列表是：", list_number)

print('列表中所有数的平均值为：%.3f' % mean_num)
