#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
from django.contrib import admin

from greetings.models import Greeting

admin.site.register(Greeting)
