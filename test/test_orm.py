# -*- coding: utf-8 -*-

import asyncio

from sys import path

path.append('F:\\awsome-python3-webapp\\www')

import orm

from models import User, Blog

from configs import configs

from coroweb import get, post

@get(' ')
def test(loop):
    yield from orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='123456', db='awesome')
    num = yield from Blog.findNumber('count(id)')
    print('num:{}'.format(num))
    return num
    #u = User(name='Test', email='Test@exmaple.com', password='1234', image='about:blank')
    #yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
