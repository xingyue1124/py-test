import logging


# 创建一个Logger类
class Logger:
    def get_logger(self):
        # 创建日志对象（获取日志器，命名为logger）
        logger = logging.getLogger('logger')
        # 定义日志输出的最低级别
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # 创建控制台处理器
            sh = logging.StreamHandler()
            # 指定显示的格式（文件：时间-等级-日志信息）
            formatter = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')
            # 控制台处理器指定格式
            sh.setFormatter(formatter)
            # 添加文件处理器到日志器
            logger.addHandler(sh)
        return logger
