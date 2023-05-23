from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('fullmatch/', views.full_match, name='full_match'),
    path('firstmatch/', views.first_match, name='first_match'),
    path("", HomePageView.as_view(), name="home"),
]