from django.urls import path
from .views import x

urlpatterns = [
    path("",x,name="x")
]