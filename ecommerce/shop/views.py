from django.shortcuts import render,redirect
from shop.models import Category,Product

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)
def allproducts(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'product.html',context)
def alldetails(request,i):
    a=Product.objects.get(id=i)
    context={'product':a}
    return render(request, 'details.html',context)


def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==cp):
            user=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            user.save()
        else:
            return HttpResponse("passwords are not same")
        return redirect('shop:login')

    return render(request, 'register.html')


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            messages.error(request,"Invalid credentials")
    return render(request, 'login.html')


def user_logout(request):

    logout(request)
    return redirect('shop:categories')


def add_categories(request):
    if(request.method=="POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']

        b=Category.objects.create(name=n,image=i,desc=d)
        b.save()
        return redirect('shop:categories')
    return render(request,'add_categories.html')

def add_products(request):
    if(request.method=="POST"):
        pn=request.POST['pn']
        d=request.POST['d']
        p=request.POST['p']
        s=request.POST['s']
        cn=request.POST['cn']
        i=request.FILES['i']

        cat=Category.objects.get(name=cn)

        c=Product.objects.create(name=pn,desc=d,image=i,price=p,stock=s,category=cat)
        c.save()
        return redirect('shop:categories')
    return render(request,'add_products.html')


def addstock(request,p):
    product = Product.objects.get(id=p)
    if(request.method=="POST"):
        product.stock=request.POST['n']

        product.save()
        return redirect('shop:categories')
    context={'product':product}
    return render(request,'addstock.html',context)


