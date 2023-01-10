from django.urls import path
from . import views
from .views import *

app_name = "training"

urlpatterns = [
    # path('', name='training'),
    path('community/', community, name='community'),
    path('community-add/', community_add, name='community_add'),
    path('community-update/<int:id>/', community_update, name='community_update'),
    path('community-delete/<int:id>/', deleteCommunity, name='community-delete'),

    path('interviews/', interviews, name='interviews'),
    path('interview-detail/<int:id>/', detailInterview, name='detail-interview'),
    path('interview-add/<int:id>/', addInterview, name='add-interview'),
    path('interview-update/<int:id>/', updateInterview, name='update-interview'),
    path('interview-delete/<int:id>/', interviewDelete, name='interview-delete'),

    path('interviews-statu/', interviews_statu, name='interviews_statu'),
    path('interviews-statu-add/', interviews_statu_add, name='interviews-statu-add'),
    path('interviews-statu-delete/<int:id>/', interviews_statu_delete, name='interviews-statu-delete'),
    path('interviews-statu-update/<int:id>/', interviews_statu_update, name='interviews-statu-update'),

    path('search/', search, name='search'),
    path('data-transfer/', data_transfer, name='data-transfer'),

]
