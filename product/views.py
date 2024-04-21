from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Testiminial, Product, Types, Bonus, Organic


class HomeListView(View):
    def get(self, request):
       products = Product.objects.all()
       type = Types.objects.all()
       bonuses = Bonus.objects.all()
       organics = Organic.objects.all()
       testiminials = Testiminial.objects.all()
       context = {
           'products' : products,
           'type' : type,
           'bonuses' : bonuses,
           'organics' : organics,
           'testiminials' : testiminials,
           
       }
       return render(request, 'main/index.html', context)