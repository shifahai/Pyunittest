"""
====================
Author:释法海
Time：2022/5/6 17:35
Porject：PYunittest
Address:shanghai
====================
"""
import logging
import os
from Common.handle_confing import conf
from Common.handle_path import logs_dir

class MyLogger(logging.Logger):

    def __init__(self,file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(conf.get("log","name"),conf.get("log","level"))

        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line: %(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

# 是否需要写入文件
if conf.getboolean("log","file_ok"):
    file_name = os.path.join(logs_dir,conf.get("log","file_name"))
else:
    file_name = None

logger = MyLogger(file_name)


# logging.info("1111111111111")
