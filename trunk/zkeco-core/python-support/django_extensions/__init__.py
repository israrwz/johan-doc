#coding=utf-8
'''
一些全局的 management extensions。其中包括create_app等的增强工具命令
参考：https://github.com/jezdez/django-extensions
'''
VERSION = (0, "4.2", "pre")

# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]

__version__ = str_version
