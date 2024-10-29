from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('lender_dashboard/' , views.lender_dashboard , name = 'lender_dashboard'),
    path('borrower_dashboard/' , views.borrower_dashboard , name = 'borrower_dashboard'),
    path('sign_up/' , views.sign_up , name='sign_up'),
    path('login/' , views.login_view , name='login_view')
]