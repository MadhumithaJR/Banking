from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path('index', views.index, ),
    path('makeTransaction', views.makeTransaction, ),
    path('displayTrans', views.displayTransaction, ),
    path('displayCust', views.displayCustomer, ),
)
