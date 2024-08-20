from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import MyCourseSerializer
from .models import MyModel
from rest_framework.response import Response

class MyAPIClass(APIView):
    serializer_class = MyCourseSerializer

    def get(self, request):
        db_data = MyModel.objects.all()
        db_data_serialized = self.serializer_class(db_data, many=True)
        return Response(db_data_serialized.data)

    def post(self, request):
        received_data = request.data
        received_data_de_serialized = self.serializer_class(data=received_data)
        if received_data_de_serialized.is_valid():
            valid_data = received_data_de_serialized.validated_data
            verify_record = MyModel.objects.filter(course=valid_data.get("course")).exists()
            if verify_record is True:
                return Response("Course Already Present", status=200)
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
            verify_record = MyModel.objects.filter(course=valid_data.get("course")).exists()
            if verify_record is True:
                new_course = MyModel.objects.get(course=valid_data.get("course"))
                new_course.course = valid_data.get("course")
                new_course.mode = valid_data.get("mode")
                new_course.location = valid_data.get("location")
                new_course.save()
                return Response("Course Updated", status=200)
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
            verify_record = MyModel.objects.filter(course=valid_data.get("course")).exists()
            if verify_record is True:
                new_course = MyModel.objects.get(course=valid_data.get("course"))
                new_course.course = valid_data.get("course")
                new_course.mode = valid_data.get("mode")
                new_course.location = valid_data.get("location")
                new_course.save()
                return Response("Course Updated", status=200)
            else:
                return Response("No Record Present To Update", status=201)
        else:
            return Response("Passed Invalid Data Please Check", status=200)

    def delete(self, request):
        received_data = request.data
        received_data_de_serialized = self.serializer_class(data=received_data)
        if received_data_de_serialized.is_valid():
            valid_data = received_data_de_serialized.validated_data
            verify_record = MyModel.objects.filter(course=valid_data.get("course")).exists()
            if verify_record is True:
                new_course = MyModel.objects.get(course=valid_data.get("course"))
                new_course.delete()
                return Response("Course Deleted", status=200)
            else:
                return Response("No Record Present To Delete", status=201)
        else:
            return Response("Passed Invalid Data Please Check", status=200)