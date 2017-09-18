# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article
from .models import Category

# Create your views here.


# class IndexView(generic.ListView):
#     template_name = 'web/index.html'
#     context_object_name = 'context'
#
#     def get_queryset(self):
#         context = {
#             'list_category': Category.objects.order_by('order_number'),
#             'list_article': Article.objects.order_by('-public_date')
#         }
#         return context

def index(request):
    list_article = Article.objects.order_by('-public_date')
    list_category = Category.objects.order_by('order_number')
    context = {
        'list_article': list_article,
        'list_category': list_category
    }
    return render(request, 'web/index.html', context)
