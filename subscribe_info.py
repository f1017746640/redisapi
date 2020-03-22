#!/usr/bin/env python
# encoding: utf-8
"""
   > FileName: subscribe_info.py
   > Author: FZH
   > Mail: fengzhihai@ilarge.cn
   > CreatedTime: 2020-03-22 17:07
"""
import time
import configparser

from rds import RedisHelper


config = configparser.ConfigParser()
config_file = "config.ini"
config.read(config_file)
sec = config["DEV"]

redis_host = sec["redis_host"]
redis_port = sec["redis_port"]
redis_db = sec["redis_db"]
redis_channel = sec["redis_channel"]
redis_password = sec["redis_password"]
if len(redis_password) == 0:
    redis_password = None


def sub_info():
    obj = RedisHelper(host=redis_host,
                      port=redis_port,
                      db=redis_db,
                      channel=redis_channel,
                      password=redis_password)
    sub_obj = obj.subscribe()
    while True:
        if sub_obj:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(time.time()))
            msg = sub_obj.parse_response()
            print('receive:', now_time, msg)
        else:
            break


if __name__ == '__main__':
    sub_info()
