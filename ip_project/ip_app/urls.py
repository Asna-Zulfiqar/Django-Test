from django.urls import path
from . import views

urlpatterns = [
    path('local_view/' , views.local , name = 'local'),
    path('live_view/' , views.live , name = 'live'),
    path('local_mid/', views.local_page, name='local_page'),
    path('live_mid/', views.live_page, name='live_page'),
    path('live_dec/' , views.live_page_view , name= 'live_page_view'),
    path('local_dec/' , views.local_page_view , name = 'local_page_view'),
]


