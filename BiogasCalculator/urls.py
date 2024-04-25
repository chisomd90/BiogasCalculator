"""
URL configuration for BiogasCalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import (
    calculate_percentage_of_fat,
    calculate_percentage_of_ash,
    calculate_percentage_of_fibre,
    calculate_percentage_of_moisture,
    calculate_percentage_of_protein,
    calculate_percentage_of_carbohydrate,
    calculate_determination_of_total_solids,
    calculate_determination_of_volatile_solids,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_percentage_of_fat/', calculate_percentage_of_fat, name='calculate_percentage_of_fat'),
    path('calculate_percentage_of_ash/', calculate_percentage_of_ash, name='calculate_percentage_of_ash'),
    path('calculate_percentage_of_fibre/', calculate_percentage_of_fibre, name='calculate_percentage_of_fibre'),
    path('calculate_percentage_of_moisture/', calculate_percentage_of_moisture, name='calculate_percentage_of_moisture'),
    path('calculate_percentage_of_protein/', calculate_percentage_of_protein, name='calculate_percentage_of_protein'),
    path('calculate_percentage_of_carbohydrate/', calculate_percentage_of_carbohydrate, name='calculate_percentage_of_carbohydrate'),
    path('calculate_determination_of_total_solids/', calculate_determination_of_total_solids, name='calculate_determination_of_total_solids'),
    path('calculate_determination_of_volatile_solids/', calculate_determination_of_volatile_solids, name='calculate_determination_of_volatile_solids'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)