from django.urls import path
from .views import tasks_list
urlpatterns = [
    path('', tasks_list, name = "tasks_list"),
    path('done/', tasks_list, name = "tasks_done_list"),
    path('today/', tasks_list, name = "tasks_today_list"),

    
]