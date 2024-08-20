"""
We can write our own serializers
"""
from rest_framework import serializers


class MyCourseSerializers(serializers.Serializer):
    course = serializers.CharField(max_length=100)
    mode = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)

