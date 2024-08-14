from django.shortcuts import render,redirect
from .models import Category
def index(request):
    return render(request,"adminlte/index.html")
def category(request):
    if request.method=="POST":
        obj = Category(catname=request.POST.get("catname"))
        obj.save()
        return render(request,"adminlte/category.html",{"key":"data inserted successfully"})

    return render(request,"adminlte/category.html")
def viewcategory(request):
    res = Category.objects.all()
    return render(request,"adminlte/viewcategory.html",{"data":res})
def editcategory(request):
     if request.method=="POST":
        data = Category.objects.get(pk=request.POST.get("txtid"))
        data.catname = request.POST.get("txtcat")
        data.save()
        return redirect('/adminlte/viewcategory')
     res = Category.objects.get(pk=request.GET.get("q"))
     return render(request,"adminlte/editcategory.html",{"data":res})

def deletecategory(request):
    pass