# -*- coding: utf-8 -*-
from ..allpage import tools
pages = tools.parseryaml()
def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:

            return locator


class homePage:
    首页协议弹框 = get_locater('homePage', '首页协议弹框')
    发现 = get_locater('homePage', '发现')


    

class LoginPage:
    本机号码一键登录 = get_locater('LoginPage', '本机号码一键登录')
    其他号码登录 = get_locater('LoginPage', '其他号码登录')
    微信 = get_locater('LoginPage', '微信')
    QQ = get_locater('LoginPage', 'QQ')
    微博 = get_locater('LoginPage', '微博')
    手机密码登录 = get_locater('LoginPage', '手机密码登录')
    请输入手机号码 = get_locater('LoginPage', '请输入手机号码')
    请输入密码 = get_locater('LoginPage', '请输入密码')
    同意协议并登录 = get_locater('LoginPage', '同意协议并登录')
    登录遇到问题 = get_locater('LoginPage', '登录遇到问题')


    

class SetPage:
    我 = get_locater('SetPage', '我')
    设置按钮 = get_locater('SetPage', '设置按钮')
    登出账户 = get_locater('SetPage', '登出账户')
    确定 = get_locater('SetPage', '确定')


    