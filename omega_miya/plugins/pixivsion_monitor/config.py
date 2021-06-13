"""
@Author         : Ailitonia
@Date           : 2021/06/12 20:45
@FileName       : config.py
@Project        : nonebot2_miya 
@Description    : 
@GitHub         : https://github.com/Ailitonia
@Software       : PyCharm 
"""

from pydantic import BaseSettings


class Config(BaseSettings):
    # plugin custom config
    # 启用使用群组转发自定义消息节点的模式发送信息
    enable_node_custom: bool = True

    class Config:
        extra = "ignore"