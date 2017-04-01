# -*- coding: utf-8 -*-

######################################################################################
#  参数说明：
#  base_url   待测系统的登录地址
#  web_types  兼容性测试的浏览器类型，目前支持firefox、chrome，IE兼容性有问题需要单独脚本
######################################################################################
test_parameters = {'education_base_url': 'http://172.18.215.121/auth/login?next=%2F',
                   'bussiness_base_url': 'http://172.18.215.122/auth/login?next=%2F',
                   'web_types': ['firefox'],
                   # login
                   'admin_username': 'admin',
                   'admin_password': 'admin123',
                   # image management
                   'image_instance_imagename': "win7_64",
                   'image_instance_flavorname': "2VCPU|3072MB|60GB",
                   'image_instance_netname': '内部网络'
                   }