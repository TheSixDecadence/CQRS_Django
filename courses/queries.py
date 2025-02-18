from courses.models import CourseQuery #Se utiliza el modelo CourseQuery para hacer consultas a la base de datos.

#Aqui se definen las consultas que se pueden hacer a la base de datos.
def get_course(course_id: int):
    #Obtiene un curso específico por ID.
    return CourseQuery.objects.get(id=course_id)

def get_courses():
    #Obtiene la lista de todos los cursos.
    return CourseQuery.objects.all()
