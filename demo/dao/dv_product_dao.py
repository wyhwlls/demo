# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------------
# DB API SERVICE generate from hslab tools
#
# @auth: shs@163.com
# ------------------------------------------------------------------------------------

import traceback

from sqlalchemy.sql.functions import now

from demo.dao import BaseDao
from demo.model import DvProductDo
class DvProductDao(BaseDao):
    '''
    DvProductDao实体对象
    '''
    def __init__(self, db):
        super(DvProductDao, self).__init__(db)
    def _get_dv_product_by_params(self, **kwargs):
        """
        根据字典参数获取对象信息
        :param kwargs:
        :return:
        """
        query = self.db.query(DvProductDo)
        for key, val in kwargs.items():
            if hasattr(DvProductDo, key):
                query = query.filter(getattr(DvProductDo, key)==val)
        return query
    def _get_dv_product_by_id(self, entry_id):
        """
        根据id获取数据
        :param kwargs:
        :return:
        """
        pars = {'id':str(entry_id)}
        return self._get_dv_product_by_params(**pars).first()
    def _add_item_by_entry(self, entry):
        """
        根据id修改数据对象
        @TODO  此处有缺陷，可以增加别的对象。 这样数据权限可能有问题。
        """
        msg = '新增{}'
        try:
            entry.gmt_created = now()
            entry.deleted = 0
            self.db.add(entry)
            self.db.commit()
            return True, msg.format('成功'), entry
        except:
            self.db.rollback()
            self.log.error(traceback.format_exc())
            return False, msg.format('失败'),''
    def _add_item_by_params(self, **kwargs):
        """
        根据id修改数据对象
        """
        entry = DvProductDo()
        for k, v in kwargs.items():
            if hasattr(entry, k):
                setattr(entry, k, v)
        return self._add_item_by_entry(entry)
    def _update_dv_product_by_id(self, entry_id, **kwargs):
        """
        根据id 修改数据对象
        """
        entry = self._get_dv_product_by_id(entry_id)
        if not entry:
            return False, 'item i is not exit', ''

        kwargs.update({'gmt_modified': now()})
        for k, v in kwargs.items():
            if hasattr(entry, k):
                setattr(entry, k, v)

        msg = '修改{}'
        if kwargs.get('deleted') == 1:
            entry.deleted = 1
            msg = '删除{}'
        else:
            entry.deleted = 0
        try:
            self.db.commit()
            return True, msg.format('成功'), entry
        except:
            self.db.rollback()
            self.log.error(traceback.format_exc())
            return False, msg.format('失败'), ''
    def _delete_item_by_id(self, entry_id):
        """
        根据id 删除数据对象
        """
        self.log.error('will delete dv_product item %s' % entry_id)
        entry = self._get_dv_product_by_id(entry_id)
        if not entry:
            return False,'item i is not exit',''

        entry.deleted = 1
        msg = '删除{}'
        try:
            self.db.commit()
            return True, msg.format('成功'), ''
        except:
            self.db.rollback()
            self.log.error(traceback.format_exc())
            return False, msg.format('失败'), ''