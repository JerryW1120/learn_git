number = input("请输入一个数：")
number_int = int(number)

if number_int > 0:

    number = list(number)
    number.reverse()
    number_reverse = int("".join(number))

else:

    number = list(number)
    number.remove('-')
    number.reverse()
    number_reverse = 0 -  int("".join(number))

print("逆序后的数字为：", number_reverse)
