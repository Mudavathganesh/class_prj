from django.shortcuts import render
from.models import *
from django.views.generic import CreateView,ListView,UpdateView
# Create your views here.
class Read(CreateView):
    modul=Product
    fields ='__all__'
    template_name='read.html'
    context_object_name = 'form'
