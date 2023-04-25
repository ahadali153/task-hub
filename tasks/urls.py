from django.urls import path
from tasks.views import create_task, show_tasks_list

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_tasks_list, name="show_my_tasks"),
]
