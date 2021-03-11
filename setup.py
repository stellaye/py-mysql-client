#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009, 2017, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2.0, as
# published by the Free Software Foundation.
#
# This program is also distributed with certain software (including
# but not limited to OpenSSL) that is licensed under separate terms,
# as designated in a particular file or component or in included license
# documentation.  The authors of MySQL hereby grant you an
# additional permission to link the program and your derivative works
# with the separately licensed software that they have included with
# MySQL.
#
# Without limiting anything contained in the foregoing, this file,
# which is part of MySQL Connector/Python, is also subject to the
# Universal FOSS Exception, version 1.0, a copy of which can be found at
# http://oss.oracle.com/licenses/universal-foss-exception.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License, version 2.0, for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA

"""

To install MySQL Connector/Python:

    shell> python ./setup.py install

"""

from setuptools import setup



setup(
    name="py-mysql-client",
    version="0.0.0.1",
    description="基于mysql-python-connector库改写的python mysql driver",
    long_description="基于mysql-python-connector库改写的python mysql driver, 删除涉及cursor的逻辑,自动获取游标数据。支持设置debug模式，运行过程会打印与mysql server所互相传送的报文，可以作为mysql协议学习的一个小方式",
    author="lindaye",
    author_email="454784911@qq.com",
    url="https://github.com/stellaye",
    packages="easymysql",
)
