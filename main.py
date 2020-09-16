# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from sys import path, argv


class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print('path:', path)

    # 字符串顺序、反序输出
    str1 = 'python'
    print(str1[:])
    print(len(str1))
    print(str1[::-1])

    # 输入函数、条件判断
    username = input('请输入你的名字：')
    password = input('请输入密码：')
    check_user(UserInfo(username, password))


def check_user(user_info: UserInfo):
    # 用户列表
    user_list = [
        UserInfo('admin', 'admin'),
        UserInfo('ricardo', '801220056')
    ]
    flag = False

    # 用户校验
    for item in user_list:
        if item.username == user_info.username and item.password == user_info.password:
            flag = True

    if flag:
        print(f'欢迎你，{user_info.username}')
        print(user_info.password)
    else:
        print('用户名或密码错误')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
