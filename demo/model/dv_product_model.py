# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------------
# DB API SERVICE generate from hslab tools
#
# @auth:shs@163.com
# ------------------------------------------------------------------------------------

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.sql.functions import now

from demo.model import Base


class DvProductDo(Base):
    """
    DAO class
    """
    __tablename__ = 'dv_product'
    id = Column(Integer,  primary_key=True,   nullable = False,   doc='')
    name = Column(String(128),   nullable = False,   doc='商品名称')
    long_name = Column(String(256),   nullable = False,   doc=' 商品长名称')
    market_price = Column(Float,   nullable = False,   default = 0,  doc='市场价')
    sell_price = Column(Float,   nullable = False,   default = 0,  doc='销售价')
    is_online = Column(Boolean,    default = 0,  doc='是否上架状态 0:未上架')
    cost_price = Column(Float,    default = 0,  doc='成本价')
    gmt_created = Column(DateTime,   default=now(), doc='')
    gmt_modified = Column(DateTime,   default=now(), doc='')
    deleted = Column(Boolean,    default = 0,  doc='')
    sort = Column(Integer,    default = 99,  doc='排序')
    shelf_life = Column(Integer,   nullable = False,   default = 180,  doc='保质期')
    pre_shelf_life = Column(Integer,    default = 160,  doc='预估保质期')
    product_img1 = Column(String(256),   nullable = False,   doc='商品图片1')
    product_img2 = Column(String(256),    doc='商品图片2')
    product_img3 = Column(String(256),    doc='商品图片3')
    product_img4 = Column(String(256),    doc='商品图片4')
    unit = Column(String(32),   nullable = False,   doc='单位')
    country = Column(String(128),    doc='商品所在国家')