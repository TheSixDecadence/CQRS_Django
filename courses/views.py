import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from courses.commands import createCourse, updateCourse, deleteCourse
from courses.queries import getCourse, getCourses
from courses.models import CourseCommand, CourseQuery

@method_decorator(csrf_exempt, name='dispatch') # Decorador para deshabilitar CSRF
# Se deshabilita CSRF para poder hacer peticiones POST, PUT y DELETE desde Postman/Thunder Client.
# CSRF es un mecanismo de seguridad que protege a los usuarios de ataques de falsificación de solicitudes entre sitios.
class CreateCourseView(View):
    # Método POST para crear un curso
    def post(self, request):
        try:
            # Intentar obtener datos en formato JSON
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
        except json.JSONDecodeError:
            # Intentar obtener datos de form-data
            title = request.POST.get('title')
            description = request.POST.get('description')

        createCourse(title, description)

        return JsonResponse({"message": "Curso creado correctamente"}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateCourseView(View):
    # Método PUT para actualizar un curso
    def put(self, request, course_id): # Se recibe el ID del curso a actualizar
        try:
            # Intentar obtener datos en formato JSON
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
        except json.JSONDecodeError:
            # Intentar obtener datos de form-data
            title = request.POST.get('title')
            description = request.POST.get('description')

        try:
            # Actualizar el curso
            updateCourse(course_id, title, description)
            return JsonResponse({"message": "Curso eliminado correctamente"}, status=201)
        except CourseCommand.DoesNotExist:
            # Si no se encuentra el curso, devolver un error 404
            return JsonResponse({"error": "Curso no encontrado"}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class DeleteCourseView(View):
    # Método DELETE para eliminar un curso
    def delete(self, request, course_id):
        try:
            # Eliminar el curso
            deleteCourse(course_id)
        except CourseCommand.DoesNotExist:
            # Si no se encuentra el curso, devolver un error 404
            return JsonResponse({"error": "Curso no encontrado"}, status=404)

class GetCoursesView(View):
    # Método GET para obtener todos los cursos
    def get(self, request):
        courses = getCourses()
        data = [{
            'id': course.id, 
            'title': course.title, 
            'description': course.description
            } 
        for course in courses]
        return JsonResponse({"courses": data})

class GetCourseView(View):
    # Método GET para obtener un curso específico
    def get(self, request, course_id):
        try:
            course = getCourse(course_id)
            return JsonResponse({
                'id': course.id,
                'title': course.title,
                'description': course.description
            })
        except CourseQuery.DoesNotExist:
            # Si no se encuentra el curso, devolver un error 404
            return JsonResponse({"error": "Curso no encontrado"}, status=404)
