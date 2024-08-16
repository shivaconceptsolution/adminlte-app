from django.shortcuts import render,redirect
from .models import Category,AdminLogin
def adminlogin(request):
    if request.method=="POST":
        res = AdminLogin.objects.filter(username=request.POST.get('txtuser'),password=request.POST.get('txtpass'))
        if(res.count()>0):
            request.session['key'] =request.POST.get('txtuser')
            return redirect('/adminlte/index')
        else:
            return render(request,"adminlte/adminlogin.html",{"key":" Invalid Userid and Password"})

    return render(request,"adminlte/adminlogin.html")
def index(request):
  if(request.session.has_key('key')):
    return render(request,"adminlte/index.html",{"key":request.session['key']})
  else:
    return redirect('/adminlte/adminlogin')
def category(request):
  if(request.session.has_key('key')):
    if request.method=="POST":
        obj = Category(catname=request.POST.get("catname"))
        obj.save()
        return render(request,"adminlte/category.html",{"key":"data inserted successfully"})

    return render(request,"adminlte/category.html")
  else:
      return redirect('/adminlte/adminlogin')
def viewcategory(request):
   if(request.session.has_key('key')):  
    res = Category.objects.all()
    return render(request,"adminlte/viewcategory.html",{"data":res})
   else:
     return redirect('/adminlte/adminlogin')
def editcategory(request):
     if request.method=="POST":
        data = Category.objects.get(pk=request.POST.get("txtid"))
        data.catname = request.POST.get("txtcat")
        data.save()
        return redirect('/adminlte/viewcategory')
     res = Category.objects.get(pk=request.GET.get("q"))
     return render(request,"adminlte/editcategory.html",{"data":res})

'''def deletecategory(request):
     res = Category.objects.get(pk=request.GET.get("q"))
     res.delete()
     return redirect('/adminlte/viewcategory')'''

def deletecategory(request):
     res = Category.objects.get(pk=request.GET.get("q"))
     if request.method=="POST":
        res.delete()
        return redirect('/adminlte/viewcategory')
     
     return render(request,"adminlte/deletecategory.html",{"data":res})

def logout(request):
    del request.session['key']
    return redirect('/adminlte/adminlogin')