import logging
'''日志管理类'''

def init_logger(logger_name):
    logger1 = logging.getLogger(logger_name)
    logger1.setLevel(logging.DEBUG)  # 设置最低级别
    return logger1


logger = init_logger('runtime-log')
