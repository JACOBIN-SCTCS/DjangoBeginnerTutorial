# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import student

# Create your views here.


def get_list(request):
    stu_list=student.objects.all()
    return render(request,'dbsample/index.html',{ 'list' : stu_list })

    
    
