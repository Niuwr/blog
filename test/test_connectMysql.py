# -*- coding: utf-8 -*-

import asyncio

import orm

from configs import configs


async def connect_mysql(loop):
    #await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    await orm.create_pool(loop=loop, **configs['db'])

loop = asyncio.get_event_loop()
loop.run_until_complete(connect_mysql(loop))

def printDict(**kw):
    for k, v in kw.items():
        print('{}: {}\n'.format(k, v))


printDict(**configs['db'])
