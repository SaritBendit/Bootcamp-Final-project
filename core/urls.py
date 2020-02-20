from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.search, name="search"),
    path('business_page/', views.business_page, name="business_page"),
    path('treatments/<int:pk>/', views.treatments_page, name="treatments_page"),
]
