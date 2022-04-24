
from django.urls import path
from firstfloor import views
urlpatterns = [
    
    path('dear/', views.home),
    path('sir/',views.flat),
]
