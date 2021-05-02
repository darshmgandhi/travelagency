from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BookingView.as_view(), name = 'create'),
    path('view/', views.BookingList.as_view(), name = 'view'),
    path('update/<int:id>/', views.UpdateBooking.as_view(), name = 'update'),
    path('delete/<int:id>/', views.DeleteBooking.as_view(), name = 'delete'),
    path('', views.HomePage.as_view(), name = 'home'),
]