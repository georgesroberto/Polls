# Writing URLS

from django.urls import path
from .views import *

app_name = "polls"

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('results/<int:question_id>/', results, name='results'),
    path('vote/<int:question_id>', vote, name='vote'),
]