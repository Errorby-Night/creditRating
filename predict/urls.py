from django.urls import path
from predict.views import index
urlpatterns = [
    path('', index)
]