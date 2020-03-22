#!/usr/bin/env python
# encoding: utf-8
"""
   > FileName: public_info.py
   > Author: FZH
   > Mail: fengzhihai@ilarge.cn
   > CreatedTime: 2020-03-22 17:06
"""
import json
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


def pub_info(app_name,
             app_version,
             app_owner,
             app_desc,
             deploy_res):
    info = {
        "app_name": app_name,
        "app_version": app_version,
        "app_owner": app_owner,
        "app_desc": app_desc,
        "deploy_res": deploy_res
    }
    obj = RedisHelper(host=redis_host,
                      port=redis_port,
                      db=redis_db,
                      channel=redis_channel,
                      password=redis_password)
    res = obj.public(msg=json.dumps(info))
    if res:
        print('public successful.')
    else:
        print('public fail.')


if __name__ == '__main__':
    app_name = 'inf-demo2'
    app_version = '3.10'
    app_owner = 'fengzhihai'
    app_desc = 'inf group demo2 application'
    deploy_res = 'FAIL'
    pub_info(app_name=app_name,
             app_version=app_version,
             app_owner=app_owner,
             app_desc=app_desc,
             deploy_res=deploy_res)



