from django.contrib import admin
from django.urls import path,include
from Api import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'companies',CompanyViewSet),

urlpatterns=[
    #path('index/',views.index,name="index"),
    path("",views.ListProductApiView.as_view(),name="Product list"),
    path("create/",views.CreateProductApiView.as_view(),name="Product list"),
    path("update/<int:pk>",views.UpdateProductApiView.as_view(),name="Product list"),
    path("delete/<int:pk>",views.DeleteProductApiView.as_view(),name="Product list"),
    ]