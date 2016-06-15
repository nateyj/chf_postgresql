# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466012407.534062
_enable_loop = True
_template_filename = 'C:/Data/chf_postgresql/homepage/styles/index.cssm'
_template_uri = 'index.cssm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        timecolor = context.get('timecolor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('.server-time {\r\n\tfont-size: 2em;\r\n\tcolor: ')
        __M_writer(str( timecolor ))
        __M_writer(';\r\n}')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"24": 3, "17": 0, "31": 25, "25": 3, "23": 1}, "source_encoding": "utf-8", "uri": "index.cssm", "filename": "C:/Data/chf_postgresql/homepage/styles/index.cssm"}
__M_END_METADATA
"""
