import logging
import time


class Logger():
    def __init__(self):
        #创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        filename = time.strftime('%Y-%m-%d', time.localtime())

        # 创建handler，写入日志文件,文件路径最好写绝对路径
        ch = logging.FileHandler(r'D:\api_guest\log\%s.log' % filename)
        ch.setLevel(logging.INFO)

        # 创建handler，输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')

        # 定义handler的输出格式
        sh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(ch)
        self.logger.addHandler(sh)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    logger = Logger().getlog()
    logger.info('wow')
