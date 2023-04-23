from django.urls import path
from . import views

urlpatterns = [
    path('api/recommendations', views.ContactList.as_view(), name='recommendation_list'),handling
    path('api/recommendations/<int:pk>', views.RecommendationDetail.as_view(), name='recommendation_detail'),
]
