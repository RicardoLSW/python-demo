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
