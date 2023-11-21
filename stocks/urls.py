from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('get_historic_data/<str:symbol>/', views.get_historic_data, name='get_historic_data'),
    path('stockinfo/<str:symbol>/', views.stockinfo, name='stockinfo'),
]
