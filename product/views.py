from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Testiminial, Product, Types, Bonus, Organic
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


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
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password"]
        psw_repeat = request.POST["psw_repeat"]
        if password_1 == psw_repeat:
            user_check = User.objects.filter(username=username, password=password_1)
            if user_check:
                return render(request, "main/index.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password_1)
                user.save()
                return redirect("login")
        else:
            return render(request, "auth/register.html")
