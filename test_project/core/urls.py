from django.urls import path
from .views import ScrapedListView

urlpatterns = [
    path('', ScrapedListView.as_view(), name= 'index'),
]
