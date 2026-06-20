from django.contrib import admin
from django.urls import path, include
from employe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employe.urls'))
]
