from django.urls import path
from dashboard.views import RandomDataView
from . import views
urlpatterns=[
    path('dashboard',views.dashboard,name='dashboard'),
    path('random_data/',RandomDataView.as_view(),name='random_data')

]