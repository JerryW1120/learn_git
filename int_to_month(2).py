dict_month = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 
              5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August',
              9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'} 

index = input("请输入月份的阿拉伯数字：")
index = int(index)

if index not in dict_month.keys():
    print("你输入的月份不对！")
else:
    print(dict_month[index])