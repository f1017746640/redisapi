#!/usr/bin/env python
# encoding: utf-8
"""
   > FileName: rds.py
   > Author: FZH
   > Mail: fengzhihai@ilarge.cn
   > CreatedTime: 2020-03-22 16:49
"""
import redis


class RedisHelper(object):
    """
    host: redis ip
    port: redis port
    channel: 发送接送消息的频道
    """
    def __init__(self,
                 host,
                 port,
                 db,
                 channel,
                 password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.channel = channel
        self.__conn = redis.Redis(self.host,
                                  self.port,
                                  self.db,
                                  self.password,
                                  decode_responses=True)

    def ping(self):
        try:
            self.__conn.ping()
            return True
        except Exception as e:
            print(e)
            return False

    # 发送消息
    def public(self,
               msg):
        if self.ping():
            self.__conn.publish(self.channel,
                                msg)
            return True
        else:
            return False

    # 订阅
    def subscribe(self):
        if self.ping():
            # 打开收音机
            pub = self.__conn.pubsub()
            # 调频道
            pub.subscribe(self.channel)
            # 准备接收
            pub.parse_response()
            return pub
        else:
            return False
