# _*_ coding: utf-8 _*_
# 开发团队：云飞国际
# 开发人员： 93792
# 开发时间： 2019/6/1 10:44
# 文件名称： adminx.py
# 开发工具： PyCharm

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "仙剑奇侠传"
    site_footer = "http://www.cnblogs.com/derek1184405959/"
    #菜单收缩
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)