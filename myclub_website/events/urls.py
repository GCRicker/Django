from django.urls import path
from . import views

urlpatterns = [

    # Path Inverters
    # int: numbers
    # str: strings
    # path: whole urls with /
    # slug: hyphen and underscores stuff
    # UUID: usernumber

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),

]