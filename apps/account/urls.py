from django.urls import path
from .views import activate_account


urlpatterns = [
    path('activate/<str:uid>/<str:token>/', activate_account, name='account-activation'),
]
