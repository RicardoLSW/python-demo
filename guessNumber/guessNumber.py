import random


class GuessNumber:
    def __init__(self):
        self.result = None
        self.start = 1
        self.end = 100
        self.answer = None

    def start_game(self):
        print('猜数字游戏开始')
        self.answer = random.randint(1, 100)
        while self.result != self.answer:
            try:
                self.result = int(input(f'请输入{self.start}到{self.end}的数字：'))
            except ValueError:
                print("您输入的不是数字，请再次尝试输入！")
                continue

            if self.result < self.start or self.result > self.end:
                print("您输入的数字超出范围，请再次尝试输入！")
                continue
            elif self.result > self.answer:
                self.end = self.result
            elif self.result < self.answer:
                self.start = self.result
            else:
                print('猜对了！')
                print('游戏结束')
                break


if __name__ == '__main__':
    g = GuessNumber()
    g.start_game()
