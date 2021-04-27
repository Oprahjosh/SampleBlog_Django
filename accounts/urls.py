from django.urls import path
from .views import accant

app_name = 'accounts'

urlpatterns = [
    path('',accant, name='accounts')
]