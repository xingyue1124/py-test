# 基础配置读取
import os
import configparser
import sys

# 主目录
base_path = os.getcwd()

path = sys.path[0]
# 测试运行配置
test_config_file = os.path.join(base_path, 'config', 'config.ini')
rc = configparser.ConfigParser()
rc.read(test_config_file, encoding='utf-8')

# 测试用例目录
test_case_path = os.path.join(base_path, 'data')
# 运行日志
test_log_file = os.path.join(base_path, 'log', 'run.log')
# 日志等级
log_level = rc.get('log', 'log_level')
