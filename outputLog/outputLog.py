class OutputLog:
    def __init__(self, log_file_name, mode, message):
        self.log_file_name = log_file_name
        self.mode = mode
        self.message = message
        self.write_log()

    def write_log(self):
        """记录日志"""
        log_file = open(f'./{self.log_file_name}.txt', self.mode)
        log_file.write(f'{self.message}\n')
        log_file.close()


if __name__ == '__main__':
    o = OutputLog('test', 'a+', 'testLog')
