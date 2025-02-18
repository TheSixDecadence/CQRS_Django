from django.urls import path
from courses.views import (
    CreateCourseView, GetCoursesView, GetCourseView, UpdateCourseView, DeleteCourseView
)

urlpatterns = [
    path("", GetCoursesView.as_view(), name="list_courses"),
    path("create/", CreateCourseView.as_view(), name="create_course"),
    path("<int:course_id>/", GetCourseView.as_view(), name="get_course"),
    path("update/<int:course_id>/", UpdateCourseView.as_view(), name="update_course"),
    path("delete/<int:course_id>/", DeleteCourseView.as_view(), name="delete_course"),
]