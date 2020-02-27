from django.urls import path
from . import views

from .views import BusinessList, BusinessDetail, SignUpClientView, SignUpBusinessView, AppointmentView, DiaryView

app_name = "core"

urlpatterns = [
    path('', views.search, name="search"),
    path('business-list/', BusinessList.as_view(), name="business_list"),
    path('<int:pk>/', BusinessDetail.as_view(), name="business_detail"),
    path('business-signup/', SignUpBusinessView.as_view(), name="business_form"),
    path('client-signup/', SignUpClientView.as_view(), name="client_create"),
    path('<int:business_id>/appointment/', AppointmentView.as_view(), name="appointment_form"),
    path('diary/', DiaryView.as_view(), name="diary_form")

    # path('treatments/<int:pk>/', views.treatments_page, name="treatments_page"),
]
