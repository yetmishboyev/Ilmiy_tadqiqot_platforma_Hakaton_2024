from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from django.views import View
from serpapi import GoogleSearch
from django.contrib.auth.models import User
from .models import *


class LoginView(View):
    def get(self,request):
        return render(request,'loginadmin.html')
    def post(self,request):
        loginn=request.POST.get('login')
        paroll=request.POST.get('parol')
        user=authenticate(request,password=paroll,username=loginn)
        if user is not None:
            login(request, user)
            return redirect('/qidirish')

        return redirect('/register')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        name=request.POST.get('ism')
        fam=request.POST.get('fam')
        loginn=request.POST.get('login')
        pp=request.POST.get('parol')
        tp=request.POST.get('takparol')
        jins=request.POST.get('jins')
        tel=request.POST.get('tel')
        if pp == tp:
            user1=User.objects.create_user(username=loginn,password=tp)
            Profil.objects.create(
                ism=name,
                fam=fam,
                jins=jins,
                tel=tel,
                user=user1
            )
            return redirect('/login')


class Sayt(View):
    def get(self,request):
        return render(request,'index.html')
class Dashboard(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'data':Profil.objects.get(user=request.user),
                'dostlar':Profil.objects.all(),
                'ishlar':Maqola.objects.filter(user_fk__user=request.user)
            }
            return render(request,'dashboard.html',data)
        return redirect('/')
class Qidiruv(View):
    def get(self,request):

        return render(request,'maqola_2.html')
    def post(self,request):
        search_query = request.POST.get('kirit')

        params = {
            "engine": "google_scholar",
            "q": search_query,
            "api_key": "8eda2b27aec15412b506a0563dae2be42b23cb3043e22c2a9f632d78ac4eaf5f"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results["organic_results"]
        data={
            'data':organic_results
        }
        return render(request,'maqola_2.html',data)

class Forms(View):
    def get(self,request):
        if request.user.is_authenticated:
            data = {
                'data': Profil.objects.get(user=request.user)
            }
            return render(request,'pages/forms/basic_elements.html',data)
        return redirect('/')
    def post(self,request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                nom=request.POST.get('nom'),
                Anotatsiya=request.POST.get('anotatsiya'),
                kalit=request.POST.get('soz'),
                adabiyot=request.POST.get('adabiyot'),
                fayl=request.POST.get('fayl'),
                user_fk=Profil.objects.get(user=request.user)
            )
            return redirect('/form')
        return redirect('/')

class Wikipediya(View):
    def get(self,request):
        if request.user.is_authenticated:

            return render(request,'wikipedia.html')
        return redirect('/')

class Translete(View):
    def get(self,request):
        if request.user.is_authenticated:

            return render(request,'Translator.html')
        return redirect('/')


# class Charts(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             data = {
#                 'data': Profil.objects.get(user=request.user)
#             }
#             return render(request,'pages/charts/chartjs.html')
#         return redirect('/')