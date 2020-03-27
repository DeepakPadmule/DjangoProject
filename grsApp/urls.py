from django.urls import path

from . import views

urlpatterns = [
    path('grievances', views.GrievanceList.as_view()),
    path('grievances/<str:pk>', views.GrievanceUpdate.as_view()),
    path('grievanceTypes', views.GrievanceTypeList.as_view()),
    path('grievanceTypes/<str:pk>', views.GrievanceTypeUpdate.as_view()),
    path('grievanceDetails', views.GrievanceDetailList.as_view()),
    path('grievanceDetails/<str:pk>', views.GrievanceDetailUpdate.as_view()),
]
