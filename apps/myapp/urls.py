from django.urls import path
from apps.myapp import views

urlpatterns = [
    path('food/', views.FoodList.as_view()),
    path('food/<uuid:pk>/', views.FoodDetail.as_view()),
    path('consume/', views.ConsumeList.as_view()),
    path('consume/<uuid:pk>/', views.ConsumeDetail.as_view()),
    path('register/', views.register_user)
]
