# 第一种方式是使用logging提供的模块级别的函数

# import time,logging
#
# format = "时间：%(asctime)s  日志器名称：%(name)s  文件：%(filename)s  " \
#          "函数：%(funcName)s  行号：%(lineno)d  等级：%(levelname)s  日志信息：%(message)s"
# logging.basicConfig(format=format,
#                     datefmt="%Y/%m/%d %H:%M:%S",
#                     level=logging.DEBUG,
#                     filename='{}_log.txt'.format(time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())))
# # 定义一个函数，同时捕获异常，获取错误日志
# def sum(a, b):
#     try:
#         sum = a + b
#     except Exception as error:
#         logging.debug(error)
# sum('a',1)

# import logging
# # 设置日志显示格式
# format = "%(asctime)s  %(name)s  %(levelname)s  %(message)s"
#                     # 格式为上述设置的日志显示格式
# logging.basicConfig(format=format,
#                     # 定义日志输出的时间格式
#                     datefmt="%Y/%m/%d %H:%M:%S",
#                     # 定义日志级别
#                     level=logging.DEBUG)
# # 错误日志信息
# logging.debug("debug级别错误信息")



# 第二种方式是使用Logging日志系统的四大组件

import time,logging
# 创建日志对象（获取日志器，命名为logger）
logger=logging.getLogger("logger")
#日志输出的最低级别（忽略当前最低级别以下级别的日志信息）
logger.setLevel(logging.ERROR)  # 级别需要大写
# 创建控制台处理器
sh=logging.StreamHandler()
# 创建文件处理器
fh=logging.FileHandler(filename="{}_log2.txt".format(time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime()))
                       ,encoding="utf-8")
# 把控制台处理器添加到日志器中
logger.addHandler(sh)
# 指定格式器显示的格式
formatter=logging.Formatter(fmt="时间：%(asctime)s  日志器名称：%(name)s  文件：%(filename)s  " \
                                "函数：%(funcName)s  行号：%(lineno)d  等级：%(levelname)s  日志信息：%(message)s",
                            datefmt="%Y/%m/%d %H:%M:%S")
# 控制台处理器指定格式
sh.setFormatter(formatter)
# 添加文件处理器到日志器
logger.addHandler(fh)
# 文件处理器设置格式
fh.setFormatter(formatter)
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误信息")
