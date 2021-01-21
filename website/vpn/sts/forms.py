# -*- coding: utf-8 -*-
"""
    website.vpn.sts.forms
    ~~~~~~~~~~~~~~~~~~~~~

    vpn forms:
        /vpn/sts/add
        /vpn/sts/<int:id>/settings

    :copyright: (c) 2014 by xiong.xiaox(xiong.xiaox@alibaba-inc.com).
"""


from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, IPAddress


class AddForm(Form):
    tunnel_name = StringField(u'隧道ID',
                              validators=[DataRequired(message=u'这是一个必选项！'),
                                          Length(max=20, message=u'帐号最长为20个字符！')])
    start_type = SelectField(u'启动类型',
                             choices=[('add', u'手工连接'), ('start', u'服务启动自动连接')])
    local_subnet = TextAreaField(u'本端子网',
                                  validators=[DataRequired(message=u'这是一个必选项！')])
    remote_ip = StringField(u'对端EIP',
                            validators=[DataRequired(message=u'这是一个必选项！'),
                                        IPAddress(message=u'无效的ip 地址！')])
    remote_subnet = TextAreaField(u'对端子网',
                                  validators=[DataRequired(message=u'这是一个必选项！')])
    psk = StringField(u'预共享秘钥',
                      validators=[DataRequired(message=u'这是一个必选项！')])
    #: submit button
    save = SubmitField(u'保存')
    delete = SubmitField(u'删除')


class ConsoleForm(Form):
    '''web console form'''
    #: submit button
    stop = SubmitField(u'关闭')
    start = SubmitField(u'启动')
    re_load = SubmitField(u'下发&重载')


class UpDownForm(Form):
    """for tunnel up and down."""
    tunnel_name = StringField(u'隧道名称')
    #: submit button
    up = SubmitField(u'连接')
    down = SubmitField(u'断开')
