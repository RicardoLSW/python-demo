import random
import datetime


class GuessNumber:
    def __init__(self):
        self.result = None
        self.start = 1
        self.end = 100
        self.answer = None
        self.logPath = './guessNumberLog.txt'

    def start_game(self):
        """开始猜数字游戏"""
        print('猜数字游戏开始！')
        self.output_log('猜数字游戏开始！')
        self.answer = random.randint(self.start, self.end)
        while self.result != self.answer:
            try:
                self.result = int(input(f'请输入{self.start}到{self.end}的数字：'))
                self.output_log(f'请输入{self.start}到{self.end}的数字：{self.result}')
                if self.result < self.start or self.result > self.end:
                    print('您输入的数字超出范围，请再次尝试输入！')
                    self.output_log('您输入的数字超出范围，请再次尝试输入！')
                    continue
                elif self.result > self.answer:
                    self.end = self.result
                elif self.result < self.answer:
                    self.start = self.result
                else:
                    print(f'猜对了！答案是：{self.answer}')
                    self.output_log(f'猜对了！答案是：{self.answer}')
                    print('游戏结束！')
                    self.output_log('游戏结束！')
                    break
            except ValueError:
                print('您输入的不是数字，请再次尝试输入！')
                self.output_log("您输入的不是数字，请再次尝试输入！")
                continue
            except (KeyboardInterrupt, EOFError):
                break

    def output_log(self, log_message: str):
        """记录日志"""
        log_file = open(self.logPath, 'a+')
        log_file.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}：{log_message}\n')
        log_file.close()


if __name__ == '__main__':
    g = GuessNumber()
    g.start_game()
