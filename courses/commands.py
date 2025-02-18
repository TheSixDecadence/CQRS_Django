from courses.models import CourseCommand

def create_course(title: str, description: str):
    #Crea un curso en la base de datos.
    return CourseCommand.objects.create(title=title, description=description)

def update_course(course_id: int, title: str, description: str):
    #Actualiza un curso existente.
    course = CourseCommand.objects.get(id=course_id)
    course.title = title
    course.description = description
    course.save()
    return course

def delete_course(course_id: int):
    #Elimina un curso de la base de datos.
    course = CourseCommand.objects.get(id=course_id)
    course.delete()
