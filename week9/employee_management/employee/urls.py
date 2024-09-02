from django.urls import path
from employee import views

urlpatterns = [
    path("", views.employee, name="employee"),
    path("position/", views.position, name="position"),
    path("project/", views.project, name="project"),
    path("project/delete/<int:project_id>/", views.project_delete, name="project_delete"),
    path("project_detail/<int:project_id>/", views.project_detail, name="project_detail"),
    path("project_detail/<int:project_id>/<int:employee_id>/manage/", views.project_detail_manage, name="project_detail_manage"),
    path("add_employee/", views.add_employee, name="add_employee"),
]
