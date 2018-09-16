# -*- coding: utf-8 -*-

import asyncio

from sys import path

path.append('F:\\awsome-python3-webapp\\www')

from models import Blog, User

@asyncio
def getNum():
    num = yield from User.findNumber('count(id)')
    return num


if __name__ == '__main__':
    getNum()
