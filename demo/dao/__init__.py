# -*- coding:utf-8 -*-

import logging
class BaseDao(object):
    def __init__(self, db):
        self.db = db
        # self.rdb = db
        self.log = logging.getLogger(__file__)