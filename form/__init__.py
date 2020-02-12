#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

__all__ = ['BaseForm', 'flatten_form', 'form_dict']

from datetime import date, datetime
from decimal import Decimal
from pprint import pformat
from flask_wtf import FlaskForm
from flask import request
from werkzeug.datastructures import ImmutableMultiDict


class BaseForm(FlaskForm):
    class Meta:
        csrf = False

    def __str__(self):
        data = {}
        for field in self:
            if type(field.data) is Decimal:
                data[field.name] = float(field.data)
            elif type(field.data) is date:
                data[field.name] = field.data.strftime('%Y-%m-%d')
            elif type(field.data) is datetime:
                data[field.name] = field.data.strftime('%Y-%m-%d %H:%M:%S')
            else:
                data[field.name] = field.data
        return pformat(data)

    def __unicode__(self):
        return self.__str__()
    


def flatten_form(formdata):
    def prefix_key(prefix, key, val):
        data = []
        key = str(key).replace('[', '-').replace(']', '')
        key = (prefix + '-' + key) if prefix else key

        if type(val) == list:
            for k, v in enumerate(val):
                data = data + prefix_key(key, str(k), v)
        elif type(val) == dict:
            for k, v in val.items():
                data = data + prefix_key(key, k, v)
        else:
            data.append((key, val))

        return data

    items = []
    for key, val in formdata.items():
        items = items + prefix_key('', key, val)

    print("flatten_form items:", items);
    return ImmutableMultiDict(items)


def form_dict(merge_query=False, flatten=False, *args, **kwargs):
    items = []
    if merge_query or request.method == 'GET':
        items += request.args.items()

    if request.method != 'GET':
        if request.is_json:
            items += [i for i in request.json.items() if i[1] is not None]
        else:
            items += request.form.items()

    k = dict(request.values)
    print("kyes:%s" % (k))     

    items += kwargs.items()
    for k, v in items:
      print("k:%s v:%s" % (k, v));
    print("form_dict items:", items);
    return flatten_form(dict(items)) if flatten else ImmutableMultiDict(items)
