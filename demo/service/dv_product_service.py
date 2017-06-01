# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------------
# DB API SERVICE generate from hslab tools
#
# @auth:shs@163.com
# ------------------------------------------------------------------------------------

from demo.dao.dv_product_dao import DvProductDao
from demo.service import BaseService


class DvProductService(BaseService):
    '''
    DvProductService实体对象
    '''
    def __init__(self, db):
        self.db = db
        self.dv_product_dao = DvProductDao(db)
    def get_dv_product_by_id(self, entry_id):
        """
        根据id获取数据
        :param kwargs:
        :return:
        """
        return self.dv_product_dao._get_dv_product_by_id(entry_id=entry_id)
    def get_dv_product_first(self, **kwargs):
        """
        根据参数获取一条数据
        :param kwargs:
        :return:
        """
        return self.dv_product_dao._get_dv_product_by_params(**kwargs).first()
    def get_dv_product_list(self, **kwargs):
        """
        根据参数获取数据列表
        :param kwargs:
        :return:
        """
        return self.dv_product_dao._get_dv_product_by_params(**kwargs).all()
    def add_dv_product(self, **kwargs):
        """
        添加数据
        :param kwargs:
        :return:
        """
        return self.dv_product_dao._add_item_by_params(**kwargs)
    def delete_dv_product_by_id(self, id):
        """
        根据id 删除数据对象
        """
        return self.dv_product_dao._delete_item_by_id(id)
    def update_dv_product_by_id(self, id, **kwargs):
        """
        根据id 修改数据对象
        :param kwargs:
        :return:
        """
        return self.dv_product_dao._update_dv_product_by_id(id,**kwargs)