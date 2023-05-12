"""class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
#from api.views import productsView,MorningView,EveningView
#from api.views import AddView,SubtractiveView
from api.views import CubeView
from api.views import FactorialView,WorldcountView,ProductView,ProductDetailView,ReviewsView,ReviewDetailsView
from api.views import ProductsViewsetView

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v1/products",ProductsViewsetView,basename="products")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cube",CubeView.as_view()),
    path("fact",FactorialView.as_view()),
    path("worldcount",WorldcountView.as_view()),
    path("products",ProductView.as_view()),
    path("products/<int:id>",ProductDetailView.as_view()),
    path("reviews",ReviewsView.as_view()),
    path("reviews/<int:id>",ReviewDetailsView.as_view())
   # path("add",AddView.as_view()),

    #path("sub",SubtractiveView.as_view())
]+router.urls

