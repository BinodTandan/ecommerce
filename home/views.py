from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import *


class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.filter(status = 'active')
        self.views['sliders'] = Slider.objects.filter(status='active')
        self.views['brands'] = Brand.objects.filter(status='active')
        self.views['ads'] = Ad.objects.all()
        self.views['hots'] = Item.objects.filter(label = 'hot')
        self.views['news'] = Item.objects.filter(label = 'new')
        self.views['sales'] = Item.objects.filter(label='sale')
        self.views['defaults'] = Item.objects.filter(label='')
        return render(request,'index.html',self.views)


class ItemDetialView(BaseView):
    def get(self,request,slug):
        self.views['item_detial'] = Item.objects.filter(slug = slug)
        cat = Item.objects.get(slug = slug).category_id
        self.views['catitems'] = Item.objects.filter(category = cat)

        return render(request,'product-detial.html',self.views)