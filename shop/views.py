from django.shortcuts import render
from django.views import View
from product.models import Types, Product, Bonus, Organic, Testiminial



class ShopListView(View):
    def get(self, request):
        types = Types.objects.all()
        products = Product.objects.all()
        bonuses = Bonus.objects.all()
        organics = Organic.objects.all()
        testiminials = Testiminial.objects.all()
        context = {
            'types' : types,
            'products' : products,
            'bonuses' : bonuses,
            'organics' : organics,
            'testiminials' : testiminials,
        }

        return render(request, 'main/shop.html', context)
    
class ShopDetailOrg(View):
    def get(self, request, id):
        types = Types.objects.all()
        products = Product.objects.all()
        bonuses = Bonus.objects.all()
        organics = Organic.objects.get(id = id)
        return render(request, 'main/shop-detail_org.html', {'organics' : organics, 'products' : products,'types':types,'bonuses':bonuses,})
    


class ShopDetailView(View):
    def get(self, request, id):
        types = Types.objects.all()
        products = Product.objects.get(id = id)
        bonuses = Bonus.objects.all()
        organics = Organic.objects.all()
        
        return render(request, 'main/shop-detail.html', {'products': products, 'organics' : organics, 'types':types,'bonuses' : bonuses,})
    

class CartListView(View):
    def get(self, request):
        types = Types.objects.all()
        products = Product.objects.all()
        bonuses = Bonus.objects.all()
        organics = Organic.objects.all()
        testiminials = Testiminial.objects.all()
        context = {
            'types' : types,
            'products' : products,
            'bonuses' : bonuses,
            'organics' : organics,
            'testiminials' : testiminials,
        }

        return render(request, 'main/pages/cart.html', context)
    
class ChackOutView(View):
    def get(self, request):
        types = Types.objects.all()
        products = Product.objects.all()
        bonuses = Bonus.objects.all()
        organics = Organic.objects.all()
        testiminials = Testiminial.objects.all()
        context = {
            'types' : types,
            'products' : products,
            'bonuses' : bonuses,
            'organics' : organics,
            'testiminials' : testiminials,
        }

        return render(request, 'main/pages/chackout.html', context)
    

class TestiminialView(View):
    def get(self, request):
        testiminial = Testiminial.objects.all()
        context = {
            'testiminial' : testiminial,

        }
        return render(request, 'main/pages/testimonial.html', context)

    
