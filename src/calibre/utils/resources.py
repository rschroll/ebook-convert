#!/usr/bin/env python


__license__   = 'GPL v3'
__copyright__ = '2009, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'


import builtins
from importlib.resources import files

from calibre import resources


def get_path(path, data=False, allow_user_override=True):
    fpath = files(resources) / path
    if data:
        with open(fpath, 'rb') as f:
            return f.read()
    return fpath


def get_image_path(path, data=False, allow_user_override=True):
    if not path:
        return get_path('images', allow_user_override=allow_user_override)
    return get_path('images/'+path, data=data, allow_user_override=allow_user_override)


builtins.__dict__['P'] = get_path
builtins.__dict__['I'] = get_image_path
