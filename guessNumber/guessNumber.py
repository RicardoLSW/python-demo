import random


class GuessNumber:
    def __init__(self):
        self.result = None
        self.start = 1
        self.end = 100
        self.answer = random.randint(1, 100)

    def start_game(self):
        print('猜数字游戏开始')
        while self.result != self.answer:
            self.result = int(input(f'请输入{self.start}到{self.end}的数字：'))
            if self.result > self.answer:
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
