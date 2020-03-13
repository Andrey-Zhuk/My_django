# обрабатывает входящие запросы

from gjango.urls import path

from .views import *

urlpatterns = [
    path('', posts_list)
]






