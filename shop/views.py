from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
     C_page=None
     prodct_list=None
     if c_slug!=None:
          C_page=get_object_or_404(category,slug=c_slug)
          prodct_list=products.objects.filter(category_id= C_page, available=True)
          print(c_slug,C_page)
          print('##########################')
     else:
          prodct_list=products.objects.all().filter(available=True)
          paginator=Paginator(prodct_list,6)
          try:
               page=int(request.GET.get('page',1))
          except:
               page=1
          try:
               prod=paginator.page(page)
          except:
               prod=paginator.page(paginator.num_pages)
               
     # p_category=category.objects.all()
     return render(request,'home.html',{'shopProduct':prod,'showCategory':C_page})
# 'showCategory':p_category


def prodDetails(request,c_slug,p_slug):
     try:
          prod=products.objects.get(category__slug=c_slug,slug=p_slug)
     except Exception as e:
          raise e
     return render(request,'products.html',{'pr':prod})

def searching(request):
     prod=None
     query=None
     if 'q' in request.GET:
          query=request.GET.get('q')
          prod=products.objects.all().filter(Q(name__contains=query)|Q(description__contain=query))
          
     return render(request,'search.html',{'qr':query,'pr':prod})