from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .serializers import MyCourseSerializers
from .models import MyModel
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class MyAPIClass(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MyCourseSerializers

    def get(self, request):
        db_data = MyModel.objects.all()
        db_data_serialized = self.serializer_class(db_data, many=True)
        return Response(db_data_serialized.data)

    def post(self, request):
        received_data = request.data
        received_data_de_serialized = self.serializer_class(data=received_data)
        if received_data_de_serialized.is_valid():
            valid_data = received_data_de_serialized.validated_data
            verify_record = MyModel.objects.filter(course =valid_data.get('course'))
            if verify_record:
                return Response("Course already present", status=409)
            else:
                new_course = MyModel()
                new_course.course = valid_data.get("course")
                new_course.mode = valid_data.get("mode")
                new_course.location = valid_data.get("location")
                new_course.save()
                return Response("New Course Added", status=201)
        else:
            return Response("Passed Invalid Data Please Check", status=200)

    def put(self, request):
        received_data = request.data
        received_data_de_serialized = self.serializer_class(data=received_data)
        if received_data_de_serialized.is_valid():
            valid_data = received_data_de_serialized.validated_data
            verify_record = MyModel.objects.filter(course =valid_data.get('course'))
            if verify_record:
                existing_course = MyModel.objects.get(course=valid_data.get('course'))
                existing_course.course = valid_data.get('course')
                existing_course.mode = valid_data.get('mode')
                existing_course.location = valid_data.get('location')
                existing_course.save()
                return Response("Course updated", status=200)
            else:
                new_course = MyModel()
                new_course.course = valid_data.get("course")
                new_course.mode = valid_data.get("mode")
                new_course.location = valid_data.get("location")
                new_course.save()
                return Response("New Course Added", status=201)
        else:
            return Response("Passed Invalid Data Please Check", status=200)

    def patch(self, request):
        received_data = request.data
        received_data_de_serialized = self.serializer_class(data=received_data)
        if received_data_de_serialized.is_valid():
            valid_data = received_data_de_serialized.validated_data
            verify_record = MyModel.objects.filter(course=valid_data.get('course'))
            if verify_record:
                existing_course = MyModel.objects.get(course=valid_data.get('course'))
                existing_course.course = valid_data.get('course')
                existing_course.mode = valid_data.get('mode')
                existing_course.location = valid_data.get('location')
                existing_course.save()
                return Response("Course updated", status=200)
            else:

                return Response("No such record present to update", status=409)
        else:
            return Response("Passed Invalid Data Please Check", status=400)


    def delete(self,request):

        received_data = request.data
        received_data_de_serialized = self.serializer_class(data=received_data)
        if received_data_de_serialized.is_valid():
            valid_data = received_data_de_serialized.validated_data
            verify_record = MyModel.objects.filter(course=valid_data.get('course'))
            if verify_record:
                existing_course = MyModel.objects.get(course=valid_data.get('course'))
                existing_course.delete()
                return Response("Course deleted", status=200)
            else:

                return Response("No such record present to delete", status=409)
        else:
            return Response("Passed Invalid Data Please Check", status=400)