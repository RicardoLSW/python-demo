# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from sys import path


class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print('path:', path)

    id_card = 801220056
    print(bin(id_card))

    # 字符串顺序、反序输出
    str1 = 'Python'
    print(str1[:])
    print(len(str1))
    print(str1[::-1])
    print(str1.lower())
    print(str1.upper())
    print(str1.split('h'))

    # 输入函数、条件判断
    # username = input('请输入你的名字：')
    # password = input('请输入密码：')
    # check_user(username, password)


def check_user(username, password):
    # 用户列表
    user_dic = {
        'admin': 'admin',
        'ricardo': '801220056'
    }

    # 用户校验
    if username in user_dic and password == user_dic[username]:
        print(f'欢迎你，{username}')
        print(password)
    else:
        print('用户名或密码错误')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_list = ['猜数字游戏', '爬虫']
    for item in menu_list:
        print(f'{menu_list.index(item)}：{item}')
    index = input('请选择菜单：')
    if index == '0':
        from guessNumber import guessNumber
        guessNumber.GuessNumber().start_game()
    elif index == '1':
        from crawler import crawler
        crawler.Crawler('http://www.4399.com/',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/85.0.4183.102 Safari/537.36').get_html()
    else:
        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
