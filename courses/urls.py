from django.urls import path
from courses.views import (
    CreateCourseView, GetCoursesView, GetCourseView, UpdateCourseView, DeleteCourseView
)

urlpatterns = [
    #Define cada ruta con su respectiva vista
    #El metodo as_view() convierte la vista en una vista basada en clases
    path("", GetCoursesView.as_view(), name="list_courses"), #Ruta para obtener todos los cursos
    path("create/", CreateCourseView.as_view(), name="create_course"), #Ruta para crear un curso
    path("<int:course_id>/", GetCourseView.as_view(), name="get_course"), #Ruta para obtener un curso
    path("update/<int:course_id>/", UpdateCourseView.as_view(), name="update_course"), #Ruta para actualizar un curso
    path("delete/<int:course_id>/", DeleteCourseView.as_view(), name="delete_course"), #Ruta para eliminar un curso
]