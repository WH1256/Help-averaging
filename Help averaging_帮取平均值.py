# X-bar = (1/n)(x1 + x2 + …… + xn)
print("帮求平均值")
all_numbers = 0
# all_numbers为
count = 0
# count为输入数字的个数，最开始为0
user_answer = input("输入数据并回车（输入over表示您已经输入完成）")
while user_answer != "over":
    # 如果用户输入的不是over，则程序一直执行
    num = float(user_answer)
    all_numbers = all_numbers + num
    # 此处的all_numbers为所有数字之和，也就是第一次输入的数字加上第二及更多次输入的数字之和
    count = count + 1
    # 程序每执行一次，则数字总数加1
    user_answer = input("请继续输入数据，直到输入完成（输入over表示您已经输入完成）")
if count == 0:
    result = 0
    # 当用户没有输入任何数时，平均值为0
else:
    result = all_numbers / count
print("平均值为" + str(result))
user_next = input("请问是否还有我可以帮助你的，或者你可以复制结果了")
if user_next == str("无"):
    print("谢谢你的使用")
else:
    print("谢谢你的使用")