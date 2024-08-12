from django.shortcuts import render

def index(request):
    return render(request,"adminlte/index.html")
def category(request):
    return render(request,"adminlte/category.html")