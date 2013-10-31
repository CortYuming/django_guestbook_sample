#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Paginate(object):
    def __init__(self, request, queryset, per_page_num):
        self.paginator = Paginator(queryset, per_page_num)
        self.page = request.GET.get('page')

    def get_paginator(self):
        page_objects = None
        try:
            page_objects = self.paginator.page(self.page)
        except PageNotAnInteger:
            page_objects = self.paginator.page(1)
        except EmptyPage:
            page_objects = self.paginator.paginator(self.paginator.num_pages)
        return page_objects
