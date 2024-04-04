from django.urls import path
from apps.myapp import views

urlpatterns = [
    path('food/', views.FoodList.as_view()),
    path('food/<uuid:pk>/', views.FoodDetail.as_view()),
]
