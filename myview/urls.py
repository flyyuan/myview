from django.urls import path
from myview.views import get_status
from myview.views import index

urlpatterns = [
    path('', index, name='index'),
    path('get_status/', get_status, name='get_status'),
]

