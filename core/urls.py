from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('buisness_page/', views.business_page, name="buisness_page"),
    path('treatments/<int:pk>/', views.treatments_page, name="treatments_page"),
]
