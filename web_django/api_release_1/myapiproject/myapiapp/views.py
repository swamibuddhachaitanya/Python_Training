"""
myapiapp/views.py
"""
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def mytestapi(request):
    my_course = {"course": "python", "location": "india", "mode":"classroom"}
    return JsonResponse(my_course)

from django.core import serializers
from .models import MyModel
def getdbdata(request):
    response = MyModel.objects.all()
    serialized_response = serializers.serialize('json', response, fields=['id', "course", "mode", "location"])
    return JsonResponse(serialized_response, safe=False)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def postdbdata(request):
    received_data = request.POST
    course_exists = MyModel.objects.filter(course=received_data.get('course')).exists()
    if course_exists is True:
        return JsonResponse({"message": "Course Exists"}, status=409)
    else:
        new_course = MyModel()
        new_course.course = received_data.get("course")
        new_course.mode = received_data.get("mode")
        new_course.location = received_data.get("location")
        new_course.save()
        return JsonResponse({"message": "Course Added"}, status=200)


from django.http import QueryDict
@csrf_exempt
def putdbdata(request):
    #all data will be in 'body' for PUT, PATCH and DELETE
    received_data = request.body
    received_data = QueryDict(received_data)

    course_exists = MyModel.objects.filter(course=received_data.get('course')).exists()
    if course_exists is True:
        new_course = MyModel.objects.get(course=received_data.get('course'))
        new_course.course = received_data.get("course")
        new_course.mode = received_data.get("mode")
        new_course.location = received_data.get("location")
        new_course.save()
        return JsonResponse({"message": "Course Updated"}, status=200)
    else:
        new_course = MyModel()
        new_course.course = received_data.get("course")
        new_course.mode = received_data.get("mode")
        new_course.location = received_data.get("location")
        new_course.save()
        return JsonResponse({"message": "Course Added"}, status=200)

@csrf_exempt
def patchdbdata(request):
    #all data will be in 'body' for PUT, PATCH and DELETE
    received_data = request.body
    received_data = QueryDict(received_data)

    course_exists = MyModel.objects.filter(course=received_data.get('course')).exists()
    if course_exists is True:
        new_course = MyModel.objects.get(course=received_data.get('course'))
        new_course.course = received_data.get("course")
        new_course.mode = received_data.get("mode")
        new_course.location = received_data.get("location")
        new_course.save()
        return JsonResponse({"message": "Course Updated"}, status=200)
    else:
        return JsonResponse({"message": "Course not present"}, status=409)

@csrf_exempt
def deletedbdata(request):
    #all data will be in 'body' for PUT, PATCH and DELETE
    received_data = request.body
    received_data = QueryDict(received_data)

    course_exists = MyModel.objects.filter(course=received_data.get('course')).exists()
    if course_exists is True:
        req_course = MyModel.objects.get(course=received_data.get('course'))
        req_course.delete()
        return JsonResponse({"message": "Course deleted"}, status=200)
    else:
        return JsonResponse({"message": "Course not present"}, status=409)