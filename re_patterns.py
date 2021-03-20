# -*- coding: utf8 -*-
# Copyright (c) 2009, 2020, Oracle and/or its affiliates.
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

"""Cursor classes
"""

from collections import namedtuple
import re
import weakref

from . import errors
from .abstracts import MySQLCursorAbstract, NAMED_TUPLE_CACHE
from .catch23 import PY2
from .constants import ServerFlag

SQL_COMMENT = r"\/\*.*?\*\/"
RE_SQL_COMMENT = re.compile(
    r'''({0})|(["'`][^"'`]*?({0})[^"'`]*?["'`])'''.format(SQL_COMMENT),
    re.I | re.M | re.S)
RE_SQL_ON_DUPLICATE = re.compile(
    r'''\s*ON\s+DUPLICATE\s+KEY(?:[^"'`]*["'`][^"'`]*["'`])*[^"'`]*$''',
    re.I | re.M | re.S)
RE_SQL_INSERT_STMT = re.compile(
    r"({0}|\s)*INSERT({0}|\s)*INTO\s+[`'\"]?.+[`'\"]?(?:\.[`'\"]?.+[`'\"]?)"
    r"{{0,2}}\s+VALUES\s*\(.+(?:\s*,.+)*\)".format(SQL_COMMENT),
    re.I | re.M | re.S)
RE_SQL_INSERT_VALUES = re.compile(r'.*VALUES\s*(\(.*\)).*', re.I | re.M | re.S)
RE_PY_PARAM = re.compile(b'(%s)')
RE_PY_MAPPING_PARAM = re.compile(
    br'''
    %
    \((?P<mapping_key>[^)]+)\)
    (?P<conversion_type>[diouxXeEfFgGcrs%])
    ''',
    re.X
)
RE_SQL_SPLIT_STMTS = re.compile(
    b''';(?=(?:[^"'`]*["'`][^"'`]*["'`])*[^"'`]*$)''')
RE_SQL_FIND_PARAM = re.compile(
    b'''%s(?=(?:[^"'`]*["'`][^"'`]*["'`])*[^"'`]*$)''')

ERR_NO_RESULT_TO_FETCH = "No result set to fetch from"

MAX_RESULTS = 4294967295