from django.urls import path
from courses.views import (
    CreateCourseView, GetCoursesView, GetCourseView, UpdateCourseView, DeleteCourseView
)

urlpatterns = [
    #Define cada ruta con su respectiva vista
    #El metodo as_view() convierte la vista en una vista basada en clases
    path("", GetCoursesView.as_view(), name="getCourses"), #Ruta para obtener todos los cursos
    path("create/", CreateCourseView.as_view(), name="createCourse"), #Ruta para crear un curso
    path("<int:course_id>/", GetCourseView.as_view(), name="getCourse"), #Ruta para obtener un curso
    path("update/<int:course_id>/", UpdateCourseView.as_view(), name="updateCourse"), #Ruta para actualizar un curso
    path("delete/<int:course_id>/", DeleteCourseView.as_view(), name="deleteCourse"), #Ruta para eliminar un curso
]