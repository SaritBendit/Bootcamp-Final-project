from django.urls import path
from . import views

from .views import BusinessList, BusinessDetail, SignUpClientView, SignUpBusinessView

app_name = "core"

urlpatterns = [
    path('', views.search, name="search"),
    path('business-list/', BusinessList.as_view(), name="business-list"),
    path('<int:pk>/', BusinessDetail.as_view(), name="business-detail"),
    path('business-signup/', SignUpBusinessView.as_view(), name="business-create"),
    path('client-signup/', SignUpClientView.as_view(), name="client-create"),
    path('appointment/', AppointmentView.as_view(), name="appointment-create"),

    # path('treatments/<int:pk>/', views.treatments_page, name="treatments_page"),
]
