print("帮求平均值")
all_numbers = 0
count = 0
user_answer = input("输入数据并回车（输入over表示您已经输入完成）")
while user_answer != "over":
    num = float(user_answer)
    all_numbers = all_numbers + num
    count = count + 1
    user_answer = input("请继续输入数据，直到输入完成（输入over表示您已经输入完成）")
if count == 0:
    result = 0
else:
    result = all_numbers / count
print("平均值为" + str(result))
user_next = input("请问是否还有我可以帮助你的，或者你可以复制结果了")
if user_next == str("无"):
    print("谢谢你的使用")
else:
    print("谢谢你的使用")