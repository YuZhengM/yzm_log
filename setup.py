# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# 读取 README.md 文件的内容
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    # 库的名称
    name='ykenan_log',

    # 版本, 每次发版本都不能重复, 每次发版必须改这个地方
    version="1.0.0",
    description=(
        # 一个简介, 别人搜索包时候, 这个概要信息会显示在在搜索列表中
        'Simple log printing'
    ),
    # 这是详细的, 一般是交别人怎么用, 很多包没写, 那么在官网就造成没有使用介绍了
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    author='Yu Zhengmin',  # 作者
    author_email='3236170161@qq.com',
    maintainer='yzm',  # 主要的工作人员
    maintainer_email='3236170161@qq.com',
    license='BSD License',
    # packages=['douban'], # 发布的包名
    packages=find_packages(),
    platforms=["all"],
    # 这个是连接, 一般写 github 就可以了, 会从 pypi 跳转到这里去
    url='https://github.com/YuZhengM/ykenan_log',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.+',
        'Topic :: Software Development :: Libraries'
    ],
    # 这里是依赖列表, 表示运行这个包的运行某些功能还需要你安装其他的包
    install_requires=[
        'coloredlogs',
    ]
)
