#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import time


def log(func):
    def logWrap(*args, **kw):
        print('call function %s' % func.__name__)
        func(*args, **kw)
    return logWrap


@log
def times(arg):
    print(arg)


times(time.time())
