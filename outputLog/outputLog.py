class OutputLog:
    def __init__(self, log_file_path, mode, message):
        self.log_file_path = log_file_path
        self.mode = mode
        self.message = message
        self.write_log()

    def write_log(self):
        """记录日志"""
        log_file = open(self.log_file_path, self.mode)
        log_file.write(self.message)
        log_file.close()


if __name__ == '__main__':
    o = OutputLog('test', 'a+', 'testLog')
