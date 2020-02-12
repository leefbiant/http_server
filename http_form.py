#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import datetime

__all__ = [
    'HttpAliyunAudioGreenCallBack',
    ]

from datetime import date, timedelta, datetime
from wtforms import IntegerField, StringField, SelectField, FloatField
from wtforms.validators import DataRequired, Optional, NumberRange, InputRequired
from form import BaseForm 

__all__ = [
    'HttpAliyunAudioGreenCallBack'
    ]

class HttpAliyunAudioGreenCallBack(BaseForm):
  checksum = StringField(validators=[Optional()], default="")
  content = StringField(validators=[Optional()], default="")
