from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', lambda request: HttpResponse({"Bienvenido a la mejor plataforma de E-Learning"}))
]
