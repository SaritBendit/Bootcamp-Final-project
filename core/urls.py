from django.urls import path
from . import views

from .views import BusinessList, BusinessDetail, SignUpBusinessView

app_name = "core"

urlpatterns = [
    path('', views.search, name="search"),
    path('business-list/', BusinessList.as_view(), name="business-list"),
    path('<int:pk>/', BusinessDetail.as_view(), name="business-detail"),
    path('businessSignUp/', SignUpBusinessView.as_view(), name="business-form"),
    path('clientSignUp/', SignUpClientView.as_view(), name="business-form"),

    # path('treatments/<int:pk>/', views.treatments_page, name="treatments_page"),
]
