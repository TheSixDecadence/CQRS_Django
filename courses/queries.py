from courses.models import CourseQuery

def get_course(course_id: int):
    #Obtiene un curso específico por ID.
    return CourseQuery.objects.get(id=course_id)

def get_courses():
    #Obtiene la lista de todos los cursos.
    return CourseQuery.objects.all()
