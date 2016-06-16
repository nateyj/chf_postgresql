# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466112628.559613
_enable_loop = True
_template_filename = 'C:/Data/chf_postgresql/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n    \r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    <header>\r\n      Welcome to the homepage app!\r\n    </header>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Colonial Heritage Foundation')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"66": 12, "36": 12, "37": 16, "38": 19, "39": 19, "40": 19, "45": 30, "46": 33, "47": 33, "48": 33, "17": 4, "19": 0, "78": 72, "54": 28, "72": 12, "60": 28, "30": 2, "31": 4}, "filename": "C:/Data/chf_postgresql/homepage/templates/base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
