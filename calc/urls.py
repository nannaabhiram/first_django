from django.contrib import admin
from django.urls import path, include
from .views import landing, calculator, about  # calc.views.*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='home'),          # Home -> landing (button to Page 1)
    path('page1/', calculator, name='page1'),# Page 1 -> calculator
    path('about/', about, name='about'),     # Brand -> about project
]