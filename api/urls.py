from django.urls import path

from api.views import Page_list, Page_detail

urlpatterns = [
    path('polls/', Page_list.as_view(), name='polls_list'),
    path('polls/<int:pk>', Page_detail.as_view(), name='polls_detail')
]
