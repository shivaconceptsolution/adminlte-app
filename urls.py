from django.urls import path
from . import views
urlpatterns=[
    path('',views.adminlogin,name='adminlogin'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('index',views.index,name='index'),
    path('category',views.category,name='category'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('editcategory',views.editcategory,name='editcategory'),
    path('deletecategory',views.deletecategory,name='deletecategory'),
    path('logout',views.logout,name='logout')
]