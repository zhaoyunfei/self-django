# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

# Create your views here.


def index(request):
    return render(request, 'web/index.html')
# class IndexView(generic.ListView):
#     template_name = 'web/index.html'
#
#     def get_queryset(self):
#         return None
