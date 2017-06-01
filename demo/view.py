# -*- coding:utf-8 -*-
import logging
from flask import Blueprint, request, session
from service.dv_product_service import DvProductService
from setting import SQLALCHEMY_DATABASE_URI

log = logging.getLogger(__file__)

banner_api = Blueprint('banner', __name__, url_prefix="/")


@banner_api.route("/login/")
def login():
    """
    用户注册/登录
    :return:
    """
    productser = DvProductService(SQLALCHEMY_DATABASE_URI)
    productser.get_dv_product_by_id(1)
    return '1111111111111111'